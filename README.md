# FraudShield-AI
AI-powered payment card fraud detection using supervised and unsupervised learning

Methods/ algorithms that we will be using to train our model 

For supervised learning we will use:
1) Logistic Regression
2) Random Forest
3) LightGBM or XGboost
Builds trees one after another, with each new tree fixing the mistakes of the ones before it.
Pros:

Usually the most accurate method for table-style data 
Built-in setting for rare classes (scale_pos_weight), no need for SMOTE(creates synthetic data if the minority class is considered too low)
LightGBM is very fast on millions of rows and can use category columns directly
Handles missing values on its own

Cons

More settings to tune (learning rate, tree depth, number of trees)
Can overfit if the settings are wrong, so you need a validation set
A "black box" unless you add an explanation tool like SHAP

Unsupervised Model
1) Isolation Forest