import tweepy, textblob

consumer_key = #put key here
consumer_secret = #put key here
access_token = #put key here
access_token_secret = #put key here
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def showTweets(inputTweets, polarityValue):
	polarityCount = 0
	tweetsCounted = 0
	for tweet in inputTweets:
		analysis = textblob.TextBlob(tweet.full_text)
		sentimentPolarity = analysis.sentiment.polarity
		if((polarityValue < 0 and sentimentPolarity <= polarityValue) or (polarityValue > 0 and sentimentPolarity >= polarityValue) or polarityValue == 0):
			tweetsCounted += 1
			polarityCount += sentimentPolarity
			print("\n" + str(tweet.full_text) + "\n" + str(analysis.sentiment))
	print('\nTotal polarity for this search: ' + str(polarityCount/(tweetsCounted+.00000001)))

def menu(inputSearch, inputTweets):
	if True:
		print('-----------------------')
		print('|  Sentiment Analyzer |')
		print('-----------------------')
		print('|A| Enter Search Terms|')
		print('|B| All Results       |')
		print('|C| Positive Results  |')
		print('|D| Negative Results  |')
		print('|Q| Quit              |')
		answer = input('-----------------------\n')

	if answer == "A" or answer == "a":
		inputSearch = input("\nWhat would you like to search for?\n")
		menu(inputSearch, inputTweets)
	elif answer == "Q" or answer ==  "q":
		exit()
	else:
		if inputSearch == "":
			print("\nSearch request was empty\n")
		else:
			includeRT = input("Include retweets? (Y/N)\n")
			if includeRT == "Y":
				inputTweets = tweepy.Cursor(api.search, q=inputSearch, lang = "en", tweet_mode="extended").items(100)
			else:
				inputTweets = tweepy.Cursor(api.search, q=(inputSearch + " -filter:retweets"), lang = "en", tweet_mode="extended").items(100)
			if answer == "B" or answer == "b":
				showTweets(inputTweets, 0)
			elif answer == "C" or answer == "c":
				showTweets(inputTweets, .5)
			elif answer == "D" or answer == "d":
				showTweets(inputTweets, -.5)
		menu(inputSearch, inputTweets)

menu("", [])