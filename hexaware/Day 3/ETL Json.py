# Databricks notebook source
# MAGIC %md
# MAGIC Read Json file

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df= spark.read.json("dbfs:/FileStore/tables/formula1/constructors.json")
display(df)

# COMMAND ----------

# MAGIC %md 
# MAGIC ##Step2: Transformations
# MAGIC ###1.new column as ingestion date
# MAGIC ###2.new column file path
# MAGIC ###3.drop url column

# COMMAND ----------

df_final=df.withColumn("New Column",current_date()).withColumn("filepath",input_file_name()).drop("url")
df_final.display()

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

df.withColumn("filepath", F.input_file_name()).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Step3: save it as table

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table formula1.constructors

# COMMAND ----------

from pyspark.sql.functions import *
df=spark.read.json("dbfs:/FileStore/tables/formula1/constructors.json")
df_final=(df.withColumn("ingestiondate",current_date())
.withColumn("path",input_file_name())
.drop("url"))
df_final.write.saveAsTable("formula1.constructors")

# COMMAND ----------


