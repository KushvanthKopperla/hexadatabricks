# Databricks notebook source
# MAGIC %md
# MAGIC #Applications
# MAGIC ##Transfomation and Action

# COMMAND ----------

df =Spark.raed.csv("path")

df1=df1.filter("condition")



# COMMAND ----------

df=spark.read.option("header",True).option("inferschema",True).csv("dbfs:/FileStore/tables/formula1/circuits.csv")
df.display()

# COMMAND ----------

df1=df.select(df.circuitId,df.circuitRef,df.name)
df1.display()

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df.select(col("circuitId").alias("circuit_id")).display()

# COMMAND ----------

df.count()

# COMMAND ----------

df.select(concat("location","country").alias("new column")).display()

# COMMAND ----------

df.select("*", concat("location",lit(" "),"country").alias("new column")).display()

# COMMAND ----------

df.withColumnRenamed("circuitId","circuit_id").display()

# COMMAND ----------

df.withColumnRenamed("circuitId","circuit_id").withColumnRenamed("circuitRef","circuit_Ref").display()

# COMMAND ----------

df.columns

# COMMAND ----------

new_columns=['circuit_id',
 'circuit_ref',
 'Name',
 'Location',
 'Country',
 'Lat',
 'Lng',
 'Alt',
 'Url']

# COMMAND ----------

df1=df.toDF(*new_columns)
display(df1)

# COMMAND ----------

df.withColumn("formula1",lit("Fromula1Data")).display()

# COMMAND ----------

df.withColumn("name",lit("Formula1Data")).display()

# COMMAND ----------

df.withColumn("New_column",current_date()).display()

# COMMAND ----------

df.withColumn("New_column",current_timestamp()).display()

# COMMAND ----------

# MAGIC %md
# MAGIC Filter or where
# MAGIC

# COMMAND ----------

df.filter("circuitId=1").display()

# COMMAND ----------

df.where("circuitId=1").display()

# COMMAND ----------

df.filter(col("circuitId")==1).display()

# COMMAND ----------

df.filter("circuitId > 10 and country = 'UK'").display()

# COMMAND ----------

df.filter((col("circuitID") > 10) & (col("country") =='UK')).display()

# COMMAND ----------

df.sort("circuitId",ascending=False).display()

# COMMAND ----------

df.orderBy(col("circuitId").desc()).display()

# COMMAND ----------

df.orderBy(desc("circuitId")).display()

# COMMAND ----------

df.sort("country","location").select("country","location").display()

# COMMAND ----------

df.drop("url","alt").display()

# COMMAND ----------

df
