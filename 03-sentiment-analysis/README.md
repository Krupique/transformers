# Fine-Tuning a Transformer Model for Sentiment Classification

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

03-sentiment-analysis/ <br/>
├── data/ <br/>
│   ├── test_data.txt <br/>
│   │── train_data.txt <br/>
├── basic-dnn.ipynb <br/>
├── lstm.ipynb <br/>
├── transformer.ipynb <br/>
├── README.md <br/>
└── transformer-main.py <br/>

---
## Neural Networks Archtectures
### Feedforward Neural Networks (FNN)
A **Feedforward Neural Network (FNN)** is the simplest type of artificial neural network, where information flows in one direction: from input to output, without any cycles or feedback loops. It consists of layers of neurons, including an input layer, one or more hidden layers, and an output layer. Each neuron in one layer is connected to every neuron in the next layer through weighted connections. The network learns by adjusting these weights during training using a process called backpropagation, which minimizes the error in the predictions. FNNs are commonly used for tasks like classification and regression, but they lack memory and cannot handle sequential data, making them unsuitable for time-series or language tasks. Their simplicity and ease of implementation make them a foundational architecture in deep learning.

In this project, I developed a model using TensorFlow, consisting of four dense hidden layers and an output layer as follows:
- **1st dense layer**: 4096 neurons
- **2nd dense layer**: 2048 neurons
- **3rd dense layer**: 1024 neurons
- **4th dense layer**: 64 neurons
- **Output layer**: 6 neurons, corresponding to the number of output classes

This architecture enables the model to progressively reduce dimensionality and capture complex patterns before outputting predictions across the 6 classes.


### LSTM
**Long Short-Term Memory (LSTM)** is a type of recurrent neural network (RNN) specifically designed to handle long-range dependencies and overcome the limitations of standard RNNs, which struggle with remembering information over extended sequences. LSTMs achieve this by using a series of gates—input, forget, and output gates—that control the flow of information and decide what to keep or discard at each time step. This structure allows LSTMs to remember relevant information over long periods while discarding irrelevant data. LSTMs are particularly effective for tasks involving sequential data, such as time series prediction, speech recognition, and natural language processing. Their ability to manage both short- and long-term dependencies makes them a powerful tool for complex sequence-based tasks.

In this project, I developed a model using TensorFlow, with your LSTM functionalities. The model architecture begins with an **embedding layer**, which converts input data (typically sequences) into dense vectors of fixed size, allowing the model to work with the textual or sequential data in a meaningful way. Following the embedding, I added an **LSTM layer** to capture temporal dependencies and patterns in the sequential data. Finally, I implemented an **output layer** with 6 neurons, representing the 6 output classes.

Additionally, I applied the **dropout technique** after both the LSTM and dense layers to prevent overfitting by randomly dropping a fraction of the neurons during training. This ensures better generalization and improves the model's robustness.

### Transformers
Transformers are a type of neural network architecture that use self-attention mechanisms to process input data in parallel, enabling them to capture long-range dependencies more efficiently than traditional recurrent models like LSTMs. Unlike RNNs, transformers handle the entire input sequence at once, making them ideal for tasks that require understanding context over large sequences, such as natural language processing (NLP), machine translation, and text generation. The key components of a transformer model are:
- **Self-Attention Mechanism**: Allows the model to weigh the importance of different words or tokens in a sequence.
- **Positional Encoding**: Injects information about the position of tokens since transformers don't inherently process sequentially.
- **Multi-Head Attention**: Uses multiple self-attention mechanisms in parallel to capture different aspects of the input.
- **Feedforward Layers**: Dense layers applied after the attention mechanism to generate outputs.
This architecture has become a foundation for modern NLP models like BERT and GPT.


**DistilBERT Base Multilingual Cased**:<br/>
DistilBERT is a smaller, faster, and more efficient version of BERT (Bidirectional Encoder Representations from Transformers) that retains 97% of its performance while being 60% smaller and 2x faster. The **Base Multilingual Cased** variant is trained on a wide variety of languages (104 in total) and is case-sensitive, meaning it distinguishes between upper- and lower-case letters.

DistilBERT uses a process called **knowledge distillation**, where a smaller "student" model (DistilBERT) is trained to mimic a larger "teacher" model (BERT). This allows it to capture the knowledge of the larger model while being more efficient in terms of memory and computation. The **multilingual** nature allows it to perform well across different languages, and the **cased** aspect makes it sensitive to differences in capitalization, which is important for tasks that require fine-grained text understanding.

This architecture is commonly used for various NLP tasks, including text classification, named entity recognition, and language translation across multiple languages.


**Using DistilBERT Base Multilingual Cased for Transfer Learning**

DistilBERT base multilingual cased is a lighter, faster version of BERT that supports multiple languages and is well-suited for transfer learning on NLP tasks such as text classification, sentiment analysis, or question answering across diverse languages. The following steps outline how to fine-tune DistilBERT on a new dataset to adapt it to a specific task.

**Step 1: Load the Model and Tokenizer**

The Hugging Face Transformers library provides an easy way to load pre-trained models. We’ll start by loading the `distilbert-base-multilingual-cased` model along with its tokenizer, specifying the number of labels required for our task (e.g., 2 labels for binary classification).

**Step 2: Preprocess Input Data**

Before passing text to the model, it needs to be tokenized. Tokenization converts text into numerical format, along with padding and truncation to ensure uniform input lengths, which is crucial for efficient batching.

**Step 3: Fine-Tune the Model**

To adapt DistilBERT to our specific task, we'll fine-tune it on labeled data. This can be done efficiently using Hugging Face’s `Trainer` API, which manages the training loop and optimizes model weights to minimize loss on the training data.

**Step 4: Evaluate and Deploy**

After fine-tuning, we'll evaluate the model on a validation dataset to measure performance. Then, we'll save the fine-tuned model for future use and deploy it to handle inference requests.




---
### Benchmark
Comparing the three developed archtectures:

| Model       | Accuracy    | Time        | GPU or CPU  |
|-------------|-------------|-------------|-------------|
| DNN         | 0.8555      | 3min 38s    | CPU         |
| LSTM        | 0.8855      | 3min 48s    | CPU         |
| Transformer | 0.9005      | 8min 10s    | GPU         |


---
### Next steps
* Convert transformer notebook to python file;
* MLOps for transformer;
* Model Deploy on AWS.
