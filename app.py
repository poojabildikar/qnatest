from os import listdir
from os.path import isfile, join
from flask import Flask, render_template, request, jsonify
from util_handlers import process_word_files_in_folder, read_word_file,read_text_file

from qa_model import qa_predict

# Configure the app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
PROCESSED_FILES_FOLDER = 'processed_text_files'

# pre-processing the word files saved in uploads folder
process_word_files_in_folder(UPLOAD_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_name = request.form['file_name']
        question = request.form['question']
        # print(f"File name is {file_name}")
        context = read_text_file(f'{PROCESSED_FILES_FOLDER}/{file_name}.txt')
        # print(f"Question is {question}")
        # Context is content in the file

        # print(f"Context is {context}")


        # Get the answer using qa_predict function
        answer = qa_predict(context, question)
        # print(f"Answer is {answer['answer']}")

        # Pass the answer to the template for rendering
        return answer['answer']

    # Get list of files
    files = [f.rsplit('.', 1)[0] for f in listdir(PROCESSED_FILES_FOLDER) if isfile(join(PROCESSED_FILES_FOLDER, f))]
    return render_template('index.html', files=files)


if __name__ == "__main__":
    app.run(debug=False)
