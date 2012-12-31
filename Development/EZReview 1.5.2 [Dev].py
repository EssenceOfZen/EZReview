#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  EZReview.py
#  
#  Copyright 2012 ZenOokami <zenookami@hotmail.com> https://www.essenceofzen.tk/
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
print("#=======================================#")
print("#            ZenOokami Codes            #")
print("#        http://EssenceOfZen.tk         #")
print("#=======================================#")
print("#          ~    /| ZEN |\   ~           #")
print("#              / |_____| \              #")
print("#             |           |             #")
print("#             |  __   __  |             #")
print("#             <  \/   \/  >             #")
print("#              <         >              #")
print("#                \  v  /                #")
print("#                 \___/                 #")
print("#           `~-::Ookami*::-~`           #")
print("#=======================================#")
print("# _____ _            _    _       _  __ #")
print("#|_   _| |          | |  | |     | |/ _|#")
print("#  | | | |__   ___  | |  | | ___ | | |_ #")
print("#  | | | '_ \ / _ \ | |/\| |/ _ \| |  _|#")
print("#  | | | | | |  __/ \  /\  / (_) | | |  #")
print("#  \_/ |_| |_|\___|  \/  \/ \___/|_|_|  #")
print("#=======================================#")

import time
import datetime
#================================
#Global Variables
#================================
today = ""
version = "1.0.0"


user_choice = 0
switch = 0

file_name = ""
app_name = ""
reviewer = ""

usability = 0
reliability = 0 
asthetics = 0 #The look of the app
quality = 0
tilt = 0

score = 0

description = ""

pros = ""
cons = ""


final_opinion = ""

def calculate_score(usability, reliability, asthetics, quality, tilt):
	score = (usability + reliability + asthetics + quality + tilt) / 5
	
	return score

def current_date():
	today = time.asctime(time.localtime(time.time()))
	
	return today
	
def name_file():
	file_name = input("Please input Title: ")
	print("The name of the file has been set to: " + str(file_name))
	
	return file_name
	
def name_app():
	app_name = input("Please input name of application: ")
	
	return app_name
	
def rate_usability():
	switch = 1
	while switch == 1:
		usability = float(input("Please input Usability score: "))
		if usability < 0 or usability > 5:
			print("Invalid input, score must be 0 to 5.")
		else:
			switch = 0
			
	return usability

def rate_reliability():
	switch = 1
	while switch == 1:
		reliability = float(input("Please input Reliability score: "))
		if reliability < 0 or reliability > 5:
			print("Invalid input, score must be 0 to 5.")
		else:
			switch = 0
			
	return reliability
	
def rate_asthetics():
	switch = 1
	while switch == 1:
		asthetics = float(input("Please input Asthetics score: "))
		if asthetics < 0 or asthetics > 5:
			print("Invalid input, score must be 0 to 5.")
		else:
			switch = 0
			
	return asthetics
	
def rate_quality():
	switch = 1
	while switch == 1:
		quality = float(input("Please input Quality score: "))
		if quality < 0 or quality > 5:
			print("Invalid input, score must be 0 to 5.")
		else:
			switch = 0
			
	return quality
	
def set_tilt():
	switch = 1
	while switch == 1:
		tilt = float(input("Please input your Tilt score: "))
		if tilt < 0 or tilt > 5:
			print("Invalid input, score must be 0 to 5.")
		else:
			switch = 0
			
	return tilt

def set_description():
	description = input("Please describe your interaction with the app: ")
	
	return description
	
def set_pros():
	pros = input("What are the pros of this application?: ")
	
	return pros
	
def set_cons():
	cons = input("What are the cons of this application?: ")
	
	return cons

def set_reviewer():
	reviewer = input("Who is reviewing this program?: ")
	
	return reviewer

def write_to_text_file(today, file_name, app_name, usability, reliability, asthetics, quality, tilt, score, pros, cons, description, reviewer):
	text_file = open(file_name + ".txt", "w")
	text_file.write("#=======================================#\n")
	text_file.write("#            ZenOokami Codes            #\n")
	text_file.write("#        http://EssenceOfZen.tk         #\n")
	text_file.write("#=======================================#\n")
	text_file.write("#          ~    /| ZEN |\   ~           #\n")
	text_file.write("#              / |_____| \              #\n")
	text_file.write("#             |           |             #\n")
	text_file.write("#             |  __   __  |             #\n")
	text_file.write("#             <  \/   \/  >             #\n")
	text_file.write("#              <         >              #\n")
	text_file.write("#                \  v  /                #\n")
	text_file.write("#                 \___/                 #\n")
	text_file.write("#           `~-::Ookami*::-~`           #\n")
	text_file.write("#=======================================#\n")
	text_file.write("# _____ _            _    _       _  __ #\n")
	text_file.write("#|_   _| |          | |  | |     | |/ _|#\n")
	text_file.write("#  | | | |__   ___  | |  | | ___ | | |_ #\n")
	text_file.write("#  | | | '_ \ / _ \ | |/\| |/ _ \| |  _|#\n")
	text_file.write("#  | | | | | |  __/ \  /\  / (_) | | |  #\n")
	text_file.write("#  \_/ |_| |_|\___|  \/  \/ \___/|_|_|  #\n")
	text_file.write("#=======================================#\n")
	text_file.write("This Text document was created through Essence of Zen \"EZReview Program\". \n")
	text_file.write("\n")
	text_file.write("Application: " + app_name + "\n")
	text_file.write("Reviewed by: " + str(reviewer) + "\n")
	text_file.write("\n")
	text_file.write("Usability: " + str(usability) + "\n")
	text_file.write("Reliability: " + str(reliability) + "\n")
	text_file.write("Asthetics: " + str(asthetics) + "\n")
	text_file.write("Quality: " + str(quality) + "\n")
	text_file.write("Tilt: " + str(tilt) + "\n")
	text_file.write("\n")
	text_file.write("The overall Score is: " + str(score) + "\n")
	text_file.write("\n")
	text_file.write("Description: " + str(description) + "\n")
	text_file.write("Pros: " + str(pros) + "\n")
	text_file.write("Cons: " + str(description) + "\n")
	text_file.write("\n")
	text_file.write("This review was made on " + today +". With version: " + version + "\n")
	text_file.close()
	
	print("Currently exporting data into a text file...")
	time.sleep(3)
	print("Export complete")

def main():
	today = current_date()
	
	file_name = name_file()
	app_name = name_app()
	reviewer = set_reviewer()
	print("")
		
	usability = rate_usability()
	reliability = rate_reliability()
	asthetics = rate_asthetics()
	quality = rate_quality()
	tilt = set_tilt()
	print("")
	
	score = calculate_score(usability, reliability, asthetics, quality, tilt)
	print("")
	
	description = set_description()
	pros = set_pros()
	cons = set_cons()
	
	
	write_to_text_file(today, file_name, app_name, usability, reliability, asthetics, quality, tilt, score, pros, cons, description, reviewer)
	




main()
