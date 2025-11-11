from pyspark.sql import SparkSession

def create_and_show_spark_df(): # Function to test Spark creation inside and outside Docker
    spark = (
        SparkSession.builder
        # .master("spark://localhost:7077")           # Use localhost for local testing
        # .master("spark://spark-master:7077")        # Use spark-master for Docker testing
        .appName("TestSparkApp")
        .getOrCreate()
    )
    
    data = [("diego", 28), ("rodrigo", 27)]
    columns = ["nome", "idade"]
    
    df = spark.createDataFrame(data, columns)
    
    df.show()
    
    spark.stop()


if __name__ == "__main__":
    create_and_show_spark_df()