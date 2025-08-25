# utils.py
import re

def match_pattern(user_input, knowledge_base):
    for entry in knowledge_base:
        pattern = entry['pattern'].replace("*", "(.*)")
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = entry['response']
            # Replace placeholders with captured groups
            for i, group in enumerate(match.groups()):
                response = response.replace(f"{{{i}}}", group)
                response = response.replace("{time}", group)
                response = response.replace("{location}", group)
            return response
    return "Sorry, I don't understand that."
