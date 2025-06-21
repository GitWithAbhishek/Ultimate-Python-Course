print("Concept of f string")

str = "Hello Guys My Name is {} And I Am From {}"
name ="Abhishek"
country = "India"
print(str.format(name,country)) 
print(str.format(country,name)) # problem 1 

# solution of problem 1
strr = "Hello Guys My Name is {1} And I Am From {0}"
name ="Abhishek"
country = "India"
print(str.format(country,name)) 

# Effective solution is f string
print(f"Hello What Is up Guys My Name is {name} And I Am From {country}")

# Example 2
# Before
txt = "The Price is {price:.2f}"
print(txt.format(price = 200.643746))

# After
price = 63.4974
txtf = f"The Price Of The Product IS {price:.3f}"
print(txtf)

# Important - To Print f Styring As It Is 
str2 = "Hello My Name is {{name}}"
print(str2)