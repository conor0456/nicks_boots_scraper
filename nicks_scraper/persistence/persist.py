import csv
import os
import json 
from pathlib import Path

delimitter = "%:%"
dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '..','..', 'previous_data.txt')

def write_array(data):
	f = open(file_path, "w")
	f.write(delimitter.join(data))
	f.close()
	
def read_array():
	if os.path.isfile(file_path):
		file = open(file_path, "r")
		string = file.read().strip()
		return string.split(delimitter)
		
	else:
		return []

def get_new_entries(new_data):
	old_data = read_array()
	write_array(new_data)
	return list(set(new_data).difference(old_data))
