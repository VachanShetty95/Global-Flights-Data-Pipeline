WITH airports AS (
    SELECT
        origin_airport AS airport_code,
        origin_airport_name AS airport_name,
        origin_city AS city,
        origin_state AS state
    FROM {{ ref('airports_enriched') }}
    WHERE origin_airport IS NOT NULL
      AND origin_airport_name IS NOT NULL
      AND origin_airport_name <> ''

    UNION

    SELECT
        destination_airport AS airport_code,
        destination_airport_name AS airport_name,
        destination_city AS city,
        destination_state AS state
    FROM {{ ref('airports_enriched') }}
    WHERE destination_airport IS NOT NULL
      AND destination_airport_name IS NOT NULL
      AND destination_airport_name <> ''
)

SELECT DISTINCT *
FROM airports
