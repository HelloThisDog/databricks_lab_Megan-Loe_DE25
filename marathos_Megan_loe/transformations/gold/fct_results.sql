
CREATE OR REFRESH MATERIALIZED VIEW marathos_list.gold.fct_results
    COMMENT "fact table for the gold layer" AS
    SELECT
        event_id,
        athlete_id,
        athlete_performance,
        athlete_average_speed,
        event_number_of_finishers
        event_dates
    FROM
        marathos_list.silver.marathon_mv
