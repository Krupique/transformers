# AI Assistent using GPT-2

### **Introduction**  
This project explores the use of the GPT-2 language model from the Transformers library to generate text based on user-provided prompts. It allows inference execution through a Python script, providing a simple and efficient interface for interacting with pre-trained language models.

### **Motivation**  
With advancements in AI technologies, language models are playing a crucial role in various applications, from chatbots to content creation tools. This project aims to demonstrate, in a practical way, how to use a pre-trained language model to generate coherent and creative text, addressing the challenges of integrating such models into real-world solutions.

### **Objective**  
The primary goal of this project is to create a functional pipeline for text generation using the GPT-2 model, which can serve as a foundation for NLP (Natural Language Processing) experiments or be integrated into broader projects. It seeks to combine accessibility and performance, using adjustable parameters to control the model's output.

### **Model Used**  
The model used is GPT-2 Large, developed by OpenAI, a larger variant of GPT-2. This model is based on a Transformer architecture and is known for its ability to generate high-quality text resembling human writing. For this project, GPT-2's inference capabilities were utilized, along with techniques like `beam search` to enhance the coherence and quality of the generated text.

### **Project Steps**  

1. **Loading the Tokenizer and Model**  
   The tokenizer and GPT-2 model are loaded using the Transformers library. The `pad_token_id` was set to match the model's `eos_token_id`, ensuring the text is properly handled during inference.

2. **Tokenizing the Prompt**  
   The initial text provided by the user is tokenized for processing by the model. This process converts the input text into numerical tensors.

3. **Text Generation**  
   Text is generated using the `generate` method, which implements strategies such as `beam search` to ensure diversity and avoid excessive repetition of words or phrases.

4. **Decoding the Response**  
   The model's output is decoded into readable text, removing special tokens, and then presented to the user.

5. **User Interface**  
   An argument parser was implemented to allow the prompt to be passed as a parameter to the script, enabling dynamic interaction with the model.

---

## **Instructions to Run the Project**

Below are the steps to execute the project with and without the Dockerfile.


### **1. Running the Project Without Docker**

#### **Prerequisites**
- Python 3.12.3 installed on your system.
- Poetry installed globally. (You can install it using `pip install poetry`.)
- Necessary Python dependencies specified in `pyproject.toml`.

#### **Steps**
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**
   ```bash
   poetry install
   ```

3. **Run the Script**
   Execute the script by passing the desired prompt:
   ```bash
   poetry run python run.py --prompt "Your custom prompt here"
   ```

---

### **2. Running the Project With Docker**

#### **Prerequisites**
- Docker installed on your system.

#### **Steps**
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build the Docker Image**
   Build the image using the provided `Dockerfile`:
   ```bash
   docker build -t gpt2-text-generator .
   ```

3. **Run the Docker Container**
   Execute the container and pass your custom prompt:
   ```bash
   docker run --rm gpt2-text-generator --prompt "Your custom prompt here"
   ```

4. **Override Default CMD (Optional)**
   If you need to override the default `CMD`, you can specify your arguments after the image name:
   ```bash
   docker run --rm gpt2-text-generator --prompt "Once upon a time"
   ```

---

### **Notes**
- The `Dockerfile` is set up to use Poetry for dependency management and execution.
- If you need to modify the exposed port or integrate the project with an API, you can uncomment and modify the `EXPOSE` line in the `Dockerfile`.
- For persistent data storage, consider using Docker volumes.

This ensures that the project can run smoothly in both local and containerized environments.

---

### **References**  
- OpenAI. "GPT-2: Language Models are Unsupervised Multitask Learners." Available at: [https://openai.com/research/language-models](https://openai.com/research/language-models)  
- Hugging Face. "Transformers Documentation." Available at: [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)  
- Vaswani, A. et al. "Attention Is All You Need." NeurIPS, 2017. Available at: [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)  
