# Creating an LLM Model Based on BERT from Scratch  

## Project Objective  

This project aims to create a Large Language Model (LLM) based on the BERT architecture from scratch, exploring every fundamental step of its development. The process encompasses tasks ranging from data loading and preparation, building an optimized vocabulary, and defining special tokens to implementing the complete model architecture. This architecture includes modules such as Embedding, Multi-Head Attention, and Encoder Layers. Additionally, the project covers hyperparameter configuration, training strategies, model evaluation, and generating predictions. By following this step-by-step approach, the goal is not only to reproduce the effectiveness of BERT but also to gain a deep understanding of the principles and mechanisms that make this architecture so powerful in natural language processing.  

1. **Data Loading**  
   Prepare and load the text corpus that will be used to train the model, ensuring its quality and relevance to the application domain.  

2. **Vocabulary Construction and Special Token Definition**  
   Build the set of tokens that the model will use, including special tokens ([CLS], [SEP], [MASK], and [PAD]) essential for tasks such as classification, sentence separation, and masking.  

3. **Hyperparameter Definition**  
   Configure the parameters that control the model’s training and architecture, such as the number of layers, attention heads, vocabulary size, and learning rate.  

4. **Batch Creation for Training**  
   Split the data into smaller batches to optimize training efficiency and enable the model to process large data volumes incrementally.  

5. **Model Construction**  
   - **Embedding Module:** Converts tokens into high-dimensional vectors, incorporating both token and positional information.  
   - **Scaled Dot Product Attention:** Implements the attention mechanism, enabling the model to focus on relevant parts of the text.  
   - **Multi-Head Attention Module:** Enhances the model's attention capability, allowing it to analyze different aspects of the text simultaneously.  
   - **Positional Feedforward Module:** Adds a non-linear layer to improve the model's expressiveness.  
   - **Encoder Layer Module:** Combines multi-head attention and feedforward components, forming the foundation of the BERT model.  
   - **Final Architecture:** Integrates all layers to create the complete BERT model structure.  

6. **Model Training and Evaluation**  
   Train the model with the data and evaluate its performance on specific tasks, fine-tuning parameters to improve results.  

7. **Generating Predictions with the Model**  
   Use the trained model to infer results on new data, demonstrating its practical application and predictive capabilities.  

---

## **Concept of Generative AI**

Generative Artificial Intelligence, particularly in the context of Large Language Models (LLMs), refers to the ability of these models to create new and original content based on patterns and information learned during training on vast volumes of textual data. This generative aspect stands out for several reasons:

**Text Generation**: LLMs can generate coherent and contextually relevant texts, including articles, stories, code scripts, poetry, and even responses to specific questions. This generation is achieved by processing user input and constructing a response that logically follows from that input.

**Creativity and Innovation**: One of the most notable characteristics of generative models is their ability to combine information in novel and creative ways. For instance, they can craft stories with original plots or suggest innovative solutions to problems.

**Personalization**: These models can be tailored to generate content specific to certain contexts or user needs. This means they can produce personalized content in a wide range of styles and formats.

**Interactivity**: Generative models enable bidirectional interaction, where the model not only responds to inputs but can also ask questions, suggest topics, or guide a conversation.

**Translation and Linguistic Adaptation**: They can be used to translate texts between languages or adapt content to different dialects or linguistic styles.

It is important to note that despite their advanced capabilities, generative models have limitations, such as the potential to generate incorrect or biased information and their lack of real-world understanding or consciousness. Additionally, the responsible use of these models is a subject of ongoing debate, involving ethical concerns and copyright issues. 

---

## Applications of Generative AI  

Generative AI has found applications across a variety of fields and contexts. Below are some examples:  

* **Art and Design:**  
    - **Image Generation:** Models like OpenAI's DALL·E can create original images based on textual descriptions.  
    - **Music:** Models can compose original music or emulate specific artists' styles.  
    - **Product Design:** Generative AI can be used to create product designs, such as furniture or clothing, optimized for specific criteria.  

* **Entertainment and Media:**  
    - **Character Creation for Games:** Generative models can create characters, settings, and objects for games.  
    - **Movies and Animations:** AI can generate animations or even write scripts.  

* **Science and Research:**  
    - **Drug Discovery:** Models can generate molecular structures for potential new drugs.  
    - **Data Simulation:** In areas with scarce data, Generative AI can create simulated datasets for research purposes.  

* **Business and Commerce:**  
    - **Website Design:** Models can propose website designs based on specific criteria or trends.  
    - **Personalized Advertising:** Graphic advertisements can be generated specifically to cater to an individual user's interests.  

* **Fashion:**  
    - **Clothing Design:** Generative models can create innovative clothing designs or textile patterns.  

* **Forgeries and Deepfakes:**  
    Unfortunately, Generative AI also has a darker side. It can be used to create "deepfakes," which are manipulated videos or audio recordings where individuals appear to say or do things they never actually did. This raises serious ethical and security concerns.  

These are just a few examples, and the list continues to grow as the technology advances and finds new applications across various industries.  

---

## What is Natural Language Processing?

Natural Language Processing (NLP) is a field of study and application at the intersection of computer science, artificial intelligence, and linguistics. The goal of NLP is to enable computers to understand, interpret, manipulate, and respond to human language in a useful and meaningful way. Here are the key aspects of NLP:

- **Language Understanding**: NLP involves the development of algorithms and systems that allow computers to understand human text and speech. This includes the ability to understand grammar, semantics, context, and nuances of language.
- **Language Generation**: In addition to understanding language, NLP also deals with generating text and speech. This can involve creating coherent responses in a conversation, generating written texts in different styles, or automatic translation between languages.
- **Sentiment Analysis**: NLP can be used to analyze opinions and sentiments in texts, such as determining whether a comment is positive, negative, or neutral.
- **Information Extraction**: This area of NLP focuses on extracting specific information from texts, such as names, locations, dates, or other relevant data.
- **Speech Processing**: NLP also extends to speech recognition and synthesis, allowing AI systems to understand and produce spoken language.
- **Machine Translation**: Translating text or speech from one language to another is another important application of NLP, though it presents challenges due to the complexities and nuances of languages.
- **Question Answering**: NLP systems can be programmed to answer questions asked in natural language, by finding and providing the relevant information.
- **Virtual Assistants and Chatbots**: Many virtual assistants and chatbots use NLP to understand and respond to user commands or questions.

NLP is an active and rapidly evolving area of research and development, driven by the increasing amount of available text and speech data, advancements in machine learning algorithms, and greater computational processing power. The applications of NLP are becoming more common in our daily lives, from simple spell check tools to sophisticated human-machine interaction systems.

---

## LLMs (Large Language Models) and the Revolution in NLP

Large Language Models (LLMs) represent one of the most significant innovations in the field of Natural Language Processing (NLP). These models are AI systems trained on vast textual datasets, enabling them to understand and generate human language in a surprisingly coherent and relevant way.

The development of LLMs marks a revolution in NLP for several reasons. Firstly, their ability to generate text that seems natural and human-like is impressive. They can write essays, create poetry, program in various computer languages, and even emulate specific writing styles. This opens up a wide range of practical applications, from automating writing tasks to supporting educational and learning systems.

Additionally, LLMs have the ability to understand context and perform complex tasks such as question answering and comprehension, which is crucial in areas like virtual assistants, chatbots, and automated information systems. They can process information, extract relevant knowledge from large volumes of text, and even perform some forms of reasoning.

Another revolutionary aspect of LLMs is their flexibility. They can be adapted for different languages and dialects, making them valuable tools in multilingual contexts. Furthermore, they can be trained or fine-tuned for specific tasks, improving their efficiency and effectiveness in specialized areas such as medicine, law, and finance.

However, there are challenges and limitations. One of them is bias, which may be inherent in the training data. This requires careful attention to ensure that the outputs do not reinforce stereotypes or prejudices. Additionally, although they are advanced in linguistic terms, LLMs do not possess an understanding of the real world or consciousness, limiting their ability to understand complex contexts or ethical nuances.

LLMs represent a significant leap in NLP, offering the potential for countless practical and creative applications. However, their responsible use and overcoming technical and ethical challenges remain areas of intense research and development.

---

## What is the Relationship Between Transformers and LLMs?

Transformers and LLMs (Large Language Models) are directly related in the field of NLP and machine learning. Let's break down this relationship:

- **Transformer Architecture:**
  
    The Transformer architecture was introduced in a research paper published by Vaswani et al. in 2017, titled “Attention is All You Need.”
    
    This architecture introduced a new way of handling sequences by using what is known as the "self-attention mechanism," which allows the model to focus on different parts of a sequence depending on the context. This made Transformers particularly powerful for sequence-to-sequence tasks, such as machine translation.
    
- **LLMs (Large Language Models):**
  
    These are language models trained on large volumes of text. They have the ability to generate text, complete sentences, answer questions, and perform a variety of other tasks related to Natural Language Processing.
    
    What makes a language model an "LLM" is, in large part, its scale—these models are trained with billions or even millions of parameters.
    

The Transformer architecture is the backbone of the most popular and powerful LLMs. Models like BERT, GPT, T5, and others are based on the Transformer architecture. When we say “GPT is a Transformer,” we are referring to the fact that GPT uses the Transformer architecture to process and generate text.

**Why are Transformers popular for LLMs?**

The ability of Transformers to handle long-range dependencies in text and their efficiency in parallelization make these models ideal for training LLMs. Furthermore, their attention mechanism allows them to capture nuances and patterns in large volumes of data, which is essential for superior performance in NLP tasks.

---

## BERT Architecture and Its Relationship with LLMs

**BERT (Bidirectional Encoder Representations from Transformers)** is one of the most influential architectures in the field of Natural Language Processing (NLP) and a milestone in the development of Large Language Models (LLMs). Created by Google AI in 2018, BERT is based on the Transformer architecture and introduced the concept of bidirectional learning for language modeling. This means it analyzes the context of words by simultaneously looking at the tokens to the left and right of each word, allowing it to capture deep semantic relationships. This feature distinguishes it from unidirectional models, such as the GPT of the time, which processed text in only one direction (from left to right).

Historically, BERT is the result of the advancement initiated by the Transformer, introduced in 2017 in the paper *"Attention is All You Need"*. While the Transformer was designed for multiple applications, BERT focused exclusively on the *encoders*, making it ideal for text comprehension tasks. Its impact was immediate: it redefined benchmarks like SQuAD and GLUE and became the foundation for many subsequent models in NLP.

BERT's training is done in two main tasks: *Masked Language Modeling (MLM)* and *Next Sentence Prediction (NSP)*. In MLM, some words are masked in the input text, and the model learns to predict these words based on the context. In NSP, the model learns to determine whether one sentence logically follows another, improving its ability to understand relationships between sentences. Additionally, BERT uses a tokenization method called *WordPiece*, which splits words into subwords, allowing greater flexibility in handling rare or unknown words.

**Advantages**  
Among BERT's advantages is its ability to deeply understand the context of words, making it especially effective in tasks like text classification, entity extraction, and question answering. It also popularized the concept of transfer learning in NLP, where a model pre-trained on large datasets can be fine-tuned for specific tasks with less data. This approach saves time and computational resources.

**Disadvantages**  
However, BERT has some limitations. Its computational cost is high, both for training and inference, due to the large number of parameters. This makes it unsuitable for devices with limited resources, such as smartphones. Additionally, since it is based solely on *encoders*, BERT is not ideal for text generation tasks, which are better suited for models based on *decoders*, like GPT.

In summary, BERT is one of the cornerstones of modern LLMs, directly influencing subsequent models and techniques. It set a new standard in NLP by providing a robust contextual understanding and highly effective solutions for text comprehension tasks, even though it has some practical limitations.


---

## Métricas de Avaliação de Performance dos LLMs

A avaliação da performance de LLMs (Large Language Models) em tarefas de Processamento de Linguagem Natural (PLN) envolve várias métricas que ajudam a medir a precisão, a coerência e a relevância dos textos gerados ou das previsões feitas. As métricas variam dependendo da tarefa específica, mas aqui estão algumas das mais comuns:

**1. Perplexidade**

- **Definição**: Perplexidade mede o quão bem o modelo prevê a próxima palavra em uma sequência de texto. Uma baixa perplexidade indica que o modelo está prevendo com mais confiança e precisão.
- **Aplicação**: Muito usada para avaliar modelos de linguagem em tarefas de geração de texto, como resposta a perguntas ou tradução automática.
- **Limitações**: Embora seja uma métrica útil para medir a "confiança" de um modelo, ela nem sempre se correlaciona com a qualidade percebida do texto gerado.

**2. BLEU (Bilingual Evaluation Understudy)**

- **Definição**: BLEU é uma métrica que compara o texto gerado pelo modelo com referências (ou textos de referência) usando a sobreposição de n-gramas (sequências de palavras). A pontuação BLEU vai de 0 a 1 (ou 0 a 100%) e indica quão próximo o texto gerado está da referência.
- **Aplicação**: Comumente usada em tradução automática, mas também aplicável em tarefas como resumo de texto.
- **Limitações**: BLEU não leva em conta a qualidade semântica e muitas vezes penaliza injustamente variações válidas que não estão nas referências.

**3. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**

- **Definição**: ROUGE mede a similaridade entre o texto gerado e o de referência com base em contagens de sobreposição de n-gramas, palavras e subsequências de palavras. As variantes mais comuns são ROUGE-N, ROUGE-L, e ROUGE-S.
- **Aplicação**: Utilizada principalmente em tarefas de resumo de texto e geração de respostas.
- **Limitações**: ROUGE também pode ser insensível a variações semânticas válidas, além de ser uma métrica baseada apenas em similaridade de superfície.

**4.** **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**

- **Definição**: A métrica METEOR foca na correspondência entre sinônimos, inflexões e ordem das palavras, oferecendo uma análise mais detalhada em comparação ao BLEU e ROUGE.
- **Aplicação**: Utilizada em tradução automática e outras tarefas de geração de texto, como resumo, pois leva em conta tanto a correspondência exata quanto a ordem.
- **Limitações**: Como é mais complexa, METEOR é mais custosa computacionalmente e pode não se aplicar bem em textos mais longos.

**5.** **F1-Score**

- **Definição**: O F1-Score é a média harmônica entre precisão e recall. A precisão mede a porcentagem de previsões corretas em relação às previsões totais, enquanto o recall mede a porcentagem de previsões corretas em relação aos dados corretos.
- **Aplicação**: Usada em tarefas de classificação, como análise de sentimentos, classificação de perguntas e respostas e detecção de entidades nomeadas.
- **Limitações**: Pode não capturar a complexidade das respostas geradas em tarefas de geração de texto.

**6.** **Exact Match (EM)**

- **Definição**: EM mede a proporção de respostas exatas (idênticas) entre a resposta do modelo e a resposta correta esperada.
- **Aplicação**: Comum em tarefas de resposta a perguntas, especialmente para perguntas onde há uma única resposta correta.
- **Limitações**: Não captura variações linguísticas válidas e é rígida, sendo mais adequada para perguntas com respostas curtas e objetivas.

**7. CIDEr (Consensus-based Image Description Evaluation)**

- **Definição**: CIDEr mede a similaridade entre a descrição gerada e as descrições de referência usando o consenso entre várias descrições de referência.
- **Aplicação**: Embora seja mais popular em geração de descrições de imagens, pode ser usada em tarefas de resumo de texto ou em tarefas multimodais, onde o modelo gera descrições a partir de dados de entrada variados.
- **Limitações**: Depende de múltiplas descrições de referência para um bom desempenho, o que nem sempre é viável.

**8. Métrica de Coerência e Fluência**

- **Definição**: São métricas qualitativas que avaliam se o texto gerado é coerente e fluente, ou seja, se faz sentido e é bem estruturado. Em geral, são medidas subjetivas, às vezes usando avaliações humanas, ou calculadas com base na probabilidade de um texto conforme modelos de linguagem como BERT.
- **Aplicação**: Úteis para modelos de geração de texto onde a coerência narrativa é essencial, como em diálogos e redação criativa.
- **Limitações**: Avaliações qualitativas dependem da percepção humana, o que torna difícil padronizar e automatizar.

**9. Human Evaluation (Avaliação Humana)**

- **Definição**: Avaliação humana envolve pessoas que julgam a qualidade dos textos gerados, classificando critérios como relevância, coerência, fluência e adequação.
- **Aplicação**: Fundamental para tarefas onde as métricas automáticas não capturam bem a qualidade, como em geração criativa de conteúdo.
- **Limitações**: É uma avaliação subjetiva, custosa e demorada, além de difícil de reproduzir.

**Resumo das Métricas de Avaliação de LLMs**

As métricas de avaliação de LLMs são diversas e variam de acordo com a tarefa. Métricas baseadas em n-gramas (como BLEU, ROUGE e METEOR) são úteis, mas muitas vezes limitadas, enquanto métricas mais complexas, como CIDEr e avaliações humanas, são necessárias para entender o desempenho em tarefas que exigem criatividade e flexibilidade. Em última análise, o uso combinado de várias métricas fornece uma visão mais abrangente e robusta da performance dos LLMs.