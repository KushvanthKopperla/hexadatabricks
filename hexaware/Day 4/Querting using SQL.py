# Databricks notebook source
# MAGIC %fs ls dbfs:/mnt/asadlsad/processeddata/iotdata/kushvanth/

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from json.`dbfs:/mnt/blobadhex/testblobcontainer/raw/16.8.23.json`

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists iotdata;
# MAGIC use iotdata

# COMMAND ----------

# MAGIC %sql
# MAGIC create table iotdata.sample as
# MAGIC (select * from json.`dbfs:/mnt/blobadhex/testblobcontainer/raw/16.8.23.json`)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from parquet.`dbfs:/mnt/asadlsad/processeddata/iotdata/kushvanth/`

# COMMAND ----------


