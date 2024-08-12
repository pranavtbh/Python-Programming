def dollarizer(word):
    return word.replace('s', '$')

string = dollarizer("testcase")
print(string)

def eurizer(word):
    return word.replace('e', '€')

string = eurizer("testcase")
print(string)

def replacer(word):
    return word.replace('t', '#')

string = replacer("testcase")
print(string)

def wonky_text(input_string):
    # Replace 's' with '$'
    output_string = input_string.replace('s', '$')
    # Replace 'e' with '€'
    output_string = output_string.replace('e', '€')
    # Replace 'l' with '£'
    output_string = output_string.replace('l', '£')
    
    return output_string

print(wonky_text("testcase"))

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_in_celsius = 25
temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")

def age_in_days(age_in_years):
    days_in_a_year = 365
    age_in_days = age_in_years * days_in_a_year
    return age_in_days

print(age_in_days(25))

def simple_interest(p, r ,t):

    si = (p * r * t)/100
    print("Simple Interest is:", si)
    return si

simple_interest(7,8,10)

def plan_finances(principal, rate, time, desired_final_amount):
    
    simple_interest = (principal * rate * time)/100

    final_amount = simple_interest + principal

    return final_amount >= desired_final_amount

print(plan_finances(10000, 5, 2, 11000))
