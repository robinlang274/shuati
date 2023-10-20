import re

# 从SQL文件中读取视图定义
def read_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        sql_text = sql_file.read()
    return sql_text

# 提取视图需要的数据源表
def extract_data_source_table(sql_text):
    source_tables = re.findall(r'FROM `([^`]+)`', sql_text)
    return source_tables

# 提取视图需要的列名
def extract_required_columns(sql_text):
    select_clause = re.search(r'SELECT ([^;]+)', sql_text)
    if select_clause:
        required_columns = select_clause.group(1).split(', ')
        return required_columns
    else:
        return []

if __name__ == "__main__":
    sql_file_path = 'your_sql_file.sql'  # 请替换为实际的SQL文件路径

    sql_text = read_sql_file(sql_file_path)
    data_source_tables = extract_data_source_table(sql_text)
    required_columns = extract_required_columns(sql_text)

    print("数据源表：", data_source_tables)
    print("所需列：", required_columns)
