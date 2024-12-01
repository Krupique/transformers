# Imports
import argparse
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def main(prompt: str):
    # Loading the tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")

    # Loading the model
    model = GPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id = tokenizer.eos_token_id)

    # Tokeniza o texto do prompt
    input_ids = tokenizer.encode(prompt, return_tensors = 'pt')

    # Generating text from prompt with initial text
    generated_text = model.generate(input_ids, max_length = 100, num_beams = 5, no_repeat_ngram_size = 2, early_stopping = True)

    response = tokenizer.decode(generated_text[0], skip_special_tokens = True)

    return response



if __name__ == "__main__":
    # Argument parser for dynamic input
    parser = argparse.ArgumentParser(description="Generate text using GPT-2")
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The initial text prompt for the GPT-2 model."
    )
    args = parser.parse_args()

    response = main(prompt=args.prompt)
    print(response)

# Usage example: python run.py --prompt "Once upon a time in a faraway land"
