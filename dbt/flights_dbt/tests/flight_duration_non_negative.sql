-- tests/flight_duration_non_negative.sql

SELECT *
FROM {{ ref('old_flight_facts') }}
WHERE flight_duration_minutes < 0
