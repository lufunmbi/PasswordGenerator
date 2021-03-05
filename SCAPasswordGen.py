import random
import string

pwlength = int(input("Kindly enter desired length of password: Note that the minimum length is 6:"))
pwletters = int(input("How many letters do you want in the password? "))
pwNumbers = int(input("How many numbers do you want in the password? "))

def passwordGen(pwlength, pwletters, pwNumbers):
    numberOfSpecialChar = int(pwlength - (pwletters + pwNumbers))

    numb = string.digits
    specialChar = string.punctuation
    #ulowerLetters = string.ascii_letters
    ucLetters = string.ascii_uppercase
    lcLetters = string.ascii_lowercase

    if pwlength >= 6:
        #selectedLetters = ''.join((random.choice(ulowerLetters) for i in range(pwletters)))
        selectedLetters = ''.join((random.choice(ucLetters + lcLetters) for i in range(pwletters)))
        selectedDigits = ''.join((random.choice(numb) for i in range(pwNumbers)))
        selectedSpecialChar = ''.join((random.choice(specialChar) for i in range(numberOfSpecialChar)))

        selectedList = list(selectedLetters + selectedDigits + selectedSpecialChar)

        random.shuffle(selectedList)

        password = ''.join(selectedList)
        print("Your password is: " + password)
         #password
    else:
        print("Minimum length of password should be 6. Kinldy amend this and try again")


new_pass = passwordGen(pwlength, pwletters, pwNumbers)
new_pass