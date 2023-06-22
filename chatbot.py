import openai
import argparse
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

def main():
    messages = []

    parser = argparse.ArgumentParser(description="Simple command line with GPT")

    parser.add_argument("--personality", 
                        type=str, 
                        help="A brief summary of the chatbot's personality", 
                        default="friendly and helpful")
    
    arguments = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {arguments.personality}"

    messages = [{"role": "assistant", "content": initial_prompt}]

    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )

            messages.append(response["choices"][0]["message"].to_dict())

            print("Assistant: ", response["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()