

import praw
import copy
import pickle
import json

url_2017_Dec = "https://www.reddit.com/r/cscareerquestions/comments/7hfrba/official_salary_sharing_thread_for_interns/"
url_2017_Sep = "https://www.reddit.com/r/cscareerquestions/comments/6xytuu/official_salary_sharing_thread_for_interns/"
url_2017_Jun = "https://www.reddit.com/r/cscareerquestions/comments/6fco6u/salary_sharing_thread_for_interns_june_2017/"

url_2018_Mar = "https://www.reddit.com/r/cscareerquestions/comments/82469b/official_salary_sharing_thread_for_interns_march/"
url_2018_Sep = "https://www.reddit.com/r/cscareerquestions/comments/9cjd6n/official_salary_sharing_thread_for_interns/"
url_2018_Jun = "https://www.reddit.com/r/cscareerquestions/comments/8ofct2/official_salary_sharing_thread_for_interns_june/"


url_2019_Mar = "https://www.reddit.com/r/cscareerquestions/comments/ax496f/official_salary_sharing_thread_for_interns_march/"
url_2019_Dec = "https://www.reddit.com/r/cscareerquestions/comments/e4ve4m/official_salary_sharing_thread_for_interns/"
url_2019_Sep = "https://www.reddit.com/r/cscareerquestions/comments/cylp5r/official_salary_sharing_thread_for_interns/"
url_2019_Jun = "https://www.reddit.com/r/cscareerquestions/comments/bw7sr3/official_salary_sharing_thread_for_interns_june/"

url_2020_Mar = "https://www.reddit.com/r/cscareerquestions/comments/fc8cp9/official_salary_sharing_thread_for_interns_march/"
url_2020_Dec = "https://www.reddit.com/r/cscareerquestions/comments/kcthwn/official_salary_sharing_thread_for_interns/"
url_2020_Sep = "https://www.reddit.com/r/cscareerquestions/comments/isfzuz/official_salary_sharing_thread_for_interns/"
url_2020_Jun = "https://www.reddit.com/r/cscareerquestions/comments/gufum4/official_salary_sharing_thread_for_interns_june/"

url_arr = [url_2020_Dec, url_2020_Sep, url_2020_Jun, url_2020_Mar, url_2019_Dec, url_2019_Sep, url_2019_Jun, url_2019_Mar, url_2018_Sep, url_2018_Jun, url_2018_Mar, url_2017_Dec, url_2017_Sep, url_2017_Jun]
reddit = praw.Reddit(client_id='Upy_aNQCt3OdhQ', client_secret='ZWXJYmrQi_R5fSrprm2g21jg03bO7w', user_agent='Reddit Web Scraping')

def parse_data(row_data):
	data_map = {}
	data_map_list = []
	lines = row_data.splitlines()
	first_company = True

	for count, line in enumerate(lines):
		if line != '' and (not "[deleted]" in line): # and any(c.isalpha() for c in line):
			#line = line.strip()
			words = line.split(":")
			#print("line", count,":", line, len(words))

			if "company" in words[0].lower() and len(words) > 1:
				if not first_company:
					data_map_list.append(data_map)
					data_map = copy.deepcopy(data_map)
				data_map["company"] = words[1]
				first_company = False

			elif "--" in words[0] or words[0] == "" or "***" in words[0] or words[0] == "&#x200B;" or words[0] == "&nbsp;":
				continue

			elif len(words) == 1 and count != len(lines)-1 and len(words[0]) <= 10:
				if not first_company:
					data_map_list.append(data_map)
					data_map = copy.deepcopy(data_map)
				data_map["company"] = words[0]
				first_company = False

			elif len(words) > 1 and words[1] == "":
				if not first_company:
					data_map_list.append(data_map)
					data_map = copy.deepcopy(data_map)
				data_map["company"] = words[0]
				first_company = False

			elif len(words) > 1:
				data_map[words[0].strip(" **").lower()] = words[1].strip("**")

			elif count == len(lines)-1 and len(words) == 1:
				data_map["comment"] = words[0]

	data_map_list.append(data_map)

	if len(data_map.keys()) > 0:
		return data_map_list
	else:
		return None




row_data = []
data_map_list = []

for url in url_arr:
	submission = reddit.submission(url=url)
	submission.comments.replace_more(limit=0)
	for top_level_comment in submission.comments:
		
		if ("Region - **US High CoL**" in top_level_comment.body) or ("Region - **US Medium CoL**" in top_level_comment.body) or ("Region - **US Low CoL**" in top_level_comment.body):
		    for second_level_comment in top_level_comment.replies:
		    	
		    	sub_list = parse_data(second_level_comment.body)
		    	if sub_list != None:
		    		data_map_list += parse_data(second_level_comment.body)
    	

with open('reddit_data_US.json', 'w') as outfile:
    json.dump(data_map_list, outfile)
        
print(len(data_map_list))



