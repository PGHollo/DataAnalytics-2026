# Messy contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

print("Lowercase Names")
print("---------------")
print(f"Name 1 lowercase: {name_1.lower()}")
print(f"Name 2 lowercase: {name_2.lower()}")
print(f"Name 3 lowercase: {name_3.lower()}")

print()

print("Title Case Names")
print("----------------")
print(f"Name 1 title case: {name_1.title()}")
print(f"Name 2 title case: {name_2.title()}")
print(f"Name 3 title case: {name_3.title()}")

print()

clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

print("Salary Strings Without Dollar Signs")
print("-----------------------------------")
print(f"Salary 1 without dollar sign: {clean_salary_1}")
print(f"Salary 2 without dollar sign: {clean_salary_2}")
print(f"Salary 1 type after replace: {type(clean_salary_1)}")
print(f"Salary 2 type after replace: {type(clean_salary_2)}")

# These values are still strings.
# To perform math, remove the comma and convert them to integers.

print()

usable_salary_1 = int(salary_1.replace("$", "").replace(",", ""))

print("Salary Converted to Integer")
print("---------------------------")
print(f"Usable salary 1: {usable_salary_1}")
print(f"Usable salary 1 type: {type(usable_salary_1)}")