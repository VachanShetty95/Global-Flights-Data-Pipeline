-- models/flights_enriched.sql

with flights as (
    select *
    from {{ ref('flights_cleaned') }}
),
airlines as (
    select
        "IATA_CODE" as airline_code,
        "AIRLINE" as airline_name
    from public.airlines
)

select
    f.*,
    a.airline_name,
    a.airline_code
from flights f
left join airlines a on f.airline = a.airline_code
