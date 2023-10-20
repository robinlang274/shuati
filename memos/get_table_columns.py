import sqlparse

# 从SQL文件中读取内容
def read_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        sql_text = sql_file.read()
    return sql_text

# 指定感兴趣的表名
interested_table = 'your_table_name'  # 请替换为实际的表名

def extract_columns_related_to_table(sql_text, interested_table):
    columns = set()
    statements = sqlparse.parse(sql_text)

    for statement in statements:
        if isinstance(statement, sqlparse.sql.IdentifierList):
            # 查找每个IdentifierList中的列名
            for item in statement.get_identifiers():
                item_str = item.get_real_name()
                if f'`{interested_table}`.' in item_str:
                    # 如果列名包含了感兴趣的表名，添加到集合中
                    columns.add(item_str)

    return list(columns)

if __name__ == "__main__":
    sql_file_path = 'your_sql_file.sql'  # 请替换为实际的SQL文件路径
    sql_text = read_sql_file(sql_file_path)

    columns = extract_columns_related_to_table(sql_text, interested_table)

    print(f"与表 '{interested_table}' 相关的列：")
    for column in columns:
        print(column)
