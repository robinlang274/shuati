WITH
  -- 指定要查询的视图名称
  view_name AS (
    SELECT 'your_project.your_dataset.your_view' AS view_name
  ),
  -- 从INFORMATION_SCHEMA.VIEWS获取视图的定义
  view_definition AS (
    SELECT
      view_name,
      view_query
    FROM
      `your_project.your_dataset.INFORMATION_SCHEMA.VIEWS`
    WHERE
      CONCAT(table_catalog, '.', table_schema, '.', table_name) IN (SELECT view_name FROM view_name)
  ),
  -- 解析视图查询以获取数据源表和所需列
  parsed_view AS (
    SELECT
      view_name,
      REGEXP_EXTRACT(view_query, r'FROM `([^`]+)`') AS data_source_table,
      REGEXP_EXTRACT_ALL(view_query, r'SELECT ([^ ]+)') AS required_columns
    FROM
      view_definition
  )
-- 最终结果：数据源表和所需列
SELECT
  view_name,
  data_source_table AS data_source_table_name,
  ARRAY(SELECT column_name FROM UNNEST(required_columns) AS column_name) AS required_columns
FROM
  parsed_view;
