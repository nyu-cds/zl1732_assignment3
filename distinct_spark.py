from pyspark import SparkContext
import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
    sc = SparkContext("local", "wordcount")

    text = sc.textFile('pg2701.txt')
    words = text.flatMap(splitter)
    words_mapped = words.map(lambda x: (x,1)).reduceByKey(lambda x,y : x+y).count()
    print(words_mapped)