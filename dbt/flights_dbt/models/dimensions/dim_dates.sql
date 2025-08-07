-- models/dim_dates.sql

WITH date_range AS (
    SELECT
        generate_series(
            '2015-01-01'::date,
            '2015-12-31'::date,
            interval '1 day'
        )::date AS date_day
)

SELECT
    date_day,
    EXTRACT(DAY FROM date_day) AS day,
    EXTRACT(MONTH FROM date_day) AS month,
    TO_CHAR(date_day, 'Month') AS month_name,
    EXTRACT(YEAR FROM date_day) AS year,
    EXTRACT(DOW FROM date_day) AS day_of_week,
    TO_CHAR(date_day, 'Day') AS day_name,
    CASE
        WHEN EXTRACT(DOW FROM date_day) IN (0, 6) THEN TRUE
        ELSE FALSE
    END AS is_weekend
FROM date_range
