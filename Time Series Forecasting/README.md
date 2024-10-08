# **Data Ingestion Pipeline with Apache Airflow**

## **Overview**

This project demonstrates how to automate the process of capturing data from an external API and storing it into a MySQL database using Apache Airflow. This workflow is essential for regularly updating your database with the latest information from the API.

## **Prerequisites**

Before setting up the pipeline, ensure the following are in place:

- **Python**: Installed on your machine
- **Apache Airflow**: Installed and properly configured
- **MySQL Database**: Running and accessible
- **Basic Knowledge**: Familiarity with Python, APIs, SQL, and Airflow

## **Setup Instructions**

### **1. Configure MySQL Database**

- **Create a Database**: Set up a MySQL database to store the data.
- **Create Tables**: Define the schema for storing the API data.

### **2. Define the Airflow DAG**

Create an Apache Airflow Directed Acyclic Graph (DAG) to automate the data ingestion process. The DAG will:

1.Start the script daily at set time.\
2.Script will fetch the data ,rewrite the schema and ingest/put the data into mysql.\
## **Future Work**

### **Product Forecasting**

In the future, we plan to enhance this pipeline with product forecasting capabilities. This will involve:

1. **Data Analysis**: Analyzing historical product data to identify trends and patterns.
2. **Forecasting Models**: Implementing machine learning models to predict future product demand and trends.
3. **Integration**: Updating the pipeline to include forecasting results and making them available for analysis.

## **Conclusion**

This pipeline automates the ingestion of API data into a MySQL database using Apache Airflow, providing a reliable and scalable solution for data management. Future enhancements will focus on leveraging this data for predictive analytics and product forecasting.

