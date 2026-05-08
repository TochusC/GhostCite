import os
import re
import sqlite3
import time
import unicodedata
from typing import Iterable, Optional

from lxml import etree as LET

DBLP_XML = r"d:\Project\GhostCite\Experiment\4_llm_generated_citations\dblp\dblp.xml"
DB_PATH = r"d:\Project\GhostCite\Experiment\4_llm_generated_citations\dblp\dblp_titles.sqlite"

ENTRY_TAGS = {
    "article",
    "inproceedings",
    "proceedings",
    "book",
    "incollection",
    "phdthesis",
    "mastersthesis",
    "www",
}


def normalize_title(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def iter_dblp_titles(xml_path: str) -> Iterable[tuple]:
    # lxml with DTD entity resolution to handle &uuml; etc.
    context = LET.iterparse(
        xml_path,
        events=("end",),
        load_dtd=True,
        resolve_entities=True,
        huge_tree=True,
    )
    _, root = next(context)
    for _, elem in context:
        tag = elem.tag
        if tag not in ENTRY_TAGS:
            continue
        title_elem = elem.find("title")
        if title_elem is None or not (title_elem.text or "").strip():
            elem.clear()
            continue
        title = " ".join(title_elem.itertext()).strip()
        if not title:
            elem.clear()
            continue
        key = elem.attrib.get("key", "")
        year = (elem.findtext("year") or "").strip()
        venue = (elem.findtext("journal") or elem.findtext("booktitle") or "").strip()
        authors = [a.text.strip() for a in elem.findall("author") if a.text]
        yield (key, tag, title, normalize_title(title), year, venue, "; ".join(authors))
        elem.clear()
        root.clear()


def build_sqlite_index(
    xml_path: str,
    db_path: str,
    batch_size: int = 2000,
    progress_every: int = 5000,
) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode = WAL")
    cur.execute("PRAGMA synchronous = NORMAL")
    cur.execute("PRAGMA temp_store = MEMORY")

    cur.execute(
        """
        CREATE TABLE entries (
            id INTEGER PRIMARY KEY,
            dblp_key TEXT,
            type TEXT,
            title TEXT,
            title_norm TEXT,
            year TEXT,
            venue TEXT,
            authors TEXT
        )
        """
    )
    cur.execute("CREATE INDEX idx_title_norm ON entries(title_norm)")

    buffer = []
    total = 0
    last_report = time.time()
    for row in iter_dblp_titles(xml_path):
        buffer.append(row)
        if len(buffer) >= batch_size:
            cur.executemany(
                "INSERT INTO entries (dblp_key, type, title, title_norm, year, venue, authors) VALUES (?, ?, ?, ?, ?, ?, ?)",
                buffer,
            )
            conn.commit()
            total += len(buffer)
            buffer.clear()

            if total % progress_every == 0:
                now = time.time()
                elapsed = now - last_report
                last_report = now
                rate = progress_every / elapsed if elapsed > 0 else 0
                print(f"Indexed {total:,} entries (+{rate:,.0f}/s)")

    if buffer:
        cur.executemany(
            "INSERT INTO entries (dblp_key, type, title, title_norm, year, venue, authors) VALUES (?, ?, ?, ?, ?, ?, ?)",
            buffer,
        )
        conn.commit()
        total += len(buffer)

    print(f"Done. Total indexed: {total:,}")

    conn.close()


def find_by_title(db_path: str, title: str, limit: int = 5) -> list[tuple]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    title_norm = normalize_title(title)
    cur.execute(
        "SELECT dblp_key, type, title, year, venue, authors FROM entries WHERE title_norm = ? LIMIT ?",
        (title_norm, limit),
    )
    rows = cur.fetchall()
    conn.close()
    return rows


# 1) Build index (first run will take a while for 4GB XML)
build_sqlite_index(DBLP_XML, DB_PATH)

# 2) Query by exact title match (normalized)
# results = find_by_title(DB_PATH, "Attention Is All You Need")
# results
