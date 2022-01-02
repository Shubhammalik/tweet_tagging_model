# Twitter Online Learning
Goal for this project is to classify twitter review sentiment with implementation of Online learning.

Online learning is the process of retraining the model as the data comes in streams of continuously generated data.

[Dataset](https://www.kaggle.com/paoloripamonti/twitter-sentiment-analysis/data) contains Twitter tweets records (Size - 1.6M unique records).

# Coverage and Modules insights
1) **Data processing** extraction of useful data features
2) **ETL** Cleaning and Filtering of data with operations like removal of stop words, punctuations, urls, repeating phrases, encodings 
3) **Visualizations** of data distributions, word clouds
4) **Microservice Implementing** - each service developed can be used as a module in external environment
5) **NLP** using techniques like Tokenization, Stemming and Lemmatization
6) **Model comparator** which compares multiple model stats and saves the best performing model
7) **Model selector** keeps checking for best performing model and selects the top model for production
8) **Clock function** which garbage collects the obsolete models and data files based on business rules
9) **Model run history** covers all previous best runs of every model

# Tech Stack
TBU
1) Data Cleaning, Filtering & Manipulation - Regular expressions, pandas and numpy dataframes
2) Data Visualization - Plotly, Seaborn, Matplotlib, word cloud
3) Data Storage - local
4) Webapp - TBA

# Running Instructions
1) Download the project and run the below requirements in the project folder terminal

    `pip install -r /path/to/requirements.txt`

# Task at Hand
1) Implement logging at a modular level
2) Exception Handling for data transformation and model selector
3) Enhance model training and history to parametric modules 
4) Implement clock function to remove obsolete models/data
5) Create and load environment variable file


       
# Illustration from Data
**Data Stats**
![Data Distribution](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/eda/data_visuals.png)

**Positive Word Cloud**
![Positive](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/wc/300000/positive_wc_300000.png)

**Negative Word Cloud**
![Negative](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/wc/300000/negative_wc_300000.png)

# MODEL EVALUATION
**Beroulli NB Model**
![Beroulli NB Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/bernoulli_nb_cf_300000.png)
![Beroulli NB Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/bernoulli_nb_roc_300000.png)

**Linear Model**
![Linear Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/linear_svc_cf_300000.png)
![Linear Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/linear_svc_roc_300000.png)

**Logistic Regression Model**
![Logistic Regression Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/lr_cf_300000.png)
![Logistic Regression Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/lr_roc_300000.png)

**Mutlinomial NB Model**
![Mutlinomial NB Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/multinomial_nb_cf_300000.png)
![Mutlinomial NB Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/multinomial_nb_roc_300000.png)

**XGBoost Model**
![XGBoost Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/xgboost_cf_300000.png)
![XGBoost Model](https://github.com/Shubhammalik/tweet_tagging_model/blob/main/static/model_eval/300000/xgboost_roc_300000.png)
