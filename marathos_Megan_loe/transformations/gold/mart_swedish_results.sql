USE CATALOG marathos_list;
USE SCHEMA gold;

CREATE OR REFRESH MATERIALIZED VIEW marathos_list.gold.mart_swedish_results
    COMMENT "serving view of swedish athletes results" AS
    SELECT
        e.event_id,
        e.event_number_of_finishers,
        e.event_date,
        a.athlete_id,
        a.athlete_performance,
        a.athlete_average_speed
    FROM fct_results fr
    LEFT JOIN dim_athlete a ON fr.athlete_id = a.athlete_id
    LEFT JOIN dim_event e ON fr.event_id = e.event_id
    WHERE a.athlete_country = 'SWE'