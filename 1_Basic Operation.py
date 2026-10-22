# Databricks notebook source
df = spark.table("workspace.default.movies")
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.count()

# COMMAND ----------

# DBTITLE 1,Cell 4
df.columns

# COMMAND ----------

display(df.describe())

# COMMAND ----------

display(df.summary())

# COMMAND ----------

# MAGIC %md
# MAGIC ###Column Filtering

# COMMAND ----------

df_trimmed = df.select("title", "imdb_rating", "industry")
df_trimmed.show(truncate = False)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Row Filtering

# COMMAND ----------

df_filtered = df.filter((df.release_year >= 2000) & (df.release_year <= 2010))
display(df_filtered)

# COMMAND ----------

from pyspark.sql.functions import col
df_filter = df.filter(col("release_year" ).between(2000, 2010))
display(df_filter)

# COMMAND ----------

df_filter1 = df.filter(col("studio") == "Marvel Studios")
display(df_filter1)

# COMMAND ----------

unique_df= df.select("industry").distinct()
display(unique_df)

# COMMAND ----------

unique_df= df.select("language").distinct()
display(unique_df)

# COMMAND ----------

df_profit = df.withColumn("Profit", col("revenue") - col("budget"))
display(df_profit)

# COMMAND ----------

df = df.withColumnRenamed("revenue", "Total_Revenue")
df.printSchema()

# COMMAND ----------

