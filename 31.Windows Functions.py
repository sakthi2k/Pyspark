# Databricks notebook source
from pyspark.sql.functions import row_number, rank, dense_rank, col
from pyspark.sql.window  import Window
data = [
("A", "X", 1, "2023-01-01"),
("A", "X", 2, "2023-01-02"),
("A", "Y", 3, "2023-01-01"),
("A", "Y", 3, "2023-01-02"),
("B", "X", 5, "2023-01-01"),
("B", "X", 4, "2023-01-02"),
]
columns = ["category", "sub_category", "value", "timestamp"]
df = spark.createDataFrame(data, columns)
df.show()

# COMMAND ----------

# DBTITLE 1,Row_Number
window=Window.partitionBy('category','sub_category').orderBy(col('timestamp'),col('value'))
Row_Ex=df.withColumn('Row_Number', row_number().over(window))
display(Row_Ex)

# COMMAND ----------

# DBTITLE 1,Rank
Rank_Ex=df.withColumn('Rank', rank().over(window))
display(Rank_Ex)

# COMMAND ----------

# DBTITLE 1,Dense_Rank
Dense_Rank_Ex=df.withColumn('Rank', dense_rank().over(window))
display(Dense_Rank_Ex)

# COMMAND ----------

# DBTITLE 1,LAG
from pyspark.sql.functions import lag
Lag_Ex=df.withColumn('Previous_Value', lag('value').over(window))
display(Lag_Ex)

# COMMAND ----------

# DBTITLE 1,Lead
from pyspark.sql.functions import lead
Lead_Ex=df.withColumn('Next_Value', lead('value').over(window))
display(Lead_Ex)