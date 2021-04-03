import sys
from google_trans_new import google_translator  

"""
When I read books I would like to save all the highlighted single words
as a bunch of cards in my vocabulary deck in anki.
This script receives a name of a book and goes over all its
notations in the clippings.txt file and creates cards for each word of the 
following format:
    Front: Word
    Back: n/adj/v English translation
    Example in sentence
    Hebrew translation
All the translations will be taken directly from google translate.
"""


CLIPPINGS_FILE = 'clippings.txt'

SEP = '=========='

# Change it to your own native language.
TARGET_LANGUAGE = 'he'

# Configure starting line number to make our lives easier
START_LINE = 0 

if __name__ == "__main__":
    book_name = sys.argv[1]
    print("BookName: {0}".format(book_name))

    clippings_file = open(CLIPPINGS_FILE, 'r')
    file_lines = clippings_file.readlines()
    print("Number of lines: {0}".format(len(file_lines)))

    # Find lines with the given book name
    idx = START_LINE
    word_list = []
    translator = google_translator()
    while idx < len(file_lines):
        if book_name in file_lines[idx]:
            note = file_lines[idx + 3].replace('\n','')
            print("Note: {0}".format(note))
            sep_note = note.split(' ')
            print("Separated note: {0}".format(sep_note))
            if len(sep_note) == 1:
                word_list.append(sep_note[0])
            idx += 5
        else:
            idx += 1

    print("Word List: {0}".format(word_list))

    # Convert to text file that anki can import.
    with open('vocab-flashcards.txt', 'w') as flashcards_file:
        for word in word_list:
            translation = translator.translate(word, lang_tgt=TARGET_LANGUAGE)
            # translation = translation[::-1]

            card = "{0}\t{1}\n".format(word, translation)
            print(card)
            flashcards_file.write("{0}\t{1}\n".format(word, translation))
