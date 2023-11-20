def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' not found.")
        return None

file_name = "sample.txt"
word_count = count_words_in_file(file_name)

if word_count is not None:
    print(f"Number of words in file '{file_name}': {word_count}")