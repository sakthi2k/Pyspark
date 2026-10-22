# Databricks notebook source
data = [
    (1,"Alice", "Electronics", 1200, "Jan"),
    (2,"Bob", "Electronics", 800, "Jan"),
    (3,"Alice", "Electronics", 1500, "Feb"),
    (4,"Bob", "Electronics", 1000, "Feb"),
    (5,"Charlie", "Clothing", 600, "Jan"),
    (6,"Charlie", "Clothing", 700, "Feb"),
    (7,"David", "Clothing", 400, "Jan"),
    (8,"Eva", "Groceries", 300, "Jan"),
    (9,"Eva", "Groceries", 500, "Feb"),
    (10,"Frank", "Groceries", 700, "Feb"),
    (11,"Frank", "Groceries", 650, "Jan"),
]
columns = ["id","employee_name", "department", "sales_amount", "month"]
df= spark.createDataFrame(data, columns)
df.show()

# COMMAND ----------

help(df.select)

# COMMAND ----------

#Select all columns
df.select("*").show() 
#Another way to select all columns
df.select([col for col in df.columns]).show()

# COMMAND ----------

df.select('id','employee_name').show()

# COMMAND ----------

df.select(df.id,df.department).show()

# COMMAND ----------

df.select(df['id'],df['department']).show()

# COMMAND ----------

from pyspark.sql.functions import col
df.select(col('id').alias('ID Number'),col('department').alias("Department_name")).show()

# COMMAND ----------

df.select(['id','department','employee_name']).show()

# COMMAND ----------

