from pyspark import pipelines as dp
from utils.utils import rename_columns_to_snake_case
from pyspark.sql.functions import col, regexp_replace, split, round as sparkround, sum as spark_sum, dense_rank
from pyspark.sql.window import Window

@dp.materialized_view(name="marathos_list.silver.marathon_mv", 
          comment="clean marathon data",
          table_properties={
              "delta.columnMapping.mode":"name",
              "delta.minReaderVersion":"2",
              "delta.minWriterVersion":"5"})

def cleaned_marathos_data():
    df = rename_columns_to_snake_case(spark.sql("""SELECT * FROM marathos_list.bronze.raw_marathos_list"""))

    df_time = df.filter(col("athlete_performance").contains("h") & (~df["athlete_performance"].contains("d")))


    df_with_decimal_hours = df_time.withColumn(
    "athlete_performance",
    split(regexp_replace(col("athlete_performance"), " h$", ""), ":")
    ).withColumn(
    "athlete_performance",
    sparkround(col("athlete_performance")[0].cast("double") + 
    col("athlete_performance")[1].cast("double") / 60 + 
    col("athlete_performance")[2].cast("double") / 3600, 2)
    )

    df_clean = df_with_decimal_hours.dropna(subset=[
        "athlete_club",
        "athlete_country",
        "athlete_year_of_birth",
        "athlete_gender",
        "athlete_age_category",
        "athlete_average_speed"
    ])
    window_spec = Window.orderBy("event_name")

    df_speed = df_clean.withColumn("athlete_average_speed", col("athlete_average_speed").cast("double"))
    
    df_final = df_speed.withColumn("event_id", dense_rank().over(window_spec))

    return df_final
