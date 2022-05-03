
def main():
	MIN_HEIGHT = 60 
	MAX_HEIGHT = 170
	height = 0
	height = int(input("What is your height in inches?: ")) #input

	if height < MIN_HEIGHT:
		print("We could not calculate the perfect weight for your height.")
		main()
	elif height > MAX_HEIGHT:
		print("Please enter an appropriate height, in inches.: ")
		main()
	else:
		maleEntries = ["m", "M", "male", "Male"]
		femaleEntries = ["f", "F", "female", "Female"]
		gender = input("Are you a male or female? ") #input
		while gender not in maleEntries and gender not in femaleEntries:
			print("You have entered an invalid response. Please try again.")
			gender = input("Are you a male or female? ")
	
	if gender in maleEntries:
		convert = getMale(height)
		print ("Your ideal weight is ", convert, "pounds")
	elif gender in femaleEntries:
		convert = getFemale(height)
		print ("Your ideal weight is ", convert, "pounds")
	else:
		print("Invalid entry.")
	
	again = input("Do you have another weight to input? y or n: ") #input
	yea = ["y", "yes", "Y", "Yes"]
	if again in yea:
		main()
	else:
		print("end.")

def getMale(userHeight):
	MIN_HEIGHT = 60 #min height
	BASE_MALE = 56.2 
	MALE_CONVERSION_FACTOR = 1.41 
	calcMale = BASE_MALE + MALE_CONVERSION_FACTOR * (userHeight - MIN_HEIGHT) #calculation
	maleConversion = calcMale * 2.205
	return round(maleConversion)

def getFemale(userHeight):
	MIN_HEIGHT = 60
	BASE_FEMALE = 53.1
	FEMALE_CONVERSION_FACTOR = 1.36
	calcFemale = BASE_FEMALE + FEMALE_CONVERSION_FACTOR * (userHeight - MIN_HEIGHT) #calculation
	femaleConversion = calcFemale * 2.205
	return round(femaleConversion)

print("This program is designed to give you the ideal weight of a person over 5 feet.")
main()
