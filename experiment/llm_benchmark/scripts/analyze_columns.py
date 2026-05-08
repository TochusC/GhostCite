import csv

with open('llm_new_res_v3.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    col_stats = {}
    for col in reader.fieldnames:
        col_stats[col] = {'non_empty': 0, 'empty': 0}
    
    for i, row in enumerate(reader):
        if i < 100:
            for col in reader.fieldnames:
                val = row.get(col, '')
                if val and val.strip():
                    col_stats[col]['non_empty'] += 1
                else:
                    col_stats[col]['empty'] += 1
        else:
            break
    
    print('前100行中各列的空值统计:')
    print('\n非空值较多的列 (>50% 非空):')
    for col, stats in col_stats.items():
        total = stats['non_empty'] + stats['empty']
        empty_pct = stats['empty'] / total * 100 if total > 0 else 0
        if empty_pct < 50:
            print(f'  {col}: 非空={stats["non_empty"]}, 空={stats["empty"]} ({empty_pct:.1f}%)')
    
    print('\n空值较多的列 (>50% 空):')
    for col, stats in col_stats.items():
        total = stats['non_empty'] + stats['empty']
        empty_pct = stats['empty'] / total * 100 if total > 0 else 0
        if empty_pct >= 50:
            print(f'  {col}: 非空={stats["non_empty"]}, 空={stats["empty"]} ({empty_pct:.1f}%)')
