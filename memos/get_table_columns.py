from sql_metadata import Parser

# 从SQL文件中读取内容
def read_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        sql_text = sql_file.read()
    return sql_text

if __name__ == "__main__":
    sql_file_path = 'your_sql_file.sql'  # 请替换为实际的SQL文件路径

    sql_text = read_sql_file(sql_file_path)

    parser = Parser(sql_text)
    data_source_tables = parser.tables
    required_columns = parser.columns

    print("数据源表：", data_source_tables)
    print("所需列：", required_columns)
