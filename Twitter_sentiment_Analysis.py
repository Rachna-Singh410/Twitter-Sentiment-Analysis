import pandas as pd
import string
from sklearn.model_selection import train_test_split
 #for first dataset 
df = pd.read_csv('E:/project4/Unsmile.csv')
df = df.dropna(axis=0, how = 'any')
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

df['text'] = df['text'].apply(removetext)
df['text'] = df['text'].apply(lambda x: x.lower())
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
array = df['text'].str.split(' ', expand=True).stack().value_counts()
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)
df2['frequency'] = df2['frequency'][df2['frequency'] > 10] 
df2 = df2.dropna(axis=0, how = 'any')
df2 = df2.drop([':(','https://t',':((', ':(((', ':((((', ':(((((', ':', '(', ''])
df2.to_csv('E:/project4/Unsmile_words.csv', header=True, index=False, encoding='utf-8')
df['text']= df['text'].str.split()
df.to_csv('E:/project4/Unsmile_split.csv')
#for second dataset 
df = pd.read_csv('E:/project4/Sad.csv')
df = df.dropna(axis=0, how = 'any')
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

df['text'] = df['text'].apply(removetext)
df['text'] = df['text'].apply(lambda x: x.lower())
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
array = df['text'].str.split(' ', expand=True).stack().value_counts()
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)
df2['frequency'] = df2['frequency'][df2['frequency'] > 10] 
df2 = df2.dropna(axis=0, how = 'any')
df2.to_csv('E:/project4/Sad_words.csv', header=True, index=False, encoding='utf-8')
df['text']= df['text'].str.split()
df.to_csv('E:/project4/Sad_split.csv')
#for third dataset 
df = pd.read_csv('E:/project4/Happie.csv')
df = df.dropna(axis=0, how = 'any')
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])
df['text'] = df['text'].apply(removetext)
df['text'] = df['text'].apply(lambda x: x.lower())
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
array = df['text'].str.split(' ', expand=True).stack().value_counts()
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)
df2['frequency'] = df2['frequency'][df2['frequency'] > 10] 

df2 = df2.dropna(axis=0, how = 'any')
df2 = df2.drop([':(','https://t',':((', ':(((', ':((((', ':(((((', ':', '(', ''])
df2.to_csv('E:/project4/Happie_words.csv', header=True, index=False, encoding='utf-8')
df['text']= df['text'].str.split()
df.to_csv('E:/project4/Happie_split.csv')
#for fourth dataset 
df = pd.read_csv('E:/project4/Funny.csv')
df = df.dropna(axis=0, how = 'any')
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])
df['text'] = df['text'].apply(removetext)
df['text'] = df['text'].apply(lambda x: x.lower())
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
array = df['text'].str.split(' ', expand=True).stack().value_counts()
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)
df2['frequency'] = df2['frequency'][df2['frequency'] > 10] 
df2 = df2.dropna(axis=0, how = 'any')
df2 = df2.drop([':(','https://t',':((', ':(((', ':((((', ':(((((', ':', '(', ''])
df2.to_csv('E:/project4/Funny_words.csv', header=True, index=False, encoding='utf-8')
df['text']= df['text'].str.split()
df.to_csv('E:/project4/Funny_split.csv')
happy = pd.read_csv('E:/project4/Happie_words.csv')
sad = pd.read_csv('E:/project4/Sad_words.csv')
unsmile = pd.read_csv('E:/project4/Unsmile_words.csv')
fun = pd.read_csv('E:/project4/Funny_words.csv')
wordbag = pd.concat([happy,sad,unsmile,fun]).drop_duplicates(subset = 'word').reset_index(drop=True)
wordbag.to_csv('E:/project4/Wordbag.csv')

fun = pd.read_csv('E:/project4/Funny_split.csv')
happy = pd.read_csv('E:/project4/Happie_split.csv')
unsmile = pd.read_csv('E:/project4/Unsmile_split.csv')
sad = pd.read_csv('E:/project4/Sad_split.csv')
wordbag = pd.read_csv('E:/project4/Wordbag.csv')
wordbag = wordbag.drop_duplicates()
fun['type'] = 1
happy['type'] = 1
unsmile['type'] = 0
sad['type'] = 0
df = pd.concat([happy,sad,unsmile,fun]).reset_index(drop=True)
train, test = train_test_split(df, test_size=0.2)
train_positive = train[train['type'] ==1]
train_negative = train[train['type'] ==0]
positive_instance = len(train_positive)
negative_instance = len(train_negative)
print(positive_instance)
print(negative_instance)
frequency = wordbag['word']
word_bank = [0]*len(frequency)
positive = [0]*len(frequency)
negative = [0]*len(frequency)
for i in range(len(frequency)):
    word = frequency.iloc[i]
    word_bank[i] = word
    check = str("'") + word + str("'")
    count = 0  
    for j in range(len(train_positive)):
        appears = train_positive['text'].iloc[j].count(check)
        if appears > 0:
            count = count + 1
    positive[i] = count
    count = 0  
    for k in range(len(train_negative)):
        appears = train_negative['text'].iloc[k].count(check)
        if appears > 0:
            count = count + 1
    negative[i] = count
    print(i)

d = {'word': word_bank, 'positive': positive, 'negative': negative}
ftable = pd.DataFrame(data = d)

ftable.to_csv('E:/project4/stable.csv')
print(positive_instance)
print(negative_instance)
ftable = pd.read_csv('E:/project4/stable.csv')
test ='i am happy'
positive_instance = 24007.0
negative_instance = 23993.0
test_words = test.split()
prob_positive = float(positive_instance/(positive_instance+negative_instance))
prob_negative = 1 - prob_positive
pos_word = 1.0*prob_positive
neg_word = 1.0*prob_negative
for i in range(len(test_words)):
    word = test_words[i]
    print(word)
    index_val = ftable.index[ftable['word'] == word]
    if (len(index_val) > 0):
        pos_val = ftable['positive'].iloc[index_val[0]]
        neg_val = ftable['negative'].iloc[index_val[0]]
        pos_word = pos_word * pos_val/positive_instance
        neg_word = neg_word * neg_val/negative_instance
        
        
if pos_word > neg_word:
    print("The sentence was POSITIVE, with a probability of")
    print(pos_word/(pos_word+neg_word))
else:
    print("The sentence was NEGATIVE, with a probability of")
    print(neg_word/(pos_word+neg_word))

