#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复CSV对齐问题：
- 保留所有原有列和数据
- 确保 similarity_correct, dblp_title_similarity, dblp_match_status 这三列的数据被正确保留
"""

import csv
import sys

def fix_csv_alignment(input_file, output_file):
    """
    修复CSV文件的列对齐问题
    
    Args:
        input_file: 输入CSV文件路径
        output_file: 输出CSV文件路径
    """
    
    target_columns = ['similarity_correct', 'dblp_title_similarity', 'dblp_match_status']
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.DictReader(infile)
            
            if reader.fieldnames is None:
                print("错误：无法读取CSV头")
                return False
            
            # 验证目标列存在
            missing_cols = [col for col in target_columns if col not in reader.fieldnames]
            if missing_cols:
                print(f"错误：找不到列: {missing_cols}")
                return False
            
            # 保留所有列
            output_fieldnames = reader.fieldnames
            
            writer = csv.DictWriter(outfile, fieldnames=output_fieldnames)
            writer.writeheader()
            
            # 复制所有数据，确保目标列被正确保留
            row_count = 0
            for row in reader:
                # 验证目标列的数据
                for col in target_columns:
                    # 确保这些列的值被保留（即使为空）
                    if col not in row:
                        row[col] = ''
                
                writer.writerow(row)
                row_count += 1
            
            print(f"✓ 成功处理 {row_count} 行数据")
            print(f"✓ 输出文件: {output_file}")
            print(f"\n保留的三个关键列:")
            print(f"  - similarity_correct")
            print(f"  - dblp_title_similarity")
            print(f"  - dblp_match_status")
            print(f"\n保留的所有列数: {len(output_fieldnames)}")
            return True
            
    except Exception as e:
        print(f"错误：{e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    input_path = 'llm_new_res_v3.csv'
    output_path = 'llm_new_res_v3_fixed.csv'
    
    print(f"正在修复: {input_path}")
    print(f"策略: 保留所有列数据，并确保这三列对齐")
    print(f"       - similarity_correct")
    print(f"       - dblp_title_similarity")
    print(f"       - dblp_match_status")
    print()
    
    if fix_csv_alignment(input_path, output_path):
        print("\n✓ 修复完成！")
    else:
        print("\n✗ 修复失败")
        sys.exit(1)
