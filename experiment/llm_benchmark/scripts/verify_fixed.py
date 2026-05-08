import csv

with open('llm_new_res_v3_fixed.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    print('修复后的文件结构:')
    print(f'总列数: {len(reader.fieldnames)}')
    print()
    print('列名:')
    for i, col in enumerate(reader.fieldnames):
        print(f'  {i}: {col}')
    
    print()
    print('前5行的数据样本:')
    for i, row in enumerate(reader):
        if i < 5:
            print(f'\n第{i+1}行:')
            print(f'  reference_id: {row["reference_id"]}')
            print(f'  similarity_correct: {row["similarity_correct"]}')
            print(f'  dblp_title_similarity: {row["dblp_title_similarity"]}')
            print(f'  dblp_match_status: {row["dblp_match_status"]}')
            print(f'  original_title: {row["original_title"][:50]}...' if len(row["original_title"]) > 50 else f'  original_title: {row["original_title"]}')
        else:
            break
