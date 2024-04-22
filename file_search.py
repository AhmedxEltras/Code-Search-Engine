import os
import fnmatch
from difflib import SequenceMatcher

def search_files_with_wildcard(directory, tokens):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(fnmatch.fnmatch(file, token) for token in tokens):
                matches.append(os.path.join(root, file))
    return matches

def search_files_with_phrase(directory, tokens):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Only search Python files for demonstration
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if all(token in content for token in tokens):
                        matches.append(os.path.join(root, file))
    return matches

def search_files_approximate(directory, tokens):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Only search Python files for demonstration
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    similarity = SequenceMatcher(None, ' '.join(tokens), content).ratio()
                    if similarity > 0.8:  # Adjust the threshold as needed
                        matches.append(os.path.join(root, file))
    return matches
