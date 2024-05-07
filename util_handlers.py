import os
from docx import Document


# Function to read a Word file and return its content as a string
def read_word_file(file_path):
    # Open the Word document
    doc = Document(file_path)
    content = []
    # Iterate over each paragraph in the document
    for para in doc.paragraphs:
        # Add a full stop at the end of the paragraph if it doesn't exist
        text = para.text if para.text.endswith('.') else para.text + '.'
        content.append(text)
    # Join all the paragraphs with a newline character and return the result
    return '\n'.join(content)


# Function to save a string as a text file
def save_as_text_file(content, filename):
    # Open a new text file in write mode
    with open(f'processed_text_files/{filename}.txt', 'w', encoding='utf-8') as f:
        # Write the content to the file
        f.write(content)


# Function  to read Text file
def read_text_file(file_path: str) -> str:
    """
    Read and return the contents of a text file.
    :param file_path: Path to the text file.
    :return: Contents of the text file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Function to process all Word files in a given folder
def process_word_files_in_folder(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a Word document
        if filename.endswith('.docx') or filename.endswith('.doc'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            # Read the content of the Word file
            content = read_word_file(file_path)
            # Save the content as a text file
            save_as_text_file(content, filename.rsplit('.', 1)[0])

# path to the folder containing the Word files
# path_to_your_folder = 'data'

# process all Word files in the folder
# process_word_files_in_folder(path_to_your_folder)
