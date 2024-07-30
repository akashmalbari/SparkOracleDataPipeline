from pyspark.sql import SparkSession
import os

# Set the path for the Oracle JDBC driver
os.environ['SPARK_CLASSPATH'] = '/path/to/ojdbc8.jar'

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV to Oracle") \
    .config("spark.jars", "/path/to/ojdbc8.jar") \
    .getOrCreate()

# Define the path to your CSV file
csv_file_path = "../data/sample_data.csv"

# Load CSV file into a DataFrame
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Define Oracle connection properties
oracle_url = "jdbc:oracle:thin:@hostname:port/service_name"
oracle_properties = {
    "user": "your_username",
    "password": "your_password",
    "driver": "oracle.jdbc.driver.OracleDriver"
}

# Define the target table name
target_table = "sample_table"

# Write DataFrame to Oracle table
df.write.jdbc(url=oracle_url, table=target_table, mode="append", properties=oracle_properties)

# Stop the Spark session
spark.stop()
