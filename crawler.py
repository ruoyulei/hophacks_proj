# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import cookielib
import lxml
import string
import requests
import subprocess
import youtube_v
import pyttsx
import process_call

s = set([''])
limit = 90
arr = []
short_page_number = 1
engine = pyttsx.init()


def main():
	page_reenter = False
	process_call.read_text("Welcome to Soundi. What would you like to search?")
	print 'What do you want to search?'

	init = raw_input()
	init = string.replace(init, ' ', '+')
	init_url = 'https://www.youtube.com/results?search_query='+init+'&page='
	page_number = 1
	while(page_number < 3):
		url = init_url + str(page_number)
		html_doc = pull_webpage(url)
		try:
			soup = get_soup(html_doc)
		except:
			return
		crawler2(soup)
		page_number = page_number + 1

	addition = 0
	while(True):
		if page_reenter == False:
			process_call.read_text("You are currently on page "+str(short_page_number + addition))
			process_call.read_text("Videos on this page are  ")
			print_list(short_page_number + addition)
			page_reenter = True

		'''
		url = init_url + page_number
		s.add(url)
		html_doc = pull_webpage(url)
		try:
			soup = get_soup(html_doc)
		except:
			return
		crawler2(soup)
		print_list()

		get_max_and_min(url)
		temp_set = set([])
		for n in range(int(min_number),int(max_number)+1):
			print n,
			temp_set.add(n)
		print '\nenter a page number or \'leave\': '
		'''
		process_call.read_text("Press W to watch video, N for next page, P for previous page, or Q to quit")
		print '\nPress N, P or Q: '
		typein = raw_input()
		'''
		if str(typein).isdigit():
			if (int(typein) in temp_set):
				print 'go to page number',int(typein)
				# page_number = str(typein)
			else:
				print 'invalid number'
				break
		'''
		if str(typein).lower() == "q":
			process_call.read_text("Thanks for using. Have a nice day")
			print 'Thanks for using. Have a nice day'
			break
		elif str(typein).lower()[:1] == "w" and str(typein)[1] == " ":
			if len(typein) == 3:
				# print "watching",typein[2]
				watch_video(short_page_number + addition, int(typein[2]))
				page_reenter = True
				#break
			elif len(typein) == 4:
				# print "watching",int(typein[2]+typein[3])
				watch_video(short_page_number + addition,int(typein[2]+typein[3]))
				page_reenter = True
				#break
		elif str(typein).lower()[:1] == "n":
			addition = addition + 1
		elif str(typein).lower()[:1] == "p":
			if short_page_number + addition > 1:
				addition = addition - 1
		else:
			print 'invalid command'
			break

def chunks(arr,number):
	for i in xrange(0,len(arr), number):
		yield arr[i:i+number]

def print_list(num):
	bottom = (num - 1) * 5
	top = 1
	if (num * 5 -1) < len(arr):
		top = num * 5
	else:
		top = len(arr)

	counter = 1
	for i in range(bottom,top):
		print (str(counter)+".").ljust(3),arr[i].title
		process_call.read_text(str(counter))
		temp_str = ""
		for character in arr[i].title:
			if ord(character) not in range(48,57) and ord(character) not in range(65,90) and ord(character) not in range(97,122):
				temp_str+=" "
			else:
				temp_str+=character
		process_call.read_text(temp_str)
		counter = counter + 1

def watch_video(curr_page,num):
	v_id = arr[curr_page*5 - 6 + num].id
	subprocess.call(["bash","a.sh",v_id,"&>","/dev/null"])
	#subprocess.call(str, shell=True)

def get_soup(html_doc):
	return BeautifulSoup(html_doc, 'lxml')

def get_max_and_min(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	 
	# An iterable is a list
	pages = list()
	 
	# We get the main div where the next/previous stuff happens
	main_div = soup.find_all('div', {'class': 'spf-link' })[0]
	 
	# let's scan for all the links in the div
	for links in main_div.find_all('a'):
	    # let's try
	    try:
	        # We add the entry to the pages list
	        pages.append(int(links.text.encode('utf-8')))
	    except:
	        continue

	global max_number
	max_number = max(pages)
	# print 'max is', max_number
	global min_number
	min_number = min(pages)
	# print 'min is',min_number

def crawler(soup):
	# DOM:
	# class -> yt-lockup-title -- a -> herf(/watch?v=id)
	for links in soup.find_all('data-page'):
		print links.a['href']

	index = 0
	for head in soup.find_all('h3', 'yt-lockup-title '):
		y_id = ""
		print str(index)+'.',
		for sub in head.find_all('a'):
			y_id = sub.get('href')
			y_id = string.replace(y_id, '/watch?v=', '', 1)
			print sub.get_text().encode('utf-8')

		for sub2 in head.find_all('span'):
			duration = sub2.get_text().encode('utf-8')
			if "Channel" in duration:
				duration = "Channel"
			else:
				duration = string.replace(duration, ' - Duration: ', '',1)
				duration = string.replace(duration, '.', '',1)
				duration = duration.ljust(8)
			print "   "+duration,"|",y_id
		index = index + 1

def crawler2(soup):
	for links in soup.find_all('data-page'):
		print links.a['href']
	
	sub_set = []
	#index = 0
	for head in soup.find_all('h3', 'yt-lockup-title '):
		y_id = ""
		title = ""
		# index
		# print str(index)+'.',
		for sub in head.find_all('a'):
			y_id = sub.get('href')
			y_id = string.replace(y_id, '/watch?v=', '', 1)
			# title
			title = sub.get_text().encode('utf-8')
			# print sub.get_text().encode('utf-8')

		for sub2 in head.find_all('span'):
			duration = sub2.get_text().encode('utf-8')
			if "Channel" in duration:
				duration = "Channel"
			else:
				duration = string.replace(duration, ' - Duration: ', '',1)
				duration = string.replace(duration, '.', '',1)
				duration = duration.ljust(8)
			# duration
			# | y_id
			# print "   "+duration,"|",y_id
		a = youtube_v.youtube_v()
		a.make_instance(title,y_id)
		# sub_set.append(a)
		#index = index + 1
		arr.append(a)
	#arr.append(sub_set)

def pull_webpage(url):
	# requests.get(address)
	# request = request.text

	# for foo in enumerate(bar)
	# for a, foo in enumerate(bar)

	# print 'start running request and urllib2...'
	try:
		request = urllib2.Request(url)
		response2 = urllib2.urlopen(request)
		if response2.getcode() == 200:
			# print 'works fine...'
			x = response2.read()
			return x
		else:
			print 'not working properly!'
	except:
		print 'no internet connection'
		return 
	# request.add_header('user-agent', 'Nexus7')
	
	

if __name__ == '__main__':
	main()