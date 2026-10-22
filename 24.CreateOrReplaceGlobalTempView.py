# Databricks notebook source
data = [
    (1, "Arjun", "Male", 'IT'),
    (2, "Priya", "Female", "HR"),
    (3, "Rahul", "Male", "Finance"),
    (4, "Sneha", "Female", "Marketing"),
    (5, "Vikram", 'Male', "Sales")
]
schema =['id','name','gender','dep']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

df.createOrReplaceTempView("Emp")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp;

# COMMAND ----------

df.createOrReplaceGlobalTempView("empGlobal")


# COMMAND ----------

# MAGIC %sql
# MAGIC show databases;