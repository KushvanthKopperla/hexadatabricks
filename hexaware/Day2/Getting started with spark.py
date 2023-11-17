# Databricks notebook source
print("Hello world")

# COMMAND ----------

spark

# COMMAND ----------

# MAGIC %md
# MAGIC ##Spark(Spark Session) is an entry point to stat ypu driver program

# COMMAND ----------

users=[(1,'a',30),(2,'b',32)]

# COMMAND ----------

sampledf=spark.createDataFrame(users)

# COMMAND ----------

sampledf.show()

# COMMAND ----------

display(sampledf)

# COMMAND ----------

users_shema_str="id int,name string, age int"

# COMMAND ----------

df1=spark.createDataFrame(users,users_shema_str)
display(df1)

# COMMAND ----------


