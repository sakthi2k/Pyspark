# Databricks notebook source
# DBTITLE 1,Map_Type
from pyspark.sql.types import StructType, StructField, StringType, MapType
data = [('Sakthi',{'Hair':'Black', 'Eye':'Brown'}),
        ('Saravanan',{'Hair':'Black', 'Eye':'Blue'})]
schema =StructType([
        StructField('Name',StringType()),\
        StructField('Properties',MapType(StringType(), StringType()))  #MapType(key<DataType>, value<DataType>)
                    ]) 

df = spark.createDataFrame(data,schema)
display(df)


# COMMAND ----------

# DBTITLE 1,Accessing Map Element
print('Accessing using Data Frame')
df1 = df.withColumn('Hair',df.Properties['Hair'])
df1.show(truncate=False)
print('accessing the element using getItem')
df2 = df.withColumn('Eye',df.Properties.getItem('Eye'))
display(df2)

# COMMAND ----------

# DBTITLE 1,explode_function to get Key and Value
from pyspark.sql.functions import explode
df1 = df.select("Name","Properties", explode(df.Properties))
display(df1)

# COMMAND ----------

# DBTITLE 1,Getting key only using map_keys
from pyspark.sql.functions import map_keys
df1 = df.withColumn("Keys", map_keys(df.Properties))
df1.show(truncate= False)

# COMMAND ----------

# DBTITLE 1,Getting Values only using map_values
from pyspark.sql.functions import map_values
df1 = df.withColumn("Values", map_values(df.Properties))
df1.show(truncate= False)

# COMMAND ----------

