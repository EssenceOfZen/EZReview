#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  EZReview.py
#  
#  Copyright 2012 ZenOokami <zenookami@ubuntu>
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
version = "1.0.1"

file_name = ""
app_name = ""

usability = 0 # is it user friendly?
reliability = 0 # does it crash often?
asthetics = 0 #The look of the app
quality = 0 # is it well made?
tilt = 0

def calculate_score(usability, reliability, asthetics, quality, tilt):
	global score
	score = (usability + reliability + asthetics + quality + tilt) / 5 # gets the average of all scores

	return score

def isValidInput(inputToValidate):
	
	try:
		inputToValidate = float(inputToValidate) # attempt to convert to float
		
		if inputToValidate < 0 or inputToValidate > 5:
			print("\nInvalid input: score must be 0 to 5.\n")
			return False # invalid input
			
	except ValueError:
		print("\nInvalid input: score must be an actual number.\n")
		return False # invalid input
	
	return True # valid input
	

def main():
	today = time.asctime(time.localtime(time.time()))
	
	file_name = input("Please input a review title: ")
	app_name = input("Please input the name of the application: ")
	
	print("") # just a newline, move along, nothing to see here...
	
	while True:
		usability = input("Please input Usability score: ")
		if isValidInput(usability): # if input is valid, get out of loop
			usability = float(usability)
			break
			
	while True:
		reliability = input("Please input Reliability score: ")
		if isValidInput(reliability): # if input is valid, get out of loop
			reliability = float(reliability)
			break
		
	while True:
		asthetics = input("Please input Asthetics score: ")
		if isValidInput(asthetics): # if input is valid, get out of loop
			asthetics = float(asthetics)
			break
			
	while True:
		quality = input("Please input Quality score: ")
		if isValidInput(quality): # if input is valid, get out of loop
			quality = float(quality)
			break
			
	while True:
		tilt = input("Please input your Tilt score: ")
		if isValidInput(tilt): # if input is valid, get out of loop
			tilt = float(tilt)
			break
	
	calculate_score(usability, reliability, asthetics, quality, tilt) # calculate the score
	
	print ("\nOverall Score: " + str(score) + "\n" ) # print the score
	
	#print(score) #testing to see if the variable changed globally instead of locally
	
	print("Currently exporting data into a text file...")
	
	#Start file writing
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
	text_file.write("\n")
	text_file.write("Usability: " + str(usability) + "\n")
	text_file.write("Reliability: " + str(reliability) + "\n")
	text_file.write("Asthetics: " + str(asthetics) + "\n")
	text_file.write("Quality: " + str(quality) + "\n")
	text_file.write("Tilt: " + str(tilt) + "\n")
	text_file.write("\n")
	text_file.write("The overall Score is: " + str(score) + "\n")
	text_file.write("\n")
	text_file.write("This review was made on " + today +". With version: " + version + "\n")
	text_file.close()
	
	time.sleep(3)
	print("Export complete\n")	

main()
