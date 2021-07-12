# Second project

Create a program to implement Word Count using PySpark.

Here is an example of the result.

![result](https://github.com/SergeiSd/data-engineering-course/blob/main/Project_2/images/result.png)

---

### Prerequisites

![](https://img.shields.io/badge/Spark-3.1.1-inactivegreen) ![](https://img.shields.io/badge/PySpark-3.8.10-inactivegreen) ![](https://img.shields.io/badge/nltk.corpus-3.6.2-inactivegreen)

---

    
### Build and run 

Running a python application using "Alice in Wonderland" for word count and output the first 20 words.

    # From your project directory
    spark-submit word_count.py \
        --name_file='alice_in_wonderland.txt' \
        --num_words=20


---

### Installing

Just git clone this repo and you are good to go.
    
    # sudo apt-get install subversion
    svn export https://github.com/SergeiSd/data-engineering-course/trunk/Project_2
