# Databricks notebook source
df=spark.read.json("dbfs:/FileStore/tables/formula1/drivers.json")

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import *


# COMMAND ----------

df1=df.withColumn("forename",col("name.forename")).withColumn("surname",col("name.surname")).drop("url")

# COMMAND ----------

df1.write.saveAsTable("formula1.drivers")

# COMMAND ----------


