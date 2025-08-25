# assistant.py
import csv
import re
from api_integration import get_weather, set_reminder
from utils import match_pattern

# Load knowledge base
knowledge_base = []
with open("data/knowledge_base.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        knowledge_base.append(row)

def chat():
    print("Virtual AI Assistant (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Assistant: Goodbye!")
            break

        response = match_pattern(user_input, knowledge_base)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    chat()
