def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
       print(f"Error: File '{filepath}' not found.")
    except Exception as e:
       print(f"Error: {e}")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_dictionary(text):
    char_dict = []
    char_count = {}
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            char = char.lower()  # Normalize to lowercase
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for char, count in char_count.items():
        char_dict.append({"char": char, "num": count})
    return char_dict

def sort_on(dict):
    return dict["num"]

def print_report(filename):
    text = get_book_text(filename)
    char_dict = get_character_dictionary(text)
    char_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    for item in char_dict:
        char, num = item.values()
        print(f"{char}: {num}")
    print("============= END ===============")
