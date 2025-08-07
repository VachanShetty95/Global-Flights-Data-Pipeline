SELECT
    f.airline_code,
    a.airline_name,
    ROUND(AVG(f.flight_duration_minutes), 2) AS avg_duration
FROM {{ ref('fact_flights') }} f
JOIN {{ ref('dim_airlines') }} a ON f.airline_code = a.airline_code
GROUP BY f.airline_code, a.airline_name
