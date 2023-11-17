-- Databricks notebook source
-- MAGIC %sql
-- MAGIC CREATE TABLE IF NOT EXISTS delta.people20m (
-- MAGIC   id INT,
-- MAGIC   firstName STRING,
-- MAGIC   middleName STRING,
-- MAGIC   lastName STRING,
-- MAGIC   gender STRING,
-- MAGIC   birthDate TIMESTAMP,
-- MAGIC   ssn STRING,
-- MAGIC   salary INT
-- MAGIC ) LOCATION 'dbfs:/mnt/adlshexaware/processed/iot_data/'

-- COMMAND ----------


insert into delta.people20m values(1,'Virat','R','K','M',2023-11-14,"123",1500)

-- COMMAND ----------



-- COMMAND ----------

describe history delta.people20m

-- COMMAND ----------

select * from delta.people20m version as of 1

-- COMMAND ----------

df.witCoulmn
