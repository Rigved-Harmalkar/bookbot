import sys


path_to_file = "books\\frankenstein.txt"




# Read file and return content
def read_text(path) -> str:
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
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
    
    
        
        
    
    
    

if __name__ == '__main__':
    words = read_text(path_to_file)
    if words:
        report(words)
