import random
st=[]

guess_word = input("Enter the word to guess (will be hidden): ").lower()
print("\n" * 50)
ty=6

hint=guess_word[0]+".."+guess_word[-1]
hint
a=input("enter a name :")
print("welcome to the game",a)
print("we are giving you to guess the word within 6 attempts")
for guess in range(ty):
    while True:
        letter=input("Guess the letter")
        if len(letter)==1:
            break
        else:
            print("opps! please guess the word")
    if letter in guess_word:
        print("yes")
        st.append(letter)
    else: 
        print("no")
    if guess==3:
        print()
        cr=input("would you like to have clue")
        if cr.lower().startswith('y'):
            print()
            print("the first and last letter would be ",hint)
        else: 
            print("you are very confident")

print()
print("now lets see what you have done so far,you have passed",len(st))
print("these letters are",st)
word_guess=input("guess the word")
if word_guess.lower()==guess_word:
    print("congrats your correct")
else:
    print("sorry, the answer is ",guess_word)
print()