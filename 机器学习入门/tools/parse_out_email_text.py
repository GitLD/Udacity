#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        # text_string = content[1].translate(str.maketrans("", ""), string.punctuation)  # Python 2 works
        text_string = content[1].translate(str.maketrans("", "", string.punctuation))  # Python 3 works

        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        text_string = text_string.replace('\r',' ')
        text_string = text_string.replace('\n',' ')
        new_word_list = []
        stemmer = SnowballStemmer('english')
        for word in text_string.split(' '):
            if word != '':
                new_word_list.append( stemmer.stem(word))
        words = ' '.join(new_word_list)




    return words

    

def main():
    ff = open("../Text Learning/test_email.txt", "r")
    text = parseOutText(ff)
    print(text)



if __name__ == '__main__':
    main()

