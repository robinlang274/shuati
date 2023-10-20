import re

# 从SQL文件中逐行读取内容
def read_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        lines = sql_file.readlines()
    return lines

# 提取视图需要的数据源表
def extract_data_source_table(lines):
    source_tables = []
    for line in lines:
        match = re.search(r'FROM `([^`]+)`', line)
        if match:
            source_tables.append(match.group(1))
    return source_tables

# 提取视图需要的列名
def extract_required_columns(lines):
    in_select_clause = False
    required_columns = []
    
    for line in lines:
        if in_select_clause:
            line = line.strip()
            if line.endswith(','):
                line = line[:-1]
            if not line.endswith(';'):
                required_columns.append(line)
            else:
                in_select_clause = False
        if line.upper().startswith('SELECT '):
            in_select_clause = True
            required_columns.append(line[len('SELECT '):])

    return required_columns

if __name__ == "__main__":
    sql_file_path = 'your_sql_file.sql'  # 请替换为实际的SQL文件路径

    lines = read_sql_file(sql_file_path)
    data_source_tables = extract_data_source_table(lines)
    required_columns = extract_required_columns(lines)

    print("数据源表：", data_source_tables)
    print("所需列：", required_columns)
