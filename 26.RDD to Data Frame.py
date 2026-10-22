# Databricks notebook source
data=[(1,'Sakthi'),(2,'Wafa')]
rdd=spark.sparkContext.parallelize(data)
print(rdd.collect())

# COMMAND ----------

rdd.toDF()