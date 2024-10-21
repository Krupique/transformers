# Fine-Tuning de um modelo Transformer para Classificação de Sentimento


# Introduction
In recent years, sentiment analysis has become an essential tool for understanding the opinions and emotions expressed in large volumes of textual data. With the exponential growth of digital interactions—whether on social media, forums, or product reviews—the need to interpret these emotions in an automated way has become increasingly relevant.

This project aims to develop a sentiment classification model using advanced artificial intelligence algorithms, focusing on neural networks and transformer architecture. By applying these technologies, we seek to identify and categorize sentiments (joy, sadness, anger, fear, love and surprise) present in texts collected from a dataset available on Kaggle.


## Dataset
**Dataset Card for TSATC: Twitter Sentiment Analysis Training Corpus**

Dataset Summary
TSATC: Twitter Sentiment Analysis Training Corpus The original Twitter Sentiment Analysis Dataset contains 1,578,627 classified tweets, each row is marked as 1 for positive sentiment and 0 for negative sentiment. It can be downloaded from [Oficial link](http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip). The dataset is based on data from the following two sources:

University of Michigan Sentiment Analysis competition on Kaggle Twitter Sentiment Corpus by Niek Sanders

This dataset has been transformed, selecting in a random way a subset of them, applying a cleaning process, and dividing them between the test and train subsets, keeping a balance between the number of positive and negative tweets within each of these subsets. These two files can be founded on [github.com](https://github.com/cblancac/SentimentAnalysisBert/blob/main/data).

Finally, the train subset has been divided in two smallest datasets, train (80%) and validation (20%). The final dataset has been created with these two new subdatasets plus the previous test dataset.

## Project structure

The project has the following structure: The data directory contains the training and testing datasets. The basic-dnn, lstm and transformer files contain the implementations, according to their respective names. And the transformer-main.py file contains the transformer architecture developed so that it can be scaled to production via AWS.

03-sentiment-analysis/
├── data/
│   ├── test_data.txt
│   │── train_data.txt
├── basic-dnn.ipynb
├── lstm.ipynb
├── transformer.ipynb
├── README.md
└── transformer-main.py




---
Falar sobre:
[ ] No código, explicar sobre os pacotes e técnicas utilizadas, tais como Spacy, método de Encode, etc.
[x] Falar sobre a ideia do projeto
[ ] Os três modelos desenvolvidos (Rede Neural Normal, LSTM e Arquitetura Transformers)
[ ] Falar sobre a plataforma HuggingFace
[ ] Falar sobre a arquitetura Bert
[ ] Comparar os resultados
[ ] Olhar o código do Transformers e o que dá para documentar melhor

Próximos passos:
[ ] Documentação
[ ] Algoritmo em Python pronto para MLOps
[ ] Como encaixar Docker e outras ferramentas parecidas
[ ] Subir o modelo para produção utilizando AWS