import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 
import re
a_tag = []
world_list =[]
clean_list =[] 
def start(url):
    
    
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code,'html.parser')
    # print(soup.find_all('a'))
    # Handling all hyperlinks
    

    for each_text in soup.find_all():
        content = each_text.text

        words= content.lower().split()

        for each_word in words:
            world_list.append(each_word)
    
    for each_tag in soup.find_all('a'):
        # print(each_tag['href'])
        corruct_link = ['javascript:void(0);','#',' ']
        if each_tag['href'] not in corruct_link:
            if each_tag['href'] not in a_tag and each_tag['href'].startswith("https://www.314e.com/") and len(a_tag)<50:
                a_tag.append(each_tag['href'])
    print(len(a_tag))
    
    clean_wordlist(world_list)

# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
	
	
	for word in wordlist: 
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
		for i in range (0, len(symbols)): 
			word = word.replace(symbols[i], '') 
			
		if len(word) > 0: 
			clean_list.append(word) 
	create_dictionary(clean_list) 

# Creates a dictionary conatining each word's 
# count and top_20 ocuuring words 
def create_dictionary(clean_list): 
	word_count = {} 
	
	for word in clean_list: 
		if word in word_count: 
			word_count[word] += 1
		else: 
			word_count[word] = 1
	c = Counter(word_count) 
	
	# returns the most occurring elements 
	top = c.most_common(10) 
	print(top) 
# Driver code 

if __name__=='__main__':
    print("Please be patience... it will take a while")
    start("https://www.314e.com/")
    print("handling all hyperlinks")
    for link in a_tag:
        start(str(link))
