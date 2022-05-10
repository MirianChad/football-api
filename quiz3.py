import requests
import json
import sqlite3

conn = sqlite3.connect("football-rankings.sqlite")
cursor = conn.cursor()
#1
url = "https://api-football-v1.p.rapidapi.com/v3/standings"

querystring = {"season":"2021", "league":"140"}

headers = {
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
print(response.status_code)
print(response.headers)
print(response.headers['Content-Type'])
#3
# result_json = response.text
# res = json.loads(result_json)
# res_structured = json.dumps(res, indent=4)
# print(res_structured)
res = response.json()
#2
# with open('standings.json', 'w') as file:
# # 	json.dump(res, file, indent=4)
# team_ranking = int(input("შეიყვანეთ რიცხვი 1-დან 20მდე: "))
# print(json.dumps(res['response'][0]['league']['standings'][0][team_ranking-1], indent=4))
# ზემოთ მოცემული პრინტის საშუალებით მე გამოვიტანე ლალიგის ცხრილში გუნდის მონაცემები სეზონში რანკის ანუ ადგილის მიხედვით
#4


with open('standings.json') as file:
	res_dictionary = json.load(file)

laliga = res_dictionary['response'][0]['league']['standings'][0]
# print(laliga)

# cursor.execute('''CREATE TABLE LaLiga
# 				  (id INTEGER PRIMARY KEY AUTOINCREMENT,
# 				  Team_Name VARCHAR(20),
# 				  Points INTEGER,
# 				  Games_PLayed INTEGER,
# 				  Win INTEGER,
# 				  Draw INTEGER,
# 				  Lose INTEGER,
# 				  Goals_Scored INTEGER,
# 				  Goals_Concerned INTEGER);
# 					''')

# ცხრილში მოცემული იქნება ლალიგის 2021 წლის ცხრილი გუნდის დასახელება, ჩატარებული მატჩები, მოგება წაგება და ა.შ გუნდები დალაგებული იქნება პოზიციის მიხედვით ცხრილში 2021 წელს
list_team_names = []
list_team_points = []
list_team_played = []
list_team_win = []
list_team_draw = []
list_team_lose = []
list_team_goals_scored = []
list_team_goals_concerned = []



for each in laliga:
	list_team_names.append(each['team']['name'])
	list_team_points.append(each['points'])
	list_team_played.append(each['all']['played'])
	list_team_win.append(each['all']['win'])
	list_team_draw.append(each['all']['draw'])
	list_team_lose.append(each['all']['lose'])
	list_team_goals_scored.append(each['all']['goals']['for'])
	list_team_goals_concerned.append(each['all']['goals']['against'])





for i in range(len(list_team_names)):
	cursor.execute('''INSERT INTO LaLiga (Team_Name, Points, Games_PLayed, Win, Draw, Lose, Goals_Scored, Goals_Concerned)
					  	  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (list_team_names[i], list_team_points[i], list_team_played[i], list_team_win[i], list_team_draw[i], list_team_lose[i], list_team_goals_scored[i], list_team_goals_concerned[i]))
conn.commit()





