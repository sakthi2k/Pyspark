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

print("which will replace all columns are unknow where ever find null")
df.fillna("Unknown").show()

# COMMAND ----------

print("which will replace only particular columns as unknow where ever find null")
df.fillna("Unknown",['gender','dep']).show()

# COMMAND ----------

print("which will replace all columns as unknow where ever find null")
df.na.fill("Unknown").show()

# COMMAND ----------

print("which will replace only particular columns as unknow where ever find null")
df.na.fill("Unknown",['gender']).show()