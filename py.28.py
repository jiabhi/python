#input a dictionary file and print all unique words

def print_unique_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read().lower()
        words = text.split()
        unique_words = set(words)
        print("Unique words:", unique_words)
        print("Number of unique words:", len(unique_words))

# Example usage:
print_unique_words("file1.txt")