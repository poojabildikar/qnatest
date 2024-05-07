import torch
import pandas as pd
import warnings
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Suppress FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)


model_name = "deepset/tinyroberta-squad2"

nlp = pipeline('question-answering', model=model_name,
               tokenizer=model_name)  # model and tokenization everything  is handled by pipeline

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def qa_predict(c: str, q: str) -> str:
    '''
    takes context and question as input and returns the answer by referring the trained model
    :param c: context of the question - sourced from the word file
    :param q:  question posed by the user- sourced from web interface
    :return: amswert to the question reffered from the context
    '''
    _parameter = {
        'question': q,
        'context': c

    }

    _result = nlp(_parameter)  # model prediction using pipeline
    # TODO : add model prediction using model and tokenizer

    return _result
