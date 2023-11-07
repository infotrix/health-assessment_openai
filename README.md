# Health Analysis Bot

This is a proof of concept for a Health Analysis Bot using OpenAI's GPT-4 API. It's designed to analyze a list of symptoms and provide a possible health analysis. This project is for demonstration purposes and uses synthetic data.

## Version

0.3.0

## Author

Ken Newton

## Setup

1. **Clone the repository:**
   ```
   git clone [repository_url]
   ```
2. **Install dependencies:**
   ```
   pip install openai
   ```

3. **Set up your OpenAI API key:**
   - Obtain your API key from OpenAI.
   - Create a file named `.env` in the root directory.
   - Add your API key to the `.env` file like so:
     ```
     OPENAI_API_KEY='your-api-key'
     ```
   - The application will read this key from the environment variables.

## Bot Usage

1. Initialize the `HealthAnalysisBot` object:
   ```python
   from health_bot import HealthAnalysisBot

   bot = HealthAnalysisBot()
   ```

2. Use the `analyze_symptoms` method to get health analysis:
   ```python
   symptoms = "persistent cough, fever, and shortness of breath"
   analysis = bot.analyze_symptoms(symptoms)
   print(analysis)
   ```
---

## How to Use the Health Analysis Bot

Welcome to the Health Analysis Bot! This tool is designed to help you get insights into possible health conditions based on the symptoms you describe. Please follow the instructions below to get the most accurate analysis:

### Getting Started

1. **Open the Chat Interface**: Begin by opening the chat interface of the Health Analysis Bot.

2. **Describe Your Symptoms**: In your own words, describe the symptoms you are experiencing. Be as specific and detailed as possible. 

### Tips on Describing Symptoms

- **Be Specific**: Instead of saying "I feel sick," describe your symptoms in detail, such as "I have a sharp, recurring pain on the left side of my abdomen that started two days ago."

- **Include Duration**: Mention how long you have been experiencing the symptoms. For example, "I have had a mild headache that comes and goes over the past week."

- **Mention Severity**: Describe how severe the symptoms are and how they are affecting your daily activities. For instance, "The pain in my back is severe enough that I can't sit down for longer than 30 minutes."

- **Note Frequency**: If applicable, mention how often you experience the symptoms. Example: "I've been feeling nauseous almost every morning for the last ten days."

- **Consider Context**: Include any relevant information that might be related to your symptoms, such as recent travel, dietary changes, or stress.

- **List All Symptoms**: If you have more than one symptom, list all of them. The bot may be able to discern patterns or related conditions based on a full picture of your health.

### What Happens Next

- After you submit your description, the bot will analyze the information using OpenAI's GPT technology and provide you with a list of possible conditions that match your symptoms.

- The bot may ask follow-up questions to clarify certain points or get more detail. Please answer these to the best of your ability.

### Important Notes

- **This is Not a Diagnosis**: The Health Analysis Bot provides potential insights, not medical diagnoses. Only a healthcare professional can provide a diagnosis.

- **Seek Professional Advice**: If you're feeling unwell or your symptoms persist, it's important to consult with a healthcare provider.

- **Emergencies**: If you are experiencing severe symptoms or believe you have a medical emergency, seek immediate medical attention.

Thank you for using the Health Analysis Bot. We hope you find this tool helpful in understanding your health better!

--- 

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This bot is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health providers with any questions you may have regarding a medical condition.
