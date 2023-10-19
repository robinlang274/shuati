WITH
  view_name AS (
    SELECT 'your_project.your_dataset.your_view' AS view_name
  ),
  parsed_view AS (
    SELECT
      CONCAT(table_catalog, '.', table_schema, '.', table_name) AS view_name,
      view_query AS view_definition
    FROM
      `your_project.your_dataset.INFORMATION_SCHEMA.VIEWS`
  )
SELECT
  view_name,
  REGEXP_EXTRACT(view_definition, r'FROM `([^`]+)`') AS data_source_table,
  REGEXP_EXTRACT_ALL(view_definition, r'SELECT ([^ ]+)') AS required_columns
FROM
  parsed_view
WHERE view_name IN (SELECT view_name FROM view_name);