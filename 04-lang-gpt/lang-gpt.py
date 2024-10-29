import speech_recognition as sr
import pygame

from IPython.display import clear_output
from gtts import gTTS
from openai import OpenAI

# Define a class named ChatBot to create a chatbot instance
class ChatBot:
    # Initialize the ChatBot instance with a client and conversation history
    def __init__(self, secret_key):
        # Create an OpenAI client instance using a provided API key
        self.client = OpenAI(api_key=secret_key)
        
        # Initialize a conversation history list with a system message
        # setting the assistant's role to "English teacher"
        self.history = [{'role': 'system', 'content': "You are a English teacher."}]

    # Define a method to generate a response based on user input
    def generate_response(self, prompt: str) -> str:
        # Add the user's message to the conversation history
        self.history.append({'role': 'user', 'content': prompt})

        # Use the OpenAI client to create a response with the conversation history
        completion = self.client.chat.completions.create(
            model='gpt-4o-mini', # Specify the model to use
            messages=self.history # Pass the conversation history to maintain context
        )

        # Extract the assistant's response from the API response
        response = completion.choices[0].message.content
        # Add the assistant's response to the conversation history
        self.history.append({'role': 'assistant', 'content': response})

        return response
    
    # Define a method to retrieve the full conversation history
    def get_history(self) -> list:
        return self.history
    
# print(bot.get_history()) # Helpful function


# Function to recognize speech and adjust waiting time between words
def recognize_speech_with_pause():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # custom pause threshold
    recognizer.pause_threshold = 5

    # Setting the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak something...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listening to the audio
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=20) 

    # Recognize speech using Google's speech recognition API
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, there was an issue with the request."
   

def text_to_speech(text, filename="output.mp3", lang='en', tld='us'):
    # Create the gTTS object
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)

    # Saving the audio to a file
    tts.save(filename)
    print(f"Audio saved as {filename}")

    # Initialize pygame mixer
    pygame.mixer.init()

    try:
        # Load and play the audio
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until the audio is finished playing
        while pygame.mixer.music.get_busy():  # Check if music is playing
            continue  
    finally:
        # Stop the music and quit the mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()


    

def main():
    # Open the file in read mode
    with open("ignore/config.txt", "r") as file:
        secret_key = file.read()  # Read the entire file content

    bot = ChatBot(secret_key)
    # Define an initial question to set the chatbot's behavior
    start_question = "I am studying English, so let's talk in English. Let's discuss a random topic. I want your answer to be in two topics. The first is that you correct my grammar mistakes when I write something wrong. The second topic is that when I type my sentence, you rephrase it so that it is more complete and more coherent. You can start by asking a question about a random topic"

    # Generate the chatbot's response to the initial question and output it
    response = bot.generate_response(start_question)
    print(response)
    # Convert the chatbot's response to speech using text_to_speech
    text_to_speech(response)

    # Use speech recognition to capture the user's response and display it
    recognized_text = recognize_speech_with_pause()
    print("You said:", recognized_text)

    # Run the main loop to continue conversation until manually interrupted
    try:
        while True:
            print('\n')

            # Generate a response from the bot using the recognized text
            response = bot.generate_response(recognized_text)
            print(response)
            # Convert the chatbot's response to speech
            text_to_speech(response)

            # Clear output
            clear_output(wait=True)

            # Capture the next user input using speech recognition
            recognized_text = recognize_speech_with_pause()
            print("You said:", recognized_text)

    # Handle the manual interruption (e.g., Ctrl+C) and exit the loop
    except KeyboardInterrupt:
        print("Loop interrupted by user.")

if __name__ == "__main__":
    main()