import nltk
import logging
import json
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Setup logging to track issues with the bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize NLTK tools
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Load intents from a JSON file (ensure the JSON file has the correct format)
def load_intents():
    try:
        with open('intents.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Error: 'intents.json' file not found.")
        return []  # Return an empty list if the file is not found

intents = load_intents()

# Preprocess user query
def process_query(query):
    tokens = word_tokenize(query.lower())
    return [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word.isalnum()]

# Stack Overflow API URL
STACK_EXCHANGE_API_URL = "https://api.stackexchange.com/2.3/search/advanced"

# Fetch answers from Stack Overflow
def get_stackoverflow_answer(query: str) -> str:
    params = {
        "q": query,
        "sort": "relevance",
        "order": "desc",
        "site": "stackoverflow",
        "pagesize": 5,
        "page": 1
    }
    try:
        response = requests.get(STACK_EXCHANGE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        
        if items:
            best_question = items[0]
            title = best_question["title"]
            link = best_question["link"]
            return f"Here is a related question on Stack Overflow: {title} - {link}"
        else:
            return "Sorry, I couldn't find a related question on Stack Overflow."
    except requests.RequestException as e:
        logging.error(f"Error fetching Stack Overflow data: {e}")
        return "Oops! There was an error fetching Stack Overflow data."

# Match user query to predefined intents
def match_intent(query):
    query_tokens = process_query(query)
    
    if not query_tokens:
        return "Your query seems empty or invalid. Please try again."
    
    best_match = None
    best_similarity = 0
    similarity_threshold = 0.3  # Set a threshold for matching intents
    
    for intent in intents:
        for pattern in intent['patterns']:
            pattern_tokens = process_query(pattern)
            
            if not pattern_tokens:
                continue

            all_tokens = list(set(query_tokens + pattern_tokens))
            query_vector = [1 if token in query_tokens else 0 for token in all_tokens]
            pattern_vector = [1 if token in pattern_tokens else 0 for token in all_tokens]
            
            similarity = cosine_similarity([query_vector], [pattern_vector])[0][0]
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = intent

    if best_match and best_similarity >= similarity_threshold:
        return best_match['responses'][0]
    else:
        return get_stackoverflow_answer(query)

# Telegram bot command and message handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I can answer your questions. Try asking me something.")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "You can ask me questions about my age, say thanks, or ask coding-related questions. For coding queries, I'll search Stack Overflow!"
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    response = match_intent(user_message)
    await update.message.reply_text(response)

# Error handler to capture and log errors
def error(update, context):
    logger.error(f'Error occurred: {context.error}')

# Define the main function to start the bot
def main():
    try:
        # Replace with your bot's token
        application = Application.builder().token("7880288980:AAFRH2ig93QbhEJHQ03Zp-tbsgpzuqEgmFE").build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Add error handler to log any issues
        application.add_error_handler(error)

        application.run_polling()

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
