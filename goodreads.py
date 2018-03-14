# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

#quote_page = 'https://www.goodreads.com/book/show/26892110-the-library-at-mount-char'
#page = urlopen(quote_page)
#soup = BeautifulSoup(page, 'html.parser')
#
#aver_rating = soup.find('span', attrs={'class': 'average'})
#aver_rating = aver_rating.string.strip()
#print(aver_rating)
#
#num_rating = soup.find('span', attrs={'class': 'votes value-title'})
#num_rating = num_rating.string.strip()
#print(num_rating)
#
#review_star = soup.find('div', attrs={'class': 'review'})
#
#genre1 = soup.find('a', attrs={'class': 'actionLinkLite bookPageGenreLink'})
#genre1 = genre1.string.strip()
#print(genre1)

shelf = pd.read_csv("C:/Users/smytmc/Desktop/goodreads_library_export.csv")
shelf["Genre"] = ""

#tester = shelf.iloc[[1,5,15,20,23,29,51,61,71,82]]
#tester["Genre"] = ""

for i in range(len(shelf)-1):
    quote_page = 'https://www.goodreads.com/book/show/' + str(shelf.iloc[i,0]) 
    page = urlopen(quote_page)
    read_soup = BeautifulSoup(page, 'html.parser')
    genre1 = read_soup.find('a', attrs={'class': 'actionLinkLite bookPageGenreLink'})
    shelf.iloc[i,31] = genre1.string.strip()
    time.sleep(0.5)

shelf.to_csv("C:/Users/smytmc/Desktop/goodreads_genre.csv")
