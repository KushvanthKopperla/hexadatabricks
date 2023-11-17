# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/tables/
# MAGIC

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/tables/hexaraw")

# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/tables/hexaraw",True)

# COMMAND ----------


