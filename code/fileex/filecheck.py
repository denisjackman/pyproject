'''
    open a file and check its contents
    https://stackabuse.com/read-a-file-line-by-line-in-python/#readafilelinebylinewithaforloopmostpythonicapproach
'''
import os
import sys


def main():
    '''
        main routine
    '''
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"File path {filepath} does not exist. Exiting...")
        sys.exit()

    bag_of_words = {}
    with open(filepath, encoding='utf-8-sig') as fp:
        for line in fp:
            record_word_cnt(line.strip().split(' '), bag_of_words)
    sorted_words = order_bag_of_words(bag_of_words, desc=True)
    print(f"Most frequent 10 words {sorted_words[:10]}")


def order_bag_of_words(bag_of_words, desc=False):
    '''
        order the bag of words by frequency
    '''
    words = list(bag_of_words.items())
    return sorted(words, key=lambda x: x[1], reverse=desc)


def record_word_cnt(words, bag_of_words):
    '''
        record the word count
    '''
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1


if __name__ == '__main__':
    main()
