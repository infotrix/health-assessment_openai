import os
import sys
import requests
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print(Fore.RED + "Error: The OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

# Headers for the API request
headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json",
}

# OpenAI API endpoint for chat completions
api_endpoint = "https://api.openai.com/v1/chat/completions"


def main():
    # Display the disclaimer and require user acknowledgment
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "DISCLAIMER: All data and interactions within this bot are generated and should be considered fake. "
        "This bot is a proof of concept for development purposes only and should not be used as a basis for real-world "
        "diagnosis or health advice."
    )

    # Require the user to acknowledge the disclaimer before continuing
    ack = input(
        Fore.GREEN + "Do you acknowledge the disclaimer and wish to proceed? (yes/no): "
    )
    if ack.lower() != "yes":
        print(Fore.RED + "You did not acknowledge the disclaimer. Exiting.")
        sys.exit(0)

    # Initialize conversation history
    conversation_history = []

    print(Fore.CYAN + "Health Analysis Bot is starting...\n")
    print(Fore.CYAN + "How can I assist you with your health concerns today?")

    while True:
        # Get user input
        user_input = input(Fore.WHITE + "You: ")
        if user_input.lower() in ["exit", "quit", "end"]:
            print(Fore.CYAN + "Thank you for using the Health Analysis Bot. Goodbye!")
            break

        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Get bot's response
        bot_response = analyze_symptoms(conversation_history)
        print(Fore.CYAN + "Bot: " + bot_response)

        # Append bot's response to conversation history
        conversation_history.append({"role": "assistant", "content": bot_response})


def analyze_symptoms(conversation_history):
    """
    Analyze the provided symptoms and maintain a dialogue using the chat completion endpoint.
    """
    try:
        # Make a POST request with a 30-second timeout
        response = requests.post(
            api_endpoint,
            headers=headers,
            json={"model": "gpt-4", "messages": conversation_history},
            timeout=30,
        )

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON and return the content
            return response.json()["choices"][0]["message"]["content"]
        else:
            # Handle non-successful status codes appropriately
            return f"An error occurred: {response.text}"

    except requests.exceptions.Timeout:
        return "The request timed out after 30 seconds. Please try again later."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    main()
