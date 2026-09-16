import os
import string


def count_words(filename):
    script_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(script_dir)
    search_paths = [
        os.path.join(script_dir, filename),
        os.path.join(project_root, filename),
        filename,
    ]

    for file_path in search_paths:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            break
    else:
        print(f"File not found: {filename}")
        return

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split text into words
    words = text.split()

    # Create dictionary for word count
    word_count = {}

    # Count each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Display words in alphabetical order
    print("Word Frequency:")
    for word in sorted(word_count):
        print(word, ":", word_count[word])


if __name__ == "__main__":
    count_words("simple.txt")