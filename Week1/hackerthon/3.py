#3.Intelligent Log "Anomalizer"
import re
from collections import Counter

log_file_path = "log.txt"

try:
    with open(log_file_path, "r") as f:
        lines = f.readlines()

    words = []
    for line in lines:
        words.extend(re.findall(r"\b\w+\b", line.lower()))

    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    threshold = total_words*0.01

    rare_words = {word for word,count in word_counts.items() if count < threshold}

    print(f"Total unique words: {total_words}")
    print(f"Rare words: {len(rare_words)} found")

    print("\nLines flagged with rare words:")
    for line in lines:
        if any(word.lower() in rare_words for word in re.findall(r"\b\w+\b", line)):
            print(f"{line} IS FLAGGED.")

except FileNotFoundError:
    print(f"File not found!")
except Exception as e:
    print(f"An error has occurred!")