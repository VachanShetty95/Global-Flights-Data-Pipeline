-- models/airports_enriched.sql

WITH flights AS (
    SELECT *
    FROM {{ ref('flights_cleaned') }}
),
airports AS (
    SELECT
        "IATA_CODE" AS iata_code,
        "AIRPORT" AS airport_name,
        "CITY" AS city,
        "STATE" AS state
    FROM public.airports
)

SELECT
    f.*,
    oa.airport_name AS origin_airport_name,
    oa.city AS origin_city,
    oa.state AS origin_state,
    da.airport_name AS destination_airport_name,
    da.city AS destination_city,
    da.state AS destination_state

FROM flights f
LEFT JOIN airports oa ON f.origin_airport = oa.iata_code
LEFT JOIN airports da ON f.destination_airport = da.iata_code
