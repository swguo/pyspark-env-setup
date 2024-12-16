from pyspark.sql import SparkSession
from sklearn.metrics import confusion_matrix, classification_report
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def main():

	# 初始化 Spark Session
	spark = SparkSession.builder \
	    .appName("Iris Decision Tree Classification") \
	    .getOrCreate()
	

	predictions_df = spark.read.csv("iris_predictions.csv", header=True, inferSchema=True)

	# 查看預測結果
	predictions_df.show()

	# 評估模型
	evaluator = MulticlassClassificationEvaluator(
	    labelCol="label", 
	    predictionCol="prediction", 
	    metricName="accuracy"
	)
	accuracy = evaluator.evaluate(predictions_df)
	print(f"Test Accuracy: {accuracy}")

	# 獲取標籤與預測值
	labels = predictions_df.select("label").rdd.flatMap(lambda x: x).collect()
	predictions = predictions_df.select("prediction").rdd.flatMap(lambda x: x).collect()

	# 計算混淆矩陣
	conf_matrix = confusion_matrix(labels, predictions)

	# 打印混淆矩陣
	print("Confusion Matrix:")
	print(conf_matrix)

	# 打印分類報告
	print("\nClassification Report:")
	print(classification_report(labels, predictions, digits=4))

if __name__ == '__main__':
	main()