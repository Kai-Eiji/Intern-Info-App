import json
import re

file = open("reddit_data_US.json")
reddit_data_list = json.load(file)

def parse_location(Str):
	data = {}
	city_state = Str.split(",")
	if len(city_state) == 2:
		data["city"] = city_state[0]
		data["state"] = city_state[1]
	else:
		data["city"] = city_state[0]

def parse_salary(salary):

	if salary != None:
		salary = salary.lower()
		rr = re.findall("(\$?\d+,?\.?\d+k?\s?)(\s?\/?\s?mo|\s?\/?\s?hr|\s?\/?\s?hour|\s?\/?\s?week)", salary)
		if rr:
			rr = rr[0]
			val = rr[0].strip(" $")
			scale = rr[1].strip(" /")
			is_k = True if "k" in val else False
			val = val.replace(",", "")
			val = val.replace("k", "")
			val = float(val)
			val = val * 1000 if is_k else val

			if "mo" in scale:
				val = val / 160
			elif "week" in scale:
				val = val / 40

			return round(val,1)
	return None

def get_housing(h):
	if h != None:
		h = h.lower()
		rr = re.findall("(\$?\d+,?\.?\d+k?\s?)(\s?\/?\s?mo)", h)
		if rr:
			rr = rr[0]
			val = rr[0].strip(" $")
			scale = rr[1].strip(" /")
			is_k = True if "k" in val else False
			val = val.replace(",", "")
			val = val.replace("k", "")
			val = float(val)
			val = val * 1000 if is_k else val
			return val
	return None

def parse_housing(h):
	h = h.lower()
	h_amount = get_housing(h)
	if h_amount != None:
		return h_amount
	elif "corp" in h or "housing provided" in h:
		return "corp housing"
	return None

def get_year(sy):
	year = ""
	if ("master" in sy) or ("grad school" in sy):
		year = "Master"
	elif ("freshman" in sy) or ("1st" in sy) or ("first" in sy):
		year = "Freshman"
	elif ("sophomore" in sy) or ("2nd" in sy) or ("second" in sy):
		year = "Sophmore"
	elif("junior" in sy) or ("3rd" in sy) or ("third" in sy):
		year = "Junior"
	elif("senior" in sy) or ("4th" in sy) or ("fourth" in sy):
		year = "Senior"
	elif("phd" in sy):
		year = "PhD"
	return year

def get_school(sy):
	school = ""
	comma_separate = sy.split(",")
	if len(comma_separate) > 2:
		for e in comma_separate:
			if ("school" in e) or ("university" in e) or ("uc" in e):
				school = e
	return school

def school_year_parser(sy):
	if sy != None:
		sy = sy.lower()
		year = ""
		school = ""
		separator = None
		comma_separate = sy.split(",")
		at_sepparate = sy.split("@")
		slash_separate = sy.split("/")

		if len(comma_separate) == 2:
			separator = comma_separate
			sy1 = get_year(comma_separate[0])
			sy2 = get_year(comma_separate[1])

			if sy1 != "":
				year = sy1
				school = comma_separate[1]
			elif sy2 != "":
				year = sy2
				school = comma_separate[0]

		elif len(at_sepparate) == 2:
			separator = at_sepparate
			sy1 = get_year(at_sepparate[0])
			sy2 = get_year(at_sepparate[1])

			if sy1 != "":
				year = sy1
				school = at_sepparate[1]
			elif sy2 != "":
				year = sy2
				school = sat_sepparate[0]

		elif len(slash_separate) == 2:
			separator = slash_separate
			sy1 = get_year(slash_separate[0])
			sy2 = get_year(slash_separate[1])

			if sy1 != "":
				year = sy1
				school = slash_separate[1]
			elif sy2 != "":
				year = sy2
				school = slash_separate[0]

		else:
			school = get_school(sy)
			year = get_year(sy)

		school = school.strip()
		year = year.strip()
		return school, year

	return None, None

clean_rd_data_list = []
for rd in reddit_data_list:
	sy = rd.get("school/year")
	salary = rd.get("salary")
	housing = rd.get("relocation/housing stipend")

	school, year = school_year_parser(sy)
	salary_clean = parse_salary(salary)
	company = rd.get("company")
	if company != None:
		company = company.strip("*")

	if housing != None:
		housing = parse_housing(housing)
		if housing == None:
			rd["housing"] = False
		elif housing == "corp housing":
			rd["housing"] = True
			rd["corp_housing"] = True
		else:
			rd["housing"] =  True
			rd["corp_housing"] = False
			rd["housing_stipend"] = housing



	if company == None or company == "" or salary_clean == None :
		pass
	else:
		rd["school"] = school
		rd["year"] = year
		rd["salary"] = salary_clean
		rd["company"] = company
		clean_rd_data_list.append(rd)

print(len(clean_rd_data_list))
with open('clean_reddit_data_US.json', 'w') as outfile:
    json.dump(clean_rd_data_list, outfile)