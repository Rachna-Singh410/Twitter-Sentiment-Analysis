# Twitter-Sentimant-Analysis
In present time we all are always active in social media, here I choose twitter to find the public sentiment. The reason is that the amount of relevant data is much larger for twitter, as compared to another social media sites. 

### Prerequisites

Some python libraries

---

numpy
pandas
sklearn etc.

---
### Installing

---

pip install Library_name

---


I collected four types of emotions data set i.e. Fun, Happy, Sad, Angry from different-different Google sites. 
Here in this I used Naive Bayes. It is a supervised machine learning algorithm which is based on Bayes’ theorem. First I cleaned the data remove the Nan values using dropna(), after this I removed unwanted symbols. Then I split the tweets into the words and creates the frequency table. I did this whole process for individual dataset. And after that I used dataset for training and then I tested the dataset and predict the result to give a sentences and find the result how it classify   the sentence.

### Result And Uses
I get 79% accuracy using the Naïve Bayes in my code. We can also use different machine learning algorithm in this like Random Forest, SVM etc. This project can be useful many field in today’s environment like we can use this to know about the mental state of the youth and also in a company, we can know about the user response towards the company products.     
