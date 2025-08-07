-- models/flight_facts.sql

with enriched as (
    select *
    from {{ ref('flights_enriched') }}
)

select
    flight_date,
    airline_name,
    origin_airport,
    destination_airport,
    distance,
    cancelled,
    cancellation_reason,

    -- Corrected calculation: cast to integer before modulo
case
    when
        ((cast(arrival_time as integer) / 100) * 60 + (cast(arrival_time as integer) % 100)) >
        ((cast(departure_time as integer) / 100) * 60 + (cast(departure_time as integer) % 100))
    then
        ((cast(arrival_time as integer) / 100) * 60 + (cast(arrival_time as integer) % 100))
        -
        ((cast(departure_time as integer) / 100) * 60 + (cast(departure_time as integer) % 100))
    else
    (
        ((cast(arrival_time as integer) / 100) * 60 + (cast(arrival_time as integer) % 100)) + 
        (24 * 60)  -- Add 24 hours in minutes if arrival is on the next day
        -
        ((cast(departure_time as integer) / 100) * 60 + (cast(departure_time as integer) % 100))
    )
    end as flight_duration_minutes

from enriched
