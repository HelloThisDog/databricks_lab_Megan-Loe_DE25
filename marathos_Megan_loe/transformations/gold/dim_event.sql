CREATE OR REFRESH MATERIALIZED VIEW marathos_list.gold.dim_event
    COMMENT "dimensional table for events"
    SELECT
        event_id,
        MAX_BY(event_name, event_dates) AS event_name,
        MAX_BY(event_dates, event_dates) AS event_date,
        MAX_BY(event_distance, event_dates) AS event_distance,
        MAX_BY(event_number_of_finishers, event_dates) AS event_number_of_finishers
    FROM
        marathos_list.silver.marathon_mv
    GROUP BY
        event_id;