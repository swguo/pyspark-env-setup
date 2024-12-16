
from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.sql import SparkSession

def main():

	# 初始化 Spark Session
	spark = SparkSession.builder \
	    .appName("Iris Decision Tree Classification") \
	    .getOrCreate()
	
	model_path = './model'
	# 載入模型
	loaded_model = DecisionTreeClassificationModel.load(model_path)
	print("Model successfully loaded.")

	# 重新讀取數據集
	train_df = spark.read.parquet("data/train_data.parquet")
	test_df = spark.read.parquet("data/test_data.parquet")

	# 預測
	predictions = loaded_model.transform(test_df)

	# 查看預測結果
	predictions.select("features", "label", "prediction").show()
	predictions.select("label", "prediction").write.csv("iris_predictions.csv", header=True)

if __name__ == '__main__':
	main()