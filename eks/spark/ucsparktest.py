from pyspark.sql import SparkSession

catalog_name = "demo1" 
schema_name = "myschema"
table_name = "dgaTable1"
new_tablename = f"{catalog_name}.{schema_name}.{table_name}"

if __name__ == "__main__":
    spark = (
        SparkSession.builder
        # .appName("jupyter-uc-dag-test")
        # .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,io.delta:delta-spark_2.12:3.2.1,io.unitycatalog:unitycatalog-spark_2.12:0.2.0") \
        .config("spark.hadoop.fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "io.unitycatalog.spark.UCSingleCatalog")
        .config(f"spark.sql.catalog.{catalog_name}", "io.unitycatalog.spark.UCSingleCatalog")
        .config(f"spark.sql.catalog.{catalog_name}.uri", "http://unity-catalog-service:8080") \
        .config(f"spark.sql.catalog.{catalog_name}.warehouse", catalog_name)
        .config("spark.sql.defaultCatalog", catalog_name)
        .config("spark.databricks.delta.catalog.update.enabled","true")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider","com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
        .getOrCreate()
    )
   
    spark.sql(f"""
    CREATE TABLE {new_tablename} (id INT, desc STRING)
    USING delta
    LOCATION 's3://data-analystic/{catalog_name}/{schema_name}/{table_name}'
    """)

    for i in range(100):        
        spark.sql(f"""INSERT INTO {new_tablename} VALUES ({i}, "test {i}")""")
    
    spark.stop()

