CREATE OR REFRESH MATERIALIZED VIEW marathos_list.gold.dim_athlete
    COMMENT "dimensional table for athlete"
    SELECT
        athlete_id,
        MAX_BY(athlete_performance, event_dates) AS athlete_performance,
        MAX_BY(athlete_club, event_dates) AS athlete_club,
        MAX_BY(athlete_country, event_dates) AS athlete_country,
        MAX_BY(athlete_year_of_birth, event_dates) AS athlete_birth_year,
        MAX_BY(athlete_gender, event_dates) AS athlete_gender,
        MAX_BY(athlete_age_category, event_dates) AS athlete_age_category,
        MAX_BY(athlete_average_speed, event_dates) AS athlete_average_speed
    FROM
        marathos_list.silver.marathon_mv
    GROUP BY
        athlete_id;