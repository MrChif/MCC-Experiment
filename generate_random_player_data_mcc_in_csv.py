import random
import numpy as np
import csv

from select_random_team_name import select_random_team_name

seed_columns = 8
seed_rows = random.randint(1,30)
header = ['Team','Team Placement', 'Team Coins', 'Individual Placement', 'Individual Coins', 'Gets to Dodgebolt?', 'Wins Dodgebolt?','Canonicity']
data = []

def convert_to_string(text_list):
	t_string = ''
	for i in text_list:
		t_string += '' + i
	return t_string.strip()

def select_team(item):
	team_as_list = select_random_team_name()
	item.append(convert_to_string(team_as_list))

def add_team_coins(item):
	if 7 <= item <= 10:
		data[2].append(random.randint(6000,12332))
	if 4 <= item <= 6:
		data[2].append(random.randint(12333,18665))
	if 1 <= item <= 3:
		data[2].append(random.randint(18666,25000))

def add_team_placement(item):
	item.append(random.randint(1,10))

def add_individual_coins(item):
	if 27 <= item <= 40:
		data[4].append(random.randint(300,1600))
	if 13 <= item <= 26:
		data[4].append(random.randint(1601,2900))
	if 1 <= item <= 12:
		data[4].append(random.randint(2901,4200))

def add_individual_placement(item):
	item.append(random.randint(1,40))

def dogdebolt_yes():
		data[5].append(1)
		data[6].append(random.randint(0,1))

def dodgebolt_no():
		data[5].append(0)
		data[6].append(0)

def canon(item):
	canon_options = ["Canon","Non-Canon","Half-Canon"]
	item.append(convert_to_string(random.choices(canon_options,weights=(90,7,3))))

def create_data(data,seed_rows,seed_columns):
	num_list = 0
	for item_for_data in range(seed_columns):
		item_for_data = []
		num_list += 1
		for i in range(seed_rows):
			if num_list == 1:
				select_team(item_for_data)
			if num_list == 2:
				add_team_placement(item_for_data)
			if num_list == 4:
				add_individual_placement(item_for_data)
			if num_list == 8:
				canon(item_for_data)
		data.append(item_for_data)

	for item in data[1]:
		if item == 1 or item == 2:
			dogdebolt_yes()
		else:
			dodgebolt_no()
		
	for item in data[1]:
		add_team_coins(item)

	for item in data[3]:
		add_individual_coins(item)
	

def transpose_data(data):
	data_np = np.array(data)
	data_np_t = data_np.T
	data_csv = data_np_t.tolist()
	return data_csv
	
	
def create_csv(data_csv):
	with open('../experiment_mcc/random_mcc_player_data.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(header)
		writer.writerows(data_csv)

create_data(data,seed_rows,seed_columns)
#print(data)
name_team = select_random_team_name()
print(name_team)
data_csv = transpose_data(data)
print(data_csv)
create_csv(data_csv)
#print(data)