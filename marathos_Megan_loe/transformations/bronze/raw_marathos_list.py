from pyspark import pipelines as dp

BASE_DIR = "/Volumes/marathos_list/default/raw"

Schema = spark.read.format("csv").options(header=True, inferSchema=True).load(f"{BASE_DIR}/data/TWO_CENTURIES_OF_UM_RACES.csv").schema

@dp.table(name="marathos_list.bronze.raw_marathos_list", comment="Raw data of the marathos list", table_properties={
    "delta.columnMapping.mode": "name",
    "delta.minReaderversion": "2",
    "delta.minWriterversion": "5"
})

def raw_marathos_list():
    return spark.readStream.format("csv").options(header= True, encoding= "UTF-8").schema(Schema).load(f"{BASE_DIR}/data")