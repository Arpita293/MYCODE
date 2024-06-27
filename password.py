import random 
import array 
max_len = 6 #to insert maximum length of the password
# list of formats to create a password
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower_case= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					'z'] 

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					'Z'] 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
		'*', '(', ')', '<'] 

list = digits + lower_case + upper_case + symbols

rand_digit = random.choice(digits) 
rand_upper = random.choice(upper_case) 
rand_lower = random.choice(lower_case) 
rand_symbol = random.choice(symbols) 

temp_pw = rand_digit + rand_upper + rand_lower + rand_symbol 

for x in range(max_len - 4): 
	temp_pw = temp_pw + random.choice(list) 

	temp_pw_list = array.array('u', temp_pw) 
	random.shuffle(temp_pw_list) 

# to create the password 
password = "" 
for x in temp_pw_list: 
		password = password + x 
		
# print the password 
print("your password is :",password) 
