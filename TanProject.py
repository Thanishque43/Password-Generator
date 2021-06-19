
import random
import string
def lower_alphabets():
    array1=[]
    for letter in string.ascii_lowercase:
       array1.append(letter)
    return(array1)   
def upper_alphabets():   
     array2=[]
     for letter in string.ascii_uppercase:
        array2.append(letter)
     return(array2)
def PasswordGenerator():
 lower_case=lower_alphabets()
 upper_case=upper_alphabets()
 numbers=['1','2','3','4','5','6','7','8','9','0']
 symbol=['!','#','$','*','&']
 Password_4=random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbol)
 Password_3=random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbol)
 Password_2=random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbol)
 Password_1=random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbol)
 Password=Password_3+Password_4+Password_2+Password_1       
 return Password
Password=PasswordGenerator()
print(Password)
