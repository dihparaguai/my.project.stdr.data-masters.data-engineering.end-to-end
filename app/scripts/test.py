from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("TestCluster") \
    .getOrCreate()

df = spark.range(0, 10)
df.show()

spark.stop()
