# Databricks notebook source
# MAGIC %fs ls dbfs:/mnt/asadlsad/processeddata/

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.<storageaccountname>.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.<storageaccountname>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.<storageaccountname>.dfs.core.windows.net", "SAS Token")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.adlshexaware.dfs.core.windows.net", "sp=rl&st=2023-11-10T06:07:50Z&se=2023-11-10T14:07:50Z&spr=https&sv=2022-11-02&sr=c&sig=JpUw6lzNecBxxziCHEVpMT3U7RqGXSw%2BP%2FFlTOSMWks%3D")


# COMMAND ----------

dbutils.fs.ls("abfss://processed@adlshexaware.dfs.core.windows.net")

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/

# COMMAND ----------

dbutils.fs.unmount("/mnt/asadlsad/processesddata")

# COMMAND ----------


