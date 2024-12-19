# AskHaven - Telegram Chatbot for First-Year Students

**AskHaven** is a Telegram chatbot created to help first-year students with a variety of queries related to their college life, programming questions, and general information. AskHaven provides instant responses to common queries, helping students get quick answers for their needs.

## Features

- **General Queries**: Provides casual interactions, such as jokes, motivation, and friendly messages to help students feel at ease.
- **College FAQs (GCS)**: Answers common questions about college life, including hostel info, syllabus, student activities, etc.
- **Programming Assistance**: Helps with programming-related queries, provides tips, and assists in debugging code or solving errors.

## Usage Instructions

To start using **AskHaven**, follow these steps:

1. Open Telegram and search for **@askhaven_bot**.
2. Alternatively, click [here](https://t.me/askhaven_bot) to open the bot.
3. Type `/start` to begin interacting with the bot.
4. You can type queries, and the bot will respond based on the available intents.

### Available Commands:
- **/start**: Starts the bot and makes it ready to receive queries.

### Categories of Queries:
- **General**: Fun responses, jokes, and mood-lifting messages.
- **GCS (College FAQs)**: Information and answers about your college life and related questions.
- **Programming**: Help with programming-related queries, debugging code, and learning resources.

## Database Structure

The chatbot’s knowledge base is stored in a JSON format, which contains a collection of intents. Each intent contains:

- **tag**: A label identifying the category (e.g., "greeting", "programming").
- **patterns**: Different variations of queries that the bot will recognize as related to the same intent.
- **responses**: A list of predefined replies that the bot will randomly select when responding.

### Example of Database Structure:

```json
{
  "queries": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi", "Hey", "How are you?", "Hello", "What's up?"
      ],
      "responses": [
        "Hello! How can I assist you today?", 
        "Hey! What can I do for you?", 
        "Hi there! Feel free to ask me anything."
      ]
    },
    {
      "tag": "programming",
      "patterns": [
        "How to start programming?", 
        "What is a good resource for learning programming?", 
        "I have an error in my code. Can you help?",
        "Tell me about competitive programming.", 
        "How do I debug my code?"
      ],
      "responses": [
        "Here is a helpful guide on starting programming: [How to Start Programming](https://www.geeksforgeeks.org/how-to-start-learning-programming/).",
        "To improve in competitive programming, practice is key! Try solving problems on websites like Codeforces, LeetCode, and HackerRank.",
        "Please share your code, and I'll help you with debugging."
      ]
    },
    {
      "tag": "gcs",
      "patterns": [
        "What is the first-year syllabus?", 
        "What should I know before starting my first year?", 
        "How do I balance studies and extracurriculars?",
        "Where can I find hostel-related info?", 
        "How do I make friends in college?"
      ],
      "responses": [
        "Here is the link to the first-year syllabus: [First Year Syllabus](https://www.college.com/first-year-syllabus).",
        "Balancing studies and extracurriculars requires time management. Try organizing your schedule to make room for both!",
        "For hostel-related information, check the hostel office or visit the official portal here: [Hostel Info](https://www.college.com/hostel-info)."
      ]
    }
  ]
}


### Key Terms:
- **patterns**: Various possible ways a user may ask a question or phrase their query.
- **responses**: A set of possible responses that the bot can choose from based on the recognized intent.
- **tag**: Groups together related queries and responses under one category for easy identification.

## How It Works

1. **User Input**: A user types a message or question to the bot.
2. **Pattern Matching**: The bot compares the user's message to the patterns in its database to determine which category (intent) the query belongs to.
3. **Response Selection**: Once the intent is identified, the bot selects a random response from the associated responses for that intent.
4. **Reply**: The bot sends the chosen response back to the user.

## Installation & Setup

1. Clone this repository.
2. Install required libraries:
   ```
   pip install nltk requests python-telegram-bot
   ```
3. Run the bot:
   ```
   python bot.py
   ```

4. Ensure that the **Telegram Bot Token** is correctly added to the script. You can get your bot token by creating a new bot via the **BotFather** on Telegram.

## Future Improvements

- Expand the database to include more intents, patterns, and responses.
- Improve natural language processing capabilities for better query matching.
- Integrate additional APIs (e.g., StackOverflow, GitHub) for programming-related assistance.
- Add a machine learning model to handle more complex queries.


## Acknowledgments

- Thanks to **Telegram** for providing an excellent platform for creating bots.
- Thanks to **NLTK** for the Natural Language Processing tools used in the chatbot.

