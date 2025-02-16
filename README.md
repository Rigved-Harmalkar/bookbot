
---

# Bookbot

This is a simple Python program that allows users to analyze the text content from either a manually entered string or a file. The program can read `.txt` files or `.pdf` files, and it performs two types of analyses:

1. **Word Count**: The total number of words in the document.
2. **Character Frequency Count**: The frequency of each alphabetical character in the document, sorted in descending order.

## Features:
- Option to enter text manually.
- Option to provide a `.txt` file to extract text.
- Option to provide a `.pdf` file and extract text from it.
- Counts the number of words in the document.
- Counts the frequency of each alphabetical character in the document, sorted by frequency.

## Requirements:
- Python 3.x
- **PyPDF2** (for PDF file reading)

### Installation Instructions:
1. Make sure you have Python 3.x installed on your system.
2. Install the required dependency (`PyPDF2`) by running the following command:

   ```bash
   pip install PyPDF2
   ```

## How to Use:
### Running the Program:
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the Python script using:

   ```bash
   python text_analysis.py
   ```

4. You will be prompted to choose an input method:
   - **1**: Enter text manually.
   - **2**: Provide a `.txt` file by entering its path.
   - **3**: Provide a `.pdf` file by entering its path.

### Example:

1. **Option 1**: Enter text manually:
   ```bash
   Choose an option:
   1: Enter text manually
   2: Provide a text file (.txt)
   3: Provide a PDF file (.pdf)
   Enter your choice (1, 2, or 3): 1
   Enter your text here: Hello world! This is a test.
   ```

   Output:
   ```
   6 words found in the document.

   The character 'l' was found 3 times.
   The character 'o' was found 2 times.
   The character 'h' was found 1 time.
   The character 'e' was found 1 time.
   The character 'w' was found 1 time.
   The character 'r' was found 1 time.
   The character 'd' was found 1 time.
   The character 'i' was found 1 time.
   The character 's' was found 1 time.
   'a' found 1 time.
   't' found 1 time.
   ```

2. **Option 2**: Provide a `.txt` file:
   ```bash
   Enter the path to the .txt file: books\\frankenstein.txt
   ```

3. **Option 3**: Provide a `.pdf` file:
   ```bash
   Enter the path to the .pdf file: books\\frankenstein.pdf
   ```

## Functionality Overview:
1. **`read_text(path)`**: Reads a text file and returns the content as a string. If the file is not found, an error message is displayed.
2. **`read_pdf(path)`**: Reads a PDF file and extracts the text from each page, returning the extracted content as a string. If the file is not found or another error occurs, an error message is displayed.
3. **`count_words(string)`**: Counts the number of words in the provided string.
4. **`count_characters(string)`**: Counts the frequency of each alphabetical character (ignores non-alphabetical characters) in the provided string.
5. **`report(words)`**: Generates the word count and character frequency report.
6. **`get_user_input()`**: Prompts the user to choose between entering text, uploading a `.txt` file, or uploading a `.pdf` file.


## Contributions:
Feel free to fork this project, make improvements, and submit pull requests. If you encounter any bugs or have suggestions, please open an issue!

---
