# Databricks notebook source
inputpath="dbfs:/mnt/asadlsad/processeddata/inputstream/json/"
outputpath="dbfs:/mnt/asadlsad/processeddata/outputautoloaderjson"

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop table stream.autojson

# COMMAND ----------

(spark.readStream
.format("cloudFiles")
.option("cloudFiles.format","json")
.option("cloudFiles.schemaLocation",f"{outputpath}/kushvanth/schemalocation")
.option("cloudFiles.inferColumnTypes",True)
.option("cloudFiles.schemaEvolutionMode","rescue")
.load(f"{inputpath}")
.writeStream
.option("checkpointLocation",f"{outputpath}/kushvanth/checkpoint")
.option("path",f"{outputpath}/kushvanth/files")
.option("mergeSchema",True)
.table("stream.autojson")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from stream.autojson

# COMMAND ----------


