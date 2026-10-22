# Databricks notebook source
data = [
    (1, "Arjun", "Male", None),
    (2, "Priya", "Female", "HR"),
    (3, "Rahul", "Male", "Finance"),
    (4, "Sneha", "Female", "Marketing"),
    (5, "Vikram", None, "Sales")
]
schema =['id','name','gender','dep']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

# DBTITLE 1,Collect Function
listRows=df.collect()
print(listRows)
print(listRows[2])
print(listRows[2][3])