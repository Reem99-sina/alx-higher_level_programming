#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences
    sentences = []
    sentence_start = 0
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            sentences.append(text[sentence_start:i+1].strip())
            sentence_start = i + 1
    sentences.append(text[sentence_start:].strip())

    # Print the sentences with two new lines between them
    for sentence in sentences:
        print(sentence)
        print()