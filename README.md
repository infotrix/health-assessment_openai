# Health Analysis Bot

This is a proof of concept for a Health Analysis Bot using OpenAI's GPT-3.5 API. It's designed to analyze a list of symptoms and provide a possible health analysis. This project is for demonstration purposes and uses synthetic data.

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

## Usage

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

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This bot is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health providers with any questions you may have regarding a medical condition.
