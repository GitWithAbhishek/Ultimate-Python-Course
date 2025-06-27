#Solution
print("Welcome To Koun Banega CrorePati")
print("We Have Five Questions And Each Correct Answer Will Award You With 1000 Rupees")
listquestion = ["What is the output of the following code? \n x = \"Python\"  \n print(x[1:4])"," Which of the following is used to define a function in Python?","print(2 ** 3)","Which of the following is a correct way to create a list in Python?","What will be the output of the following code? \n a = True \n b = False \n print(a and b)"]
listchoice = ["A. Pyt \nB. ythc \nC. ytho \nD. yth","A. function \nB. def \nC. define \nD. fun","A. 6 \nB. 8 \nC. 9 \nD. 5","A. list = (1, 2, 3) \nB. list = 1, 2, 3 \nC. list = [1, 2, 3] \nD. list = {1, 2, 3}","A. True \nB. False \nC. 1 \nD. 0"]
listcorrectans = ["D","B","B","C","B"]
lifeline = 0
rupee = 0
for i in range (0,5):
    print(listquestion[i])
    print(listchoice[i])
    a = input("Enter A , B , C , D \n")
    if(a == listcorrectans[i]):
        rupee = rupee +1000
    else:
        print("Wrong You Lost")
        break

print("You Have Win ",rupee)