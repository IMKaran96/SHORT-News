from django.shortcuts import render
from newsapi import NewsApiClient
import pycountry

# Create your views here.
import requests
def NewsFetch(request):
	parameters = {"source": "bbc-news","sortBy": "top","apiKey": "137748f9ac4f4f7ca5e9f07c42a01db6"}
	url = "https://newsapi.org/v1/articles"
	response = requests.get(url, params=parameters)
	page = response.json()
	
	article = page["articles"]
	
	title=[]
	description=[]
	image=[]
	newsurl=[]
	
	for news in article:
		title.append(news["title"])
		description.append(news["description"])
		image.append(news["urlToImage"])
		newsurl.append(news["url"])
		
	mylist=zip(title, description, image, newsurl)
	
	return render(request, 'NewsUI.html', context ={"mylist":mylist})
def Category(request, item):
	newsapi = NewsApiClient(api_key='137748f9ac4f4f7ca5e9f07c42a01db6')
	top_headlines = newsapi.get_top_headlines(category=f'{item.lower()}')
	article = top_headlines['articles']
	title=[]
	description=[]
	image=[]
	newsurl=[]
	for news in article:
		title.append(news["title"])
		description.append(news["description"])
		image.append(news["urlToImage"])
		newsurl.append(news["url"])
		
	mylist=zip(title, description, image, newsurl)
	
	return render(request, 'NewsUI.html', context ={"mylist":mylist})
def Country(request, countryName):
	countries={"Argentina":"AR","Australia":"AU","Belgium":"BE","Canada":"CA","Denmark":"DK","France":"FR","India":"IN","Japan":"JP"}
	newsapi = NewsApiClient(api_key='137748f9ac4f4f7ca5e9f07c42a01db6')
	top_headlines = newsapi.get_top_headlines(country=f'{countries[countryName].lower()}')
	article = top_headlines['articles']
	title=[]
	description=[]
	image=[]
	newsurl=[]
	for news in article:
		title.append(news["title"])
		description.append(news["description"])
		image.append(news["urlToImage"])
		newsurl.append(news["url"])
		
	mylist=zip(title, description, image, newsurl)
	
	return render(request, 'NewsUI.html', context ={"mylist":mylist})
