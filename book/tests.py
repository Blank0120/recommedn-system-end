# from pyspark.ml import Pipeline, PipelineModel
# from pyspark.ml.evaluation import RegressionEvaluator
# from pyspark.ml.recommendation import ALS
# from pyspark.sql import SparkSession
# import os
# os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"
# os.environ["SPARK_HOME"] = "F:/Python/pythonC38/Lib/site-packages/pyspark"
# os.environ["PYSPARK_PYTHON"] = "F:/Python/pythonC38/python"
# import pyspark.pandas as ps
# ps.set_option('compute.ops_on_diff_frames', True)
#
# spark = SparkSession.builder.config("spark.executor.processTreeMetrics", False).getOrCreate()
# data_path = os.path.join("../datasets","BX-CSV-Dump")
#
# ratings_path = os.path.join(data_path,"BX-Book-Ratings.csv")
# ratings_df = spark.read.csv(ratings_path, 'uid int, ISBN int, rank float', header=True)
#
# als = ALS(maxIter=10, rank=35, regParam=0.005, seed=10, userCol='uid', itemCol='ISBN', ratingCol='rank').setColdStartStrategy("drop").setNonnegative(True)
#
# model = als.fit(ratings_df)
#
# # prediction = model.recommendForUserSubset(276726, 20)
# prediction = model.transform(ratings_df)
# prediction.show()
#
#
# evaluator = RegressionEvaluator().setMetricName("rmse").setLabelCol("rank").setPredictionCol("prediction")
#
# print(als.explainParam("maxIter"))
# print(als.explainParam("rank"))
# print(als.explainParam("regParam"))
# print("均方根误差为=>",evaluator.evaluate(prediction))
#
#
#
