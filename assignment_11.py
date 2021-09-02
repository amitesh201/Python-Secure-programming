import sys
import re
from api import *
import csv
import logging
from datetime import datetime 


# Regex for phone numbers of users
phone_type_1 = '^\d{5}$'
phone_type_2 = '^\(\d{3}\)\d{3}\-\d{4}$'
phone_type_3 = '^\d{3}-\d{4}$'
phone_type_4 = '^\+\d\(\d{3}\)\d{3}\-\d{4}$'
phone_type_5 = '^\+\d{2}\s\(\d{2}\)\s\d{3}\-\d{4}$'
phone_type_6 = '^\d\(\d{3}\)\d{3}\-\d{4}$'
phone_type_7 = '^\d{3}\s\d{3}\s\d{3}\s\d{4}$'
phone_type_8 = '^\d{5}\.\d{5}$'
phone_type_9 = '^\d{3}\s\d\s\d{3}\s\d{3}\s\d{4}$'
list_phono_acceptable = [phone_type_1,phone_type_2,phone_type_3,phone_type_4,
phone_type_5,phone_type_6,phone_type_7,phone_type_8,phone_type_9]

# Regex for names if user
name_type_1 = '^\w+\s\w+$'
name_type_2 = '^\w+\,\s\w+$'
name_type_3 = '^\w+\,\s\w+\s\w+$'
name_type_4 = "^\w\'\w+\,\s\w+\s\w\.$"
name_type_5 = "^\w+\s\w\'\w+\-\w+$"
name_type_6 = '^\w+$'
list_name_acceptable = [
    name_type_1,
    name_type_2,
    name_type_3,
    name_type_4,
    name_type_5,
    name_type_6]

length = len(sys.argv)

def log(input,output):
	logging.basicConfig(filename="phonebook.log", level = logging.DEBUG)
	logger = logging.getLogger()
	if len(input)>=3:
		for val in input:
			if val == "ADD":
				logger.info('Operation: {} Name: {} PhoneNumber:{} Result: {} TimeStamp: {}'.format(input[1],input[2],input[3],output,datetime.now()))
				logger.info('Result: {}'.format(output))
				
			elif val == "DEL":
				logger.info('Operation: {} Value: {} Result: {} TimeStamp: {}'.format(input[1],input[2], output,datetime.now()))
	else:
		if input[1] == "ADD" or input[1] == "DEL":
			logger.info('Operation: {}, Result: {} TimeStamp: {}'.format(input[1],output,datetime.now()))
		elif input[1] == "LIST":
				logger.info('Operation:{} Result: {} TimeStamp: {}'.format(input[1],output,datetime.now()))

			


def add_info(name, phone_number):
	#print(name)
	#print(phone_number)
	success_name = ""
	success_number = 0
	for name_validate in list_name_acceptable:
		if re.search(name_validate, name):
			#print("search was successful")
			success_name = name
			
        
	for phone_validate in list_phono_acceptable:
		if re.search(phone_validate, phone_number):
			success_number = phone_number
			

	# loop ends
	if success_name and success_number:
		insert(success_name,success_number)
		
		return 0
	else:
		return 1


def delete_info(entry):
	#print(entry)
	if re.search('^\d+',entry):
		for phone_validate in list_phono_acceptable:
			if re.search(phone_validate,entry):
				#print("regex working")
				if delete_by_phone(entry):
					return 0
				else:
					return 1
			else:
				return 1
	elif re.search('^\w+',entry):
		#print(entry)
		
		for name_validate in list_name_acceptable:
			if re.search(name_validate,entry):
				#print("working")
				if delete_by_name(entry):
					return 0
				else:
					return 1
		else:
			return 1


if length > 1 and length < 5:
	for arg in range(1,length):
		if sys.argv[arg] == "ADD":
			if length >=4:
				if add_info(sys.argv[arg+1],sys.argv[arg+2]):
					print("Input could not be validated you either gave name in incorrect format or phone number in incorrect format")
					log(sys.argv,"fail")
				else:
					print("Information successfully added")
					log(sys.argv,"success")
			else:
				print("Input given cannot be accepted as more or less arguments are given. Please follow the format")
				log(sys.argv[:2],"fail")
		elif sys.argv[arg] == "LIST":
			get()
			log(sys.argv,"success")
		elif sys.argv[arg] == "DEL":
			if length >=3:
				if delete_info(sys.argv[arg+1]):
					print("PhoneNumber or User Name provided does not exist")
					log(sys.argv,"fail")
				else:
					print("Entry Successfully Deleted")
					log(sys.argv,"success")
			else:
				print("Input given cannot be accepted as more or less arguments are given. Please follow the format")
				log(sys.argv,"fail")
else:
	display_text = """The option available for users are:-
	1) To add element use ADD followed by Name and Phone Number in the given order only.
	2) To delete any element use DEL keyword followed by Name or Phone Number of the given individual.
	3) To List all the entries use List keyword and press Enter
	4) Not following the instructions and providing input other than how it is specified will result in getting disapproved
	Thank You for understanding and enjoy our program."""
	print(display_text)
