from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier
from sklearn.datasets import load_iris
import pandas as pd
from pyspark.sql import SparkSession


def main():

	# 初始化 Spark Session
	spark = SparkSession.builder \
	    .appName("Iris Decision Tree Classification") \
	    .getOrCreate()

	# 載入 Iris Dataset
	iris = load_iris()
	df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
	df['label'] = iris.target

	# 將 Pandas DataFrame 轉為 Spark DataFrame
	iris_df = spark.createDataFrame(df)
	iris_df.show(5)

	
	feature_cols = iris.feature_names
	assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
	iris_features_df = assembler.transform(iris_df)
	iris_features_df.show(5)

	# 資料分割：將數據集劃分為訓練集與測試集：
	train_df, test_df = iris_features_df.randomSplit([0.8, 0.2], seed=42)
	# 儲存數據集到 Parquet 格式
	train_df.write.mode("overwrite").parquet("data/train_data.parquet")
	test_df.write.mode("overwrite").parquet("data/test_data.parquet")
	print("Train and Test datasets saved as Parquet.")


	# 建立 Decision Tree 模型 & 訓練
	dt = DecisionTreeClassifier(featuresCol="features", labelCol="label", maxDepth=5)

	# 模型訓練
	dt_model = dt.fit(train_df)
	model_path = './model'
	dt_model.write().overwrite().save(model_path)
	print(f"Model saved to {model_path}")

if __name__ == '__main__':
	main()