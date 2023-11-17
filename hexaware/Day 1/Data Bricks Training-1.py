# Databricks notebook source
# MAGIC %md
# MAGIC # Getting Started with Spark
# MAGIC ## Getting Started with Databricks
# MAGIC ### Azure Databricks
# MAGIC #### Lakehouse
# MAGIC ##### Delta lake

# COMMAND ----------

# MAGIC %scala
# MAGIC println("run Scala")

# COMMAND ----------

print('Hello world')

# COMMAND ----------

# MAGIC %sql
# MAGIC create database Hexaware

# COMMAND ----------

# MAGIC %sql
# MAGIC Create schema if not exists hexawaredev;
# MAGIC use hexawaredev

# COMMAND ----------

# MAGIC %sql
# MAGIC create table hexawaredev.sample(id int, name string, age int)

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into hexawaredev.sample values(2,'b',30)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from hexawaredev.sample

# COMMAND ----------

# MAGIC %sql
# MAGIC show schemas;
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail hexawaredev.sample

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended hexawaredev.sample

# COMMAND ----------


