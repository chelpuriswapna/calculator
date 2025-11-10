import string
import random
length=int(input("enter the length of the password:"))
print("choose character set for password from these:" )
print("1.digits") 
print("2.letters") 
print("3.special characters") 
print("4.exit")
choice=input("enter your choice(1/2/3/4):")
if choice=='1':
    char_set=string.digits
elif choice=='2':
    char_set=string.ascii_letters
elif choice=='3':
    char_set=string.punctuation
elif choice=='4':
    print("exiting password generator.goodbye")
    exit()
else:
    print("invalid input.please select a valid option")
    exit()
password=[]
for i in range(length):
    random_char=random.choice(char_set)
    password.append(random_char)
print("the random password is"+" ".join(password))
      