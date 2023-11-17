# Databricks notebook source
inputpath="dbfs:/mnt/asadlsad/processeddata/inputstream/csv/"
outputpath="dbfs:/mnt/asadlsad/processeddata/outputautoloader"

# COMMAND ----------

(spark.readStream
.format("cloudFiles")
.option("cloudFiles.format","csv")
.option("cloudFiles.schemaLocation",f"{outputpath}/kushvanth/schemalocation")
.load(f"{inputpath}")
.writeStream
.option("checkpointLocation",f"{outputpath}/kushvanth/checkpoint")
.option("path",f"{outputpath}/kushvanth/files")
.table("stream.firstauto")
)

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop table stream.firstauto

# COMMAND ----------

(spark.readStream
.format("cloudFiles")
.option("cloudFiles.format","csv")
.option("cloudFiles.schemaLocation",f"{outputpath}/kushvanth/schemalocation")
.option("cloudFiles.inferColumnTypes",True)
.load(f"{inputpath}")
.writeStream
.option("checkpointLocation",f"{outputpath}/kushvanth/checkpoint")
.option("path",f"{outputpath}/kushvanth/files")
.option("mergeSchema",True)
.table("stream.firstauto")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from stream.firstauto

# COMMAND ----------

(spark.readStream
.format("cloudFiles")
.option("cloudFiles.format","csv")
.option("cloudFiles.schemaLocation",f"{outputpath}/kushvanth/schemalocation")
.option("cloudFiles.inferColumnTypes",True)
.option("schemaEvolutionMode","resuce")
.load(f"{inputpath}")
.writeStream
.option("checkpointLocation",f"{outputpath}/kushvanth/checkpoint")
.option("path",f"{outputpath}/kushvanth/files")
.option("mergeSchema",True)
.table("stream.firstauto")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from stream.firstauto

# COMMAND ----------


