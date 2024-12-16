from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from sklearn.datasets import load_iris
import gradio as gr
import pandas as pd


def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    	
			
	input_data = pd.DataFrame({
	'sepal length (cm)': [sepal_length],
	'sepal width (cm)': [sepal_width],
	'petal length (cm)': [petal_length],
	'petal width (cm)': [petal_width],
	})
	
	spark = SparkSession.builder \
	    .appName("Iris Decision Tree Classification") \
	    .getOrCreate()

	iris = load_iris()
	
	label_mapping = {index: name for index, name in enumerate(iris.target_names)}

	feature_cols = iris.feature_names
	assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    
    
	input_sdf = spark.createDataFrame(input_data)
    
	input_features = assembler.transform(input_sdf)

	model_path = './model'

	loaded_model = DecisionTreeClassificationModel.load(model_path)
	print("Model successfully loaded.")    

	prediction = loaded_model.transform(input_features)
	predicted_label = prediction.collect()[0]['prediction']

	# 返回對應的標籤名稱
	return label_mapping[predicted_label]

def main():

	# 設定 Gradio 介面
	inputs = [
	    gr.Number(label="Sepal Length (cm)", value=5.1),  # 使用 gr.Number，`value` 表示預設值
	    gr.Number(label="Sepal Width (cm)", value=3.5),
	    gr.Number(label="Petal Length (cm)", value=1.4),
	    gr.Number(label="Petal Width (cm)", value=0.2),
	]

	outputs = gr.Textbox(label="Predicted Species")  # 使用 gr.Textbox 來顯示結果

	# 建立 Gradio Interface
	gr.Interface(
	    fn=predict_species,
	    inputs=inputs,
	    outputs=outputs,
	    title="Iris Species Predictor",
	    description="輸入花萼與花瓣的長度與寬度，預測 Iris 的種類（Setosa, Versicolor, Virginica）。"
	).launch(server_port=8088)

if __name__ == '__main__':
	main()