# Assignment 2: Text Mining and Analysis

## Introduction

In this project you will learn how to use computational techniques to analyze text. Specifically, you will access text from the web and social media (such as Twitter), run some sort of computational analysis on it, and create some sort of deliverable (either some interesting results from a text analysis, a visualization of some kind, or perhaps a computer program that manipulates language in some interesting way). You will be working with a partner on this assignment. 

**Skills Emphasized**:

- Accessing information on the Internet programmatically
- Parsing text and storing it in relevant data structures
- Choosing task-appropriate data structures (e.g. dictionaries versus lists)
- Computational methods for characterizing and comparing text

## How to proceed

In order to get started on the assignment, you should fork this base repository. Once you've forked the repository, clone the repository on your computer.

You should read this document in a somewhat non-linear/spiral fashion:

1. Scan through Part 1 to get a sense of what data sources are available. Try grabbing text from one of the sources that interests you. You do not need to try all the data sources.
2. Scan through Part 2 to see a bunch of cool examples for what you can do with your text.
3. Choose (at least) one data source from Part 1 or elsewhere and analyze/manipulate/transform that text using technique(s) from Part 2 or elsewhere.
4. Write a brief document about what you did (Part 3)

### Teaming Logistics:

- You can work in a team of exactly two students or work individually.
- Your partner cannot be in the same term-project team with you.
- Only one of you should fork the base repo for this assignment. The one that forks the repo should then add the other team member as a collaborator on Github for that repo.


## Part 1: Harvesting text from the Internet

The goal for Part 1 is for you to get some text from the Internet with the aim of doing something interesting with it down the line. As you approach the assignment, I recommend that you get a feel for the types of text that you can grab using different Python packages. However, before spending too much time going down a particular path on the text acquisition component, you should look ahead to Part 2 to understand some of the things you can do with text you are harvesting. The strength of your mini project will be in combining a source of text with an appropriate technique for language analysis (see Part 2).

### Data Source: Project Gutenberg

Project Gutenberg (<http://www.gutenberg.org/>) is a website that has over 55,000 freely available e-books. In contrast to some sites, this site is 100% legal since all of these texts are no longer under copyright protection. For example, the website boasts 171 works by Charles Dickens. Perhaps the best thing about the texts on this site is that they are available in plain text format, rather than PDF which would require some additional computational processing to process in Python. 

In order to download a book from Project Gutenberg you should first use their search engine to find a link to a book that you are interested in analyzing. For instance, if I decide that I want to analyze Oliver Twist I would click on this link (<http://www.gutenberg.org/ebooks/730>) from the Gutenberg search engine. Next, I would copy the link from the portion of the page that says "Plain Text UTF-8". It turns out that the link to the text of Oliver Twist is (<http://www.gutenberg.org/ebooks/730.txt.utf-8>). To download the text inside Python, I would use the following code:

```
import urllib.request

url = 'http://www.gutenberg.org/ebooks/730.txt.utf-8'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing
```
Note, that there is a preamble (boiler plate on Project Gutenberg, table of contents, etc.) that has been added to the text that you might want to strip out (potentially using Python code) when you do your analysis (there is similar material at the end of the file). The one complication with using Project Gutenberg is that they impose a limit on how many texts you can download in a 24-hour period. So, if you are analyzing say 10 texts, you might want to download them once and load them off disk rather than fetching them off of Project Gutenberg's servers every time you run your program (see the **Pickling Data** section in session of **Files** for some relevant information on doing this). However, there are many mirrors of the Project Gutenberg site if you want to get around the download restriction.

### Data Source: Wikipedia

Another source of data that you can easily access and parse is Wikipedia. You can use wikipedia package (<https://pypi.python.org/pypi/wikipedia/>) to search Wikipedia, get article summaries, get data like links and images from a page, and more. To get this pacakge, run the following command in **Command Prompt**:

```
pip install wikipedia
```
Given that you know the particular title of the article you would like to access, you can fetch the article and then print out its sections using the following Python program:

```
import wikipedia

babson = wikipedia.page("Babson College")
print(babson.title)
print(babson.url)
print(babson.content)

```

Which yields the output:
```
Babson College 

https://en.wikipedia.org/wiki/Babson_College           

Babson College is a private business school in Wellesley, Massachusetts, established in 1919. Its central focus is on entrepreneurship education, and it is often ranked the most prestigious entrepreneurship college in the United States....
```

### Data Source: Twitter

To search Twitter, you need first create a new application in Twitter Apps(<https://apps.twitter.com/>). Then you need a Python library <code>twython</code> (another choice is <code>tweepy</code>), which you can install by running the following command in **Command Prompt**:

```
pip install twython
```
Here is a simple example for searching tweets containing <code>Patriots</code>:
```
from twython import Twython

# Replace the following strings with your own keys and secrets
TOKEN = 'Your TOKEN'
TOKEN_SECRET = 'Your TOKEN_SECRET'
CONSUMER_KEY = 'Your CONSUMER_KEY'
CONSUMER_SECRET = 'Your CONSUMER_SECRET'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Patriots", count=50)


for status in data['statuses']:
    print(status['text'])

```

When I ran this program the other day I got the following output:
```
RT @Boyd_2650: 🔴♦️MN PATRIOTS!🔴♦️The ball is in your court! It’s time to decide who you want to repres
ent your great state! Please vote 4 R…
Dodgers vs Red Sox

Rams vs Patriots

Warriors vs Celtics

@Blakepierson513 @Kinslow214 All favorites to go to ch… https://t.co/qRFgfCT9my
...
```

### Data Source: Reddit
To get reddit data, you need to install Python PRAW package by running the following command in **Command Prompt**:

```
pip install praw
```
Here's an example from the PRAW docs page (<https://praw.readthedocs.io/en/stable/getting_started/quick_start.html>):
```
import praw
import config
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)
sub = 'learnpython'
submissions = reddit.subreddit(sub).top('day', limit=5)
top5 = [(submission.title, submission.selftext) for submission in submissions]
```

### SMS Spam Collection
This collection(<http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/>) is composed by 5,574 English, real and non-enconded messages, tagged according being legitimate (ham) or spam. You can download data this link (<http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/smsspamcollection.zip>). 

### IMDB Movie Reviews
To get IMDB data, you need to install Python imdbpie package by running the following command in **Command Prompt**:
```
pip install imdbpie
```
Here's an example to print the first review of the movie 'The Dark Knight':
```
from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("The Dark Knight")[0])
reviews = imdb.get_title_user_reviews("tt0468569")

# import pprint
# pprint.pprint(reviews)

print(reviews['reviews'][0]['author']['displayName'])
print(reviews['reviews'][0]['reviewText'])

```

### More Data Sources

There are many other data sources that you can find:

- Newsfeed
- DBPedia
- Google search
- Bing search
- Enron email dataset (<https://www.cs.cmu.edu/~./enron/>)
- TripAdvisor dataset (<http://times.cs.uiuc.edu/~wang296/Data/>)
- Yelp dataset (<https://www.yelp.com/dataset_challenge>)
- News articles (<https://archive.ics.uci.edu/ml/datasets/Reuters-21578+Text+Categorization+Collection>)
- ...

### Pickling Data

For several of these data sources you might find that the API calls take a pretty long time to return, or that you run into various API limits. To deal with this, you will want to save the data that you collect from these services so that the data can be loaded back at a later point in time. Suppose you have a bunch of Project Gutenberg texts in a list called <code>charles_dickens_texts</code>. You can save this list to disk and then reload it using the following code:
```
import pickle

# Save data to a file (will be part of your data fetching script)

with open('dickens_texts.pickle','w') as f:
    pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
with open('dickens_texts.pickle','r') as input_file:
    reloaded_copy_of_texts = pickle.load(input_file)
```
The result of running this code is that all of the texts in the list variable <code>charles_dickens_texts</code> will now be in the list variable <code>reloaded_copy_of_texts</code>. In the code that you write for this project you won't want to pickle and then unpickle in the same Python script. Instead, you might want to have a script that pulls data from the web and then pickles them to disk. You can then create another program for processing the data that will read the pickle file to get the data loaded into Python so you can perform some analysis on it.


## Part 2: Analyzing Your Text

### Characterizing by Word Frequencies

One way to begin to process your text is to take each unit of text (for instance a book from Project Gutenberg, or perhaps a collection of movie reviews and summarize it by counting the number of times a particular word appears in the text. A natural way to approach this in Python would be to use a dictionary where the keys are words that appear and the values are frequencies of words in the text (if you want to do something fancier look into using TF-IDF features (<https://en.wikipedia.org/wiki/Tf%E2%80%93idf>)).

### Computing Summary Statistics
Beyond simply calculating word frequencies there are some other ways to summarize the words in a text. For instance, what are the top 10 words in each text? What are the words that appear the most in each text that don't appear in other texts? 

### Doing Natural Language Processing
NLTK - the Natural Language Toolkit (<https://www.nltk.org/>) is a leading platform for building Python programs to work with human language data. It provides some really cool natural language processing capabilities. Some examples include: part of speech tagging, sentiment analysis, and full sentence parsing. 

To use NLTK, you need to install nltk by running the following command in **Command Prompt**:

```
pip install nltk
```
Here is an example of doing sentiment analysis (<https://en.wikipedia.org/wiki/Sentiment_analysis>):
```
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
```
This program will print out:
```
{'neg': 0.0, 'neu': 0.614, 'pos': 0.386, 'compound': 0.7417}
```
If you perform some natural language processing, you may be able to say something interesting about the text you harvested from the web. For instance, if you listen to a particular Twitter hashtag on a political topic, can you gauge the mood of the country by looking at the sentiment of each tweet that comes by in the stream? Which of recent movies received most negative reviews? There are tons of cool options here!

### Text Similarity
It is potentially quite useful to be able to compute the similarity of two texts. Suppose that we have characterized some texts from Project Gutenberg using word frequency analysis. One way to compute the similarity of two texts is to test to what extent when one text has a high count for a particular word the other text also a high count for a particular word. Specifically, we can compute the cosine similarity between the two texts. This strategy involves thinking of the word counts for each text as being high-dimensional vectors where the number of dimensions is equal to the total number of unique words in your text dataset and the entry in a particular element of the vector is the count of how frequently the corresponding word appears in a specific document (if this is a bit vague and you want to try this approach, send professor an e-mail).


### Text Clustering

If you can generate pairwise similarities (say using the technique above), you can Metric Multi-dimensional Scaling (MDS) to visualize the texts in a two dimensional space. This can help identify clusters of similar texts. 

In order to apply MDS to your data, you can use the machine learning toolkit scikit-learn. Here is some code that uses the similarity matrix defined in the previous section to create a 2-dimensional embedding of the four Charles Dickens and 1 Charles Darwin texts.

```
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
    [0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
    [0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
    [0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
    [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))


plt.show()
```

This will generate the following plot. The coordinates don't have any special meaning, but the embedding tries to maintain the similarity relationships that we computed via comparing word frequencies. Keep in mind that the point labeled 4 is the work by Charles Darwin.
![text_clustering](text_clustering.png)


### Markov Text Synthesis
You can use Markov analysis to learn a generative model of the text that you collect from the web and use it to generate new texts. You can even use it to create mashups of multiple texts. One of possibilities in this space would be to to create literary mashups automatically. Again, let professor know if you go this route and we can provide more guidance.

## Part 3: Project Writeup and Reflection
Please prepare a short (suggested lengths given below) document with the following sections:

**1. Project Overview** [Maximum 100 words]
What data source(s) did you use and what technique(s) did you use analyze/process them? What did you hope to learn/create?

**2. Implementation** [~2-3 paragraphs]
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

**3. Results** [~2-3 paragraphs + figures/examples]
Present what you accomplished:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.


**4. Reflection** [~1 paragraph]
From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by task, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

## Turning in your assignment

1. Push your completed code to Github repository (depending on which team member's repository is being used to work on the project).
2. Submit your Project Writeup/Reflection (1 per team, not 1 per person). This can be in the form of either:
    + a PDF document pushed to GitHub, or
    + a project web page (if you choose this route, make sure there is a link to your web page in your `README.md` file in your Github repo.)
3. Create a pull request to the upstream repository. Learn [Creating a pull request](https://help.github.com/en/articles/creating-a-pull-request).
4. **This step is required for everyone.** Zip the entire project folder to a .zip file and submit it on Blackboard/Assignments/Assignment 2. Leave the url to your project github repository in the comment area on Blackboard.