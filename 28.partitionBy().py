# Databricks notebook source
data = [
    (1, "Arjun", "Male", 'IT'),
    (2, "Priya", "Female", "HR"),
    (3, "Rahul", "Male", "Finance"),
    (4, "Sneha", "Female", "Marketing"),
    (5, "Vikram", 'Male', "Sales")
    ]
schema =['id','name','gender','dep']
df= spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

# DBTITLE 1,Write DataFrame with partitionBy
# Update the path to a Unity Catalog volume. Replace <catalog>, <schema>, <volume> with your actual values.
df.write.parquet('your_loc/path', mode='overwrite', partitionBy='dep')
spark.read.parquet('your_loc/path').show()


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases;
# MAGIC use default;

# COMMAND ----------

# MAGIC %sql
# MAGIC desc emp;

# COMMAND ----------

# MAGIC %sql
# MAGIC desc detail emp;

# COMMAND ----------

location = spark.sql("DESCRIBE DETAIL emp").collect()[0]['location']
print(location)