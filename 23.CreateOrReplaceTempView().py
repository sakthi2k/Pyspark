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
display(df)

# COMMAND ----------

df.createOrReplaceTempView('employee')
df1= spark.sql('select upper(name),id from employee ')
df1.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employee where gender ='Male';
# MAGIC Select id, upper(name) as Name from employee ;