import sys
import PyPDF2

path_to_file = "books\\frankenstein.txt"




# Read file and return content
def read_text(path) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""
    

def read_pdf(path) -> str:
    try:
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()  # Extract text from each page
            return text
    except FileNotFoundError:
        print(f"Error: The PDF file at {path} was not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""
    
    

def count_words(string) -> int:
    if not string.strip():
        return 
    
    words = string.split()
    return len(words)

def count_characters(string) -> None:
    freq = {}
    string = string.lower()
    for c in string:
        if c.isalpha():
            freq[c] = freq.get(c,0) + 1
            
    return freq



# Report word and character count statistics
def report(words):
    print(f"{count_words(words)} words found in the document.")
    print()
    # count_characters(words)
    freq = count_characters(words)
    for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):  # Sort by frequency
        print(f"The character '{char}' was found {count} times.")
    
    
def get_user_input():
    print("Choose an option:")
    print("1: Enter text manually")
    print("2: Provide a text file (.txt)")
    print("3: Provide a PDF file (.pdf)")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        # Option 1: Enter text manually
        user_text = input("Enter your text here: ")
        return user_text

    elif choice == "2":
        # Option 2: Provide a text file
        file_path = input("Enter the path to the .txt file: ")
        return read_text(file_path)

    elif choice == "3":
        # Option 3: Provide a PDF file
        file_path = input("Enter the path to the .pdf file: ")
        return read_pdf(file_path)

    else:
        print("Invalid choice. Please try again.")
        return get_user_input()
        
    
    
    

if __name__ == '__main__':
    text = get_user_input()
    if text:  # If we got any text (either user input or from a file)
        report(text)
