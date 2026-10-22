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
df = spark.createDataFrame(data,columns)
df.show()

# COMMAND ----------

df.groupBy("department").count().show()

# COMMAND ----------

# DBTITLE 1,Min
df.groupBy("department").min('sales_amount').show()

# COMMAND ----------

# DBTITLE 1,Group by with Agg
from pyspark.sql.functions import count,min,max
df1= df.groupBy("department").agg(count('*').alias('Count of Employees'),
                                  min("sales_amount").alias('Min sales Amount'),
                                  max('sales_amount').alias('Max Sales Amount')
                                  ).show()

# COMMAND ----------

