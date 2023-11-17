# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df =spark.read.json("dbfs:/mnt/blobadhex/testblobcontainer/raw/16.8.23.json")

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 1: 

# COMMAND ----------

users_schema=StructType([StructField("sensor_id",StringType()),
                         StructField("temperature",FloatType()),
                         StructField("humidity",FloatType()),
                         StructField("pressure",FloatType()),
                         StructField("timestamp",StringType()),
                         StructField("test",IntegerType())
])
df = spark.read.schema(users_schema).json("dbfs:/mnt/blobadhex/testblobcontainer/raw/16.8.23.json")

# COMMAND ----------

df1 = df.withColumn("path",input_file_name()).drop("test")
df1.display()


# COMMAND ----------

outputpath= "dbfs:/mnt/asadlsad/processeddata/iotdata/"

# COMMAND ----------

df1.write.mode("overwrite").parquet(f"{outputpath}kushvanth")

# COMMAND ----------


