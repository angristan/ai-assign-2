from pyspark.sql import SparkSession

# Init Spark
spark = SparkSession.builder.getOrCreate()

sc = spark.sparkContext

# Load and transform JSON into Spark dataframe
path = "./data-300k.json"
spark_df = spark.read.json(path)

# Convert Spark dataframe to Pandas dataframe
pandas_df = spark_df.toPandas()

# Get every unique UUID
uuids = pandas_df.drop_duplicates('uuid', keep='last')['uuid']

# For each UUID, dump all related data to pickle file
for uuid in uuids.tolist():
    # Get all rows with this UUID
    uuid_df = pandas_df.loc[pandas_df.uuid == uuid]
    # Dump datafram object to pickle file
    uuid_df.to_pickle("./data/" + uuid + ".pickle")
