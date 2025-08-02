-- models/flights_cleaned.sql

WITH source AS (
    SELECT *
    FROM public.flights_raw
    WHERE "DEPARTURE_TIME" IS NOT NULL
      AND "ARRIVAL_TIME" IS NOT NULL
)

SELECT
    "FLIGHT_DATE" AS flight_date,
    "AIRLINE" AS airline,
    "ORIGIN_AIRPORT" AS origin_airport,
    "DESTINATION_AIRPORT" AS destination_airport,
    "DEPARTURE_TIME" AS departure_time,
    "ARRIVAL_TIME" AS arrival_time,
    "AIR_TIME" AS air_time,
    "DISTANCE" AS distance,
    "CANCELLED" AS cancelled,
    "CANCELLATION_REASON" AS cancellation_reason
FROM source
