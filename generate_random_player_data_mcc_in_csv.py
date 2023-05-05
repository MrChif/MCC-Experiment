import random
import numpy as np
import csv

from select_random_team_name import select_random_team_name

seed_columns = 6
seed_rows = random.randint(1,25)
header = ['Team Placement', 'Team Coins', 'Individual Placement', 'Individual Coins', 'Gets to Dodgebolt?', 'Wins Dodgebolt?']
data = []

def add_team_coins(item):
	if 7 <= item <= 10:
		data[1].append(random.randint(6000,12332))
	if 4 <= item <= 6:
		data[1].append(random.randint(12333,18665))
	if 1 <= item <= 3:
		data[1].append(random.randint(18666,25000))


def add_team_placement(item):
	item.append(random.randint(1,10))

def add_individual_coins(item):
	if 27 <= item <= 40:
		data[3].append(random.randint(300,1600))
	if 13 <= item <= 26:
		data[3].append(random.randint(1601,2900))
	if 1 <= item <= 12:
		data[3].append(random.randint(2901,4200))

def add_individual_placement(item):
	item.append(random.randint(1,40))

def dogdebolt_yes():
		data[4].append(1)
		data[5].append(random.randint(0,1))

def dodgebolt_no():
		data[4].append(0)
		data[5].append(0)

def create_data(data,seed_rows,seed_columns):
	num_list = 0
	for item_for_data in range(seed_columns):
		item_for_data = []
		num_list += 1
		for i in range(seed_rows):
			if num_list == 1:
				add_team_placement(item_for_data)
			if num_list == 3:
				add_individual_placement(item_for_data)
		data.append(item_for_data)

	for item in data[0]:
		if item == 1 or item == 2:
			dogdebolt_yes()
		else:
			dodgebolt_no()
		
	for item in data[0]:
		add_team_coins(item)

	for item in data[2]:
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