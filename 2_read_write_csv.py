# Databricks notebook source
df = spark.read.option("header", True)\
    .option("inferSchema", True)\
    .csv("/Volumes/workspace/default/raw_data/orders.csv")
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType, TimestampType

orders_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("customer_id", IntegerType(), True),
    StructField("order_date", TimestampType(), True),
    StructField("product_id", IntegerType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("status", StringType(), True)
])


# COMMAND ----------


df1 = spark.read.option("header", True)\
    .option("dateFormat", "yyyy-MM-dd")\
    .schema(orders_schema)\
    .csv("/Volumes/workspace/default/raw_data/orders.csv")
df.printSchema()

# COMMAND ----------

display(df1)

# COMMAND ----------

df.show()

# COMMAND ----------

df.write.mode("overwrite").parquet("/Volumes/workspace/default/raw_data/orders/")

# COMMAND ----------

df.write\
    .format("delta")\
        .mode("overwrite")\
    .saveAsTable("dev.bronze.order_sample")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC SELECT *, first(price) over(partition by country order by order_date asc rows between unbounded preceding and unbounded following ) as last_va
# MAGIC FROM dev.bronze.vw_order_sample 
# MAGIC