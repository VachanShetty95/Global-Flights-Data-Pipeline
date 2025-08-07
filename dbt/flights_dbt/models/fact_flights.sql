WITH flights AS (
    SELECT *,
        -- Convert arrival & departure to minutes since midnight
        (
            (CAST(arrival_time AS INTEGER) / 100) * 60 +
            (CAST(arrival_time AS INTEGER) % 100)
        ) AS arr_mins,
        (
            (CAST(departure_time AS INTEGER) / 100) * 60 +
            (CAST(departure_time AS INTEGER) % 100)
        ) AS dep_mins
    FROM {{ ref('flights_enriched') }}
),
airlines AS (
    SELECT * FROM {{ ref('dim_airlines') }}
),
airports AS (
    SELECT * FROM {{ ref('dim_airports') }}
),
dates AS (
    SELECT * FROM {{ ref('dim_dates') }}
)

SELECT
    -- Foreign keys
    f.airline_code,
    f.origin_airport AS origin_airport_code,
    f.destination_airport AS destination_airport_code,
    f.flight_date,

    -- Fact metrics
    f.departure_time,
    f.arrival_time,
    f.air_time,
    f.distance,

    -- Calculated metric
    CASE
        WHEN f.arr_mins >= f.dep_mins THEN f.arr_mins - f.dep_mins
        ELSE (f.arr_mins + 24 * 60) - f.dep_mins
    END AS flight_duration_minutes,

    -- Optional enrichment
    a.airline_name,
    oa.airport_name AS origin_airport_name,
    da.airport_name AS destination_airport_name

FROM flights f
LEFT JOIN airlines a ON f.airline_code = a.airline_code
LEFT JOIN airports oa ON f.origin_airport = oa.airport_code
LEFT JOIN airports da ON f.destination_airport = da.airport_code
LEFT JOIN dates d ON CAST(f.flight_date AS DATE) = d.date_day
