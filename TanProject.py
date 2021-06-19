import random
import string

#function to generate array of lowercase letters
def lower_alphabets():
    array1=[]
    for letter in string.ascii_lowercase:
       array1.append(letter)
    return(array1)   

#function to generate array of uppercase letters
def upper_alphabets():   
     array2=[]
     for letter in string.ascii_uppercase:
        array2.append(letter)
     return(array2)

lower_case=lower_alphabets()                                                         #lowercase letters
upper_case=upper_alphabets()                                                         #uppercase letters
numbers=['1','2','3','4','5','6','7','8','9','0']                                    #numbers 
symbol=['!','#','$','*','&']                                                         #special characters

def shortPassword():
    return random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbol)

#functioin to generate random strong password
def PasswordGenerator():

 Password_4= shortPassword()
 Password_3= shortPassword()
 Password_2= shortPassword()
 Password_1= shortPassword()
 Password=Password_3+Password_4+Password_2+Password_1       
 return Password


Password=PasswordGenerator()
print(Password)
