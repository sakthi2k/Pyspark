# Databricks notebook source
df=spark.range(2)
df.show()

# COMMAND ----------

# DBTITLE 1,Current Time Stamp
from pyspark.sql.functions import current_timestamp
df1=df.withColumn('currentTimeStamp',current_timestamp())
display(df1)
df1.printSchema()

# COMMAND ----------

# DBTITLE 1,To TimeStamp
from pyspark.sql.functions import lit,to_timestamp
df2 = df1.withColumn('timeStampString', lit('2026.02.14 08.12.33'))
display(df2)
display(df2.withColumn('timeStampString', to_timestamp(df2.timeStampString, 'yyyy.MM.dd HH.mm.ss')))

# COMMAND ----------

# DBTITLE 1,Hour minute
from pyspark.sql.functions import hour,minute, second
df1.select('*',hour(df1.currentTimeStamp).alias('hour'),\
    minute(df1.currentTimeStamp).alias('minute'),\
        second(df1.currentTimeStamp).alias('second')).show(truncate=False)