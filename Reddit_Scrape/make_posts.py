import json
import requests

file = open("clean_reddit_data_US.json")
clean_reddit_data = json.load(file)

url = "http://127.0.0.1:8000/students/"

for rd in clean_reddit_data:
	body = {}
	body["prev_exp_num"] = -1
	if rd.get("company"):
		body["company"] = rd.get("company")

	if rd.get("salary"):
		body["salary"] = rd.get("salary")

	if rd.get("school"):
		body["university"] = rd.get("school")

	if rd.get("year"):
		body["grade_year"] = rd.get("year")

	if rd.get("city"):
		body["city"] = rd.get("city")

	if rd.get("State"):
		body["state"] = rd.get("State")

	if rd.get("housing"):
		if not rd.get("corp_housing"):
			body["housing"] = "Housing Stipend"
			body["housing_amount"] = rd.get("housing_stipend")
		else:
			body["housing"] = "Corporate Housing"

	if rd.get("comment"):
		body["comment"] = rd.get("comment")

	x = requests.post(url, data = body)
	if x.status_code > 300:
		print(x.text)
		print(rd)
		print()
		print(body)
		print()
		print()

