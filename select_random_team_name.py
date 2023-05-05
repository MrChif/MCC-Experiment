import numpy as np
import random

#reads file according to string, returns array with info form file#
def read_txt_file(string):
    teams_x =[]
    with open('../experiment_mcc/info/teams/'+ string,'r') as f:
        for line in f:
           teams_x.append(line)          
    return teams_x

#selects a random name according to weights
def select_random(teams_n,teams_h,teams_c):
    n_random = random.randint(0,9)
    h_random = random.randint(0,9)
    c_random = random.randint(0,9)
    chosen_list = [teams_n[n_random],teams_h[h_random],teams_c[c_random]]
    #print(chosen_list)
    return random.choices(chosen_list,weights=(80,10,10))
    
def name_to_string(name):
    string = ''
    string.join(name)

#main function from this file
def select_random_team_name():
    teams_n = read_txt_file('name_of_teams_normal.txt')
    teams_h = read_txt_file('name_of_teams_halloween.txt')
    teams_c = read_txt_file('name_of_teams_christmas.txt')
    selected_name = select_random(teams_n,teams_h,teams_c)
    name_to_string(selected_name)
    return selected_name


