# Databricks notebook source
df=spark.range(start =1, end=101)
display(df)
df1=df.sample(fraction=0.1,seed=123)
df2=df.sample(fraction=0.1, seed=123)
display(df1)
display(df2)


# COMMAND ----------

