WITH
  view_name AS (
    SELECT 'your_project.your_dataset.your_view' AS view_name
  ),
  view_definition AS (
    SELECT
      CONCAT(table_catalog, '.', table_schema, '.', table_name) AS view_name,
      view_query
    FROM
      `your_project.your_dataset.INFORMATION_SCHEMA.VIEWS`
  ),
  parsed_view AS (
    SELECT
      view_name,
      REGEXP_EXTRACT(view_query, r'FROM `([^`]+)`') AS data_source_table,
      REGEXP_EXTRACT_ALL(view_query, r'SELECT ([^ ]+)') AS required_columns
    FROM
      view_definition
    WHERE view_name IN (SELECT view_name FROM view_name)
  )
SELECT
  view_name,
  data_source_table AS data_source_table_name,
  ARRAY(SELECT column_name FROM UNNEST(required_columns) AS column_name) AS required_columns
FROM
  parsed_view;