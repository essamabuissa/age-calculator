import datetime

def check_birthdate(year, month, day):
	# write code here
	today_year  = datetime.date.today().year
	today_month = datetime.date.today().month
	today_day   = datetime.date.today().day

	if year >= today_year:
		if year > today_year:
			return False
		elif month > today_month or day > today_day:
				return False
		else:
			print("s")
			return True
	else:
		print("ss")
		return True

def calculate_age(year, month, day):
    # write code here
	today_year  = datetime.date.today().year
	today_month = datetime.date.today().month
	today_day   = datetime.date.today().day

	if today_month < month:
		age = (today_year - year) - 1
	else:
		age = (today_year - year)
	print("You are %d years old." % (age))

def main():
	# write main code here
	birth_year  = int(input("Enter year of birth: "))
	birth_month = int(input("Enter month of birth: "))
	birth_day   = int(input("Enter day of birth: "))
	if check_birthdate(birth_year,birth_month,birth_day):
		calculate_age(birth_year,birth_month,birth_day)
	else:
		print("The birthdate is invalid!")

if __name__ == '__main__':
	main()
