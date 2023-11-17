-- Databricks notebook source
-- MAGIC %sql
-- MAGIC create schema delta;
-- MAGIC use delta

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC CREATE TABLE IF NOT EXISTS delta.people10m ( 
-- MAGIC    id INT, 
-- MAGIC    firstName STRING,
-- MAGIC    middleName STRING,
-- MAGIC    lastName STRING,
-- MAGIC    gender STRING,
-- MAGIC    birthDate TIMESTAMP,
-- MAGIC    ssn STRING,
-- MAGIC    salary INT) USING DELTA

-- COMMAND ----------

select * from delta.people10m

-- COMMAND ----------

describe extended delta.people10m

-- COMMAND ----------

describe history delta.people10m

-- COMMAND ----------

-- MAGIC %fs ls dbfs:/mnt/adlshexaware/processed/iot_data/

-- COMMAND ----------

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


