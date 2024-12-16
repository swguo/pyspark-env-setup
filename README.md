以下是基於你的腳本撰寫的 GitHub Markdown 文件，包含介紹、逐步說明及相關命令的詳細說明：

---

# 配置 PySpark 執行環境：Ubuntu 教程

本教程詳細介紹如何在 Ubuntu 系統上配置一個獨立的 **PySpark** 開發環境，適合進行數據處理、機器學習以及部署應用。

## **目錄**
- [簡介](#簡介)
- [前置需求](#前置需求)
- [步驟詳解](#步驟詳解)
  - [1. 更新系統並安裝 Python](#1-更新系統並安裝-python)
  - [2. 安裝虛擬環境](#2-安裝虛擬環境)
  - [3. 創建並啟動虛擬環境](#3-創建並啟動虛擬環境)
  - [4. 安裝相關依賴](#4-安裝相關依賴)
  - [5. 執行 Python 腳本](#5-執行-python-腳本)
- [結論](#結論)

---

## **簡介**
PySpark 是基於 Apache Spark 的 Python API，廣泛應用於大規模數據處理與分佈式計算。本教程將幫助你從零開始配置一個獨立的 PySpark 開發環境，並支持與常見數據科學工具（如 Pandas、Scikit-learn 和 Gradio）一起使用。

---

## **前置需求**
- 一台可執行 Ubuntu 的機器（推薦版本：20.04 或更新）。
- Python 版本至少為 3.6。
- 能夠連上網路下載必要的函式庫。

---

## **步驟詳解**

### **1. 更新系統並安裝 Python**
首先，確保你的系統是最新的，並安裝所需的 Python 版本。
```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```

### **2. 安裝虛擬環境**
使用 `virtualenv` 創建一個隔離的 Python 執行環境，便於管理 PySpark：
```bash
pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple
```
這裡使用清華大學的 Python 來源以加速下載。

### **3. 創建並啟動虛擬環境**
1. 創建一個名為 `spark` 的虛擬環境，並指定 Python 版本：
   ```bash
   python3 -m virtualenv spark --python=python3.10
   ```
2. 啟動虛擬環境：
   ```bash
   source spark/bin/activate
   ```

### **4. 安裝相關依賴**
在虛擬環境中安裝以下套件：
1. 安裝 PySpark：
   ```bash
   pip install pyspark
   ```
2. 安裝機器學習與數據處理庫：
   ```bash
   pip install sklearn
   pip install scikit-learn
   pip install pandas
   ```
3. 安裝 Gradio，用於構建和部署 Web 應用：
   ```bash
   pip install gradio
   ```

### **5. 執行 Python 腳本**
1. 創建並進入工作目錄：
   ```bash
   mkdir workspace
   cd workspace
   ```
2. 執行以下 Python 腳本來進行訓練、預測和評估：
   ```bash
   python3 train.py
   python3 inference.py
   python3 eval.py
   ```

---

## **結論**
通過以上步驟，你已經成功在 Ubuntu 系統上配置了 PySpark 開發環境，並能夠執行相關的 Python 腳本進行數據處理和機器學習任務。

如果遇到任何問題，請檢查是否正確啟動了虛擬環境，或檢查依賴是否完整安裝。

---

## **參考**
- [PySpark 官方文檔](https://spark.apache.org/docs/latest/api/python/)
- [Virtualenv 使用指南](https://virtualenv.pypa.io/en/latest/)