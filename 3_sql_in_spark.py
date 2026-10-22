# Databricks notebook source
df_marvel =spark.sql("select * from  workspace.default.movies where studio = 'Marvel Studios'")
display(df_marvel)

# COMMAND ----------

# MAGIC %md
# MAGIC ### SQL using %SQL
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from  workspace.default.movies where studio = 'Marvel Studios'

# COMMAND ----------

isNotNull()