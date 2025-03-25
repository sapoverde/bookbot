def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_book_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_book_words(text)
    print(f"{word_count} words found in the document")

main()