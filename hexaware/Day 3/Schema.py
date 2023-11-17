# Databricks notebook source
# MAGIC %fs ls
# MAGIC

# COMMAND ----------

df=spark.read.option("header",True).option("Inferschema",True).csv("dbfs:/databricks-datasets/asa/airlines/")

# COMMAND ----------

display(df)

# COMMAND ----------


