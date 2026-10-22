# Databricks notebook source

data = [
    (1, "Arjun", "Male", "IT"),
    (2, "Priya", "Female", "HR"),
    (3, "Rahul", "Male", "Finance"),
    (4, "Sneha", "Female", "Marketing"),
    (5, "Vikram", "Male", "Sales"),
    (6, "Anita", "Female", "IT"),
    (7, "Karthik", "Male", "Operations"),
    (8, "Meera", "Female", "Finance"),
    (9, "Suresh", "Male", "HR"),
    (10, "Neha", "Female", "Marketing")
]
schema =['id','name','gender','dep']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

df.groupBy('dep','gender').count().show()

# COMMAND ----------

dis=df.groupBy('dep').pivot('gender').count()
display(dis)

# COMMAND ----------

print("Print only Male so inside the list")
df1=df.groupBy('dep').pivot('gender',['Male']).count()
display(df1)

# COMMAND ----------

