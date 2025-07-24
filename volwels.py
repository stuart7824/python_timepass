a=input('Enter your letter: ')
if len(a)==1 and type(a)==str and a.islower()==True:
    if a in "aeiou":
        print("It is a vowel")
    else:
        print('It is a consonant')
else:
    print("Wrong Input!")
