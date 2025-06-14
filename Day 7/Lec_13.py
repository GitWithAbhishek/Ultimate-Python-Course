print("String Methods")
name = "Abhishek"
print(name)
print(name.upper())
print(name.lower())
name = "Naman!!!!"
print(name.rstrip("!"))
name = "Naman Pandey"
print(name.replace("Pandey","Pandit"))
para = "Hello Abhishek Pandey How Are you"
print(para.split(" "))
print(para.capitalize())
paragraph = """Python is a high-level, interpreted programming language that is widely known for its simplicity and readability. Designed to be easy to learn, Python uses a clean and straightforward syntax that closely resembles English, making it ideal for beginners as well as professionals. It is a versatile language used in various domains such as web development, data analysis, artificial intelligence, automation, and more. """
print("Is Appear ",paragraph.count("is")," Times");
print("Index of That in paragraph",paragraph.find("that"));
print("Index of That in paragraph",paragraph.index("that")); # If It Can Not Found i Will Give An Error
name= "Abhishek!!!"
print("Is Name Ends With !!",name.endswith("!"))

alphanumeric = "HelloGuysHowAreYou"
print(alphanumeric.isalpha());
print(alphanumeric.isalnum());
print(alphanumeric.islower());

str1 = "Hello Guys How Are You Doing \n"
print(str1.isprintable());
print(str1.isspace());

title = "How Guys"
print(title.istitle());
print(str1.startswith("H"));

str2 = "how Are you"
print(str2.title());