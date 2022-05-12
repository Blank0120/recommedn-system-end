from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"
os.environ["SPARK_HOME"] = "F:/Python/pythonC38/Lib/site-packages/pyspark"
os.environ["PYSPARK_PYTHON"] = "F:/Python/pythonC38/python"
import pyspark.pandas as ps
ps.set_option('compute.ops_on_diff_frames', True)

spark = SparkSession.builder.config("spark.executor.processTreeMetrics", False).getOrCreate()
data_path = os.path.join("datasets","BX-CSV-Dump")

# 读取处理过的books.csv为dataframe
books_path = os.path.join(data_path, "BX-Books.csv")
books_df = spark.read.csv(books_path, "ISBN string, BookTitle string, BookAuthor string, YearOfPublication int, Publisher string, ImageURLS string, ImageURLM string, ImageURLL string", header=True)
books_df.cache()
# print(books_df.is_cached)
# books_df.show()

# 读取处理过的book-ratings.csv为dataframe
ratings_path = os.path.join(data_path,"BX-Book-Ratings.csv")
ratings_df = spark.read.csv(ratings_path, 'uid int, ISBN int, rank float', header=True)
# ratings_df.cache()
# print(ratings_df.is_cached)
# ratings_df.show()

# 加载或训练模型
model = None
model_path = os.path.join("models", "book_als")
if not os.path.exists("models"):
    print("the model is forming")
    als = ALS(maxIter=10, rank=16, regParam=0.1, seed=5, userCol='uid', itemCol='ISBN', ratingCol='rank')
    pipeline = Pipeline(stages=[als])
    model = pipeline.fit(ratings_df)
    model.save(model_path)
else:
    print("the model is loading from file.......")
    model = PipelineModel.load(model_path)


def get_top_ratings(uid):
    print("get_top_ratings......")
    unrated_books_df = ratings_df.drop("rank").filter("uid != " + str(uid))
    user_unrated_books_df = unrated_books_df.withColumn("uid", unrated_books_df.uid - unrated_books_df.uid + uid).distinct()
    # user_unrated_books_df.show()

    predict_rank = model.transform(user_unrated_books_df)
    predict_result = predict_rank.drop(predict_rank.uid).orderBy(desc("prediction")).filter("prediction > 3")
    recommend_book = predict_result.join(books_df, books_df.ISBN == predict_rank.ISBN, "inner").drop(predict_rank.ISBN)
    return recommend_book.limit(20).toJSON().collect()

# get_top_ratings(11676)


