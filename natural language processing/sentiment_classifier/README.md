
# Sentiment Classification: From Basic NLP Concepts to Transformers

## Overview

This project focuses on building sentiment classification models, progressing from basic NLP concepts to advanced transformer-based approaches. It covers the essential steps and methodologies used in the development of sentiment analysis models.

# Model Performance Summary

This table provides a summary of the accuracy achieved by different models on the IMDB sentiment classification task.

| Model                     |  Test Accuracy | Notes                            |
|---------------------------|---------------|----------------------------------|
| LinearSVC                 |  86.76%       | Preprocessing:countvectorizer after cleaning data |
| LinearSVC                 | 87.36%        | Preprocessing:Stemming & lemmatizing after cleaning data |
| LinearSVC                 | 89.84%        | Preprocessing:ngram with n being 3   |
| LinearSVC                 | 90.064%        | Preprocessing:TFIDF after cleaning data   |
| Custom-transformer         | 85.60%        | Preprocessing:raw input data   |




Integration with DVC(data versioning) & DAGHUBS(MLflow) to track experiments:https://github.com/AmulPatil/mlops_sentiment_analysis
