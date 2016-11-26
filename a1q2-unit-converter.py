#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Variable declaration
sack_to_cubic_metres = 0.109106
wey_to_cubic_metres  = 1.409563

# Provide description of program
print('This program takes a number of sacks from the user, converts it to a corresponding number of weys,\n' + \
	'and prints the result. It then takes a number of weys from the user, converts it to a corresponding\n' + \
	'number of sacks, and prints the result. All that is required from the user is that they enter a\n' + \
	'positive real number for both required values.')

# Retrieve sack value
input_sack = float(input('\n\n\nNumber of sacks: '))

# Convert to wey value
output_wey = input_sack * sack_to_cubic_metres / wey_to_cubic_metres

# Print wey value
print(input_sack, 'sack is equivalent to', output_wey, 'wey.')

# Retrieve wey value
input_wey = float(input('\n\nNumber of wey: '))

# Convert to sack value
output_sack = input_wey * wey_to_cubic_metres / sack_to_cubic_metres

# Print sack value
print(input_wey, 'wey is equivalent to,', output_sack, 'sack.')

# Thank the user for using the program
print('Thank-you for using this program, you may terminate it whenever you wish.')