-- models/dimensions/dim_airlines.sql

SELECT
    DISTINCT airline_code,
    airline_name
FROM {{ ref('flights_enriched') }}
WHERE airline_code IS NOT NULL
