# Databricks notebook source
# MAGIC %fs ls dbfs:/mnt/asadlsad/processeddata/raw/

# COMMAND ----------

df = spark.read.option("header",True).option("inferschema",True).csv("dbfs:/mnt/asadlsad/processeddata/raw/Baby_Names.csv")

# COMMAND ----------

df.count()

# COMMAND ----------

display(df)

# COMMAND ----------

df.groupBy("year").count().show()

# COMMAND ----------


