# Databricks notebook source
# MAGIC %fs ls dbfs:/FileStore/tables/formula1/
# MAGIC

# COMMAND ----------

df=spark.read.option("header",True).option("inferschema",True).csv("dbfs:/FileStore/tables/formula1/circuits.csv")

# COMMAND ----------

display(df)
df.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema formula1;
# MAGIC use formula1;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop table formula1.Circuit

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("formula1.Circuit")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from formula1.Circuit

# COMMAND ----------

spark.sql("select * from formula1.circuit where location='Melbourne'").display()

# COMMAND ----------


