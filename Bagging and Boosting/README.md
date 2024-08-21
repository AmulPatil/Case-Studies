
**Bagging:**  
Bagging is an ensemble technique that improves the stability and accuracy of machine learning models. It works by training multiple instances of the same model on different subsets of the training data, which are generated through bootstrapping (random sampling with replacement). The predictions from all models are then aggregated, typically by averaging (for regression) or voting (for classification). Bagging reduces variance and helps prevent overfitting, making it particularly effective with high-variance models like decision trees. Random Forest is a popular example of a bagging method.

**Boosting:**  
Boosting is another ensemble technique that aims to convert weak learners into strong ones. Unlike bagging, where models are trained independently, boosting trains models sequentially. Each model attempts to correct the errors made by the previous ones by focusing more on the misclassified instances. This process continues iteratively, with each model weighted according to its accuracy. Boosting reduces both bias and variance, often leading to highly accurate models. Common boosting algorithms include AdaBoost, Gradient Boosting, and XGBoost.

Intro.ipynb: it will shows why ensemble models works better then single models algorithms.
