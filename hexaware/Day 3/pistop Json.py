# Databricks notebook source
df=spark.read.option("multiline","true").json("dbfs:/FileStore/tables/formula1/pit_stops.json")
display(df)


# COMMAND ----------

df.write.saveAsTable("formula1.pit_stops")

# COMMAND ----------


