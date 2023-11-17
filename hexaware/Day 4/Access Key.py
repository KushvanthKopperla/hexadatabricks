# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://raw@bolbhexaware.blob.core.windows.net",
  mount_point = "/mnt/bolbhexaware/raw",
  extra_configs = {"fs.azure.account.key.bolbhexaware.blob.core.windows.net":"v36Q4L+X+VFTBekfiKxPYIV8uSOcg6ynXTpED3VPmGQtMemr2Y3m3PgMNlkWd/SHNxQRkanTVUaX+AStXJuuqw=="})

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://testblobcontainer@blobadhex.blob.core.windows.net",
  mount_point = "/mnt/blobadhex/testblobcontainer",
  extra_configs = {"fs.azure.account.key.blobadhex.blob.core.windows.net":"q5I8uK1/Z4PL9+1OsIPWik5gHWWliO8M4RO7iVIYcf2uE+sJCXKTNd5tdcPa/U99JDmpkT7Zbphl+AStgc+3LQ=="})

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/blobadhex/testblobcontainer/raw/

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Mounting Akhil's Adls

# COMMAND ----------


dbutils.fs.mount(
  source = "wasbs://processeddata@asadlsad.blob.core.windows.net",
  mount_point = "/mnt/asadlsad/processeddata",
  extra_configs = {"fs.azure.account.key.asadlsad.blob.core.windows.net":"CgjjI6wlHTDiuYdRjWwkN0akzNZMWLd5H1dfezAgt9/1QxEsBftLQvagg5iz3uh5+LkRQctEgYQK+ASt+jU+rA=="})

# COMMAND ----------

outputpath= "dbfs:/mnt/asadlsad/processeddata/iotdata/"

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## F String

# COMMAND ----------


