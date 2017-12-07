import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

foutsentiment = "/Users/alyssali/Documents/Berkeley/Classes/202/Final Project/sentiment.txt"
foutaudience = "/Users/alyssali/Documents/Berkeley/Classes/202/Final Project/audience.txt"

memeData = pd.read_csv("/Users/alyssali/Documents/Berkeley/Classes/202/Final Project/202 Dataset.csv")


def get_inverted_index(input_list):
	sentiment_dict = {}
	for v,k in enumerate(input_list):
		for value in k:
			#print('Assignging', value, v)
			new_list = sentiment_dict.get(value, set())
			new_list.add(v)
			sentiment_dict[value] = new_list
	#print('SSS', sentiment_dict)
	return sentiment_dict

def persist_to_file(text, filename ):
	fa = open(filename, 'w')
	fa.write(str(text))
	fa.close()


#tokenizing sentiment and audience 
sentiment = (memeData['Sentiment'].str.lower()).apply(nltk.word_tokenize)
audience = (memeData['Type of presentation'].str.lower()).apply(word_tokenize)
sentiment_reverse = get_inverted_index(sentiment)
audience_reverse = get_inverted_index(audience)
persist_to_file(audience_reverse, 'audience.txt')
persist_to_file(sentiment_reverse,'sentiment.txt')
print('Sentiment', sentiment_reverse)
print('Audience', audience_reverse)
