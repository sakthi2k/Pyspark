# Databricks notebook source
df = spark.table("workspace.default.movies")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct studio from workspace.default.movies;

# COMMAND ----------

re_by_key=df.repartition(6,"studio")
re_by_key.explain("formatted")

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume workspace.default.partition_demo;

# COMMAND ----------

out_path ="/Volumes/workspace/default/partition_demo/repartition_6"
re_by_key.write.mode("overwrite").parquet(out_path)

# COMMAND ----------

df_par = spark.read.parquet("/Volumes/workspace/default/partition_demo/repartition_6")
display(df_par)

# COMMAND ----------

