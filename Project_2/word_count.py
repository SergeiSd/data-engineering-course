import argparse
import os

from pyspark.sql import SparkSession
from nltk.corpus import stopwords
from typing import Union


def check_path(path: str) -> Union[str, None]:
    """A function for checking the existence of the specified file.

    Parameters
    ----------
        - path: [`str`]

        The specified path to the file.

    Returns
    -------
        class: Union[`str`, `None`]

        Returns the specified path or None if the file does not exist.
    """

    if os.path.exists(path):
        return path
    else:
        print('Error: {} file does not exist in the directory.'.format(path))
        raise argparse.ArgumentTypeError


parser = argparse.ArgumentParser()
parser.add_argument("--name_file", default="alice_in_wonderland.txt",
                    type=check_path, help="Data file name.")
parser.add_argument("--num_words", default=50, type=int,
                    help="Number of words to output the result.")
args = parser.parse_args()


def lower_clear_str(text: str) -> str:
    """A function for converting text to lowercase and
    removing punctuation characters.

    Parameters
    ----------
       - text: [`str`]

        The text received from the file.

    Returns
    -------
        class: [`str`]

        Text converted to lowercase and without punctuation characters.
    """

    punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~-'
    lowercased_str = text.lower()
    for ch in punc:
        lowercased_str = lowercased_str.replace(ch, '')

    return lowercased_str


if __name__ == "__main__":

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("WordCount") \
        .getOrCreate()

    sc = spark.sparkContext
    name_file = args.name_file
    stopwords = stopwords.words('english')

    words = sc.textFile(name_file)

    wordCounts = words.map(lower_clear_str) \
                      .flatMap(lambda text: text.split(" ")) \
                      .filter(lambda token: token != '') \
                      .filter(lambda word: word not in stopwords) \
                      . map(lambda word: (word, 1)) \
                      .reduceByKey(lambda x, y: (x + y)) \
                      .sortBy(ascending=False, keyfunc=lambda x: x[1])

    for word, count in wordCounts.take(args.num_words):
        print('{} : {}'.format(word, count))

    if not os.path.exists('wordCount'):
        wordCounts_DF = wordCounts.toDF(['word', 'count'])
        wordCounts_DF.write.json('wordCount')
