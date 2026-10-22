# Databricks notebook source
# DBTITLE 1,Column Rename
#Modify the Column name in DataFrmae
data = [(1,'Sakthi',1000),(2,'Saravanan',2000),(3,'Kumar',3000)]
columns=['ID','Name','Salary']
#df=spark.createDataFrame(data = data, schema=columns)
df=spark.createDataFrame(data, columns)
df1=df.withColumnRenamed('Salary','Salary_Amount')
df1.show()
df1.printSchema()


# COMMAND ----------

# DBTITLE 1,WithColumn
 df2 = df.withColumn("Salary",df['Salary'].cast('int'))
 df2.printSchema()

# COMMAND ----------

# DBTITLE 1,StructType && StructField
from pyspark.sql.types import StructType,StructField,IntegerType,StringType

schema = StructType([StructField(name ='ID',dataType = IntegerType()),\
                     StructField(name ='Name', dataType=StringType()),\
                     StructField(name ='Salary_A', dataType =IntegerType())])
df=spark.createDataFrame(data,schema)
df.show()
df.printSchema()

# COMMAND ----------

# DBTITLE 1,Complex Column implementation
from pyspark.sql.types import StructType,StructField,IntegerType,StringType

data = [(1,('Sakthi','Saravanan'),1000),(2,('Saravanan','Kumar'),2000),(3,('Kumar','2kkid'),3000)]
complex_schema =StructType([\
                             StructField(name ='First_Name',dataType=StringType()),\
                             StructField(name ='Last_Name',dataType = StringType())])

schema = StructType([StructField(name ='ID',dataType = IntegerType()),
                     StructField(name ='Name', dataType=complex_schema),
                     StructField(name ='Salary_A', dataType =IntegerType())
                    ])
df=spark.createDataFrame(data,schema)
df.show()
df.printSchema()

# COMMAND ----------

# DBTITLE 1,Array_Type
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,ArrayType
data = [('abc',[1,2]),
        ('mno',[3,4]),
        ('pqr',[5,6]),
        ('xyz',[7,8])]
schema = StructType([
                    StructField('ID',StringType()),
                    StructField('Number',ArrayType(IntegerType()))
                    ])
df =spark.createDataFrame(data,schema)
df.show()
#Accessing the Array Element
df.withColumn('First_Number_InArray',df.Number[0]).show()

# COMMAND ----------

from pyspark.sql.functions import col,array
data =[(1,2),(3,4)]
schema =('num1','num2')
df=spark.createDataFrame(data,schema)
df1 = df.withColumn('arrayOfNums',array(col('num1'),col('num2')))
display(df1)
df1.withColumn('FirstNum',df1.arrayOfNums[0]).show()





# COMMAND ----------

