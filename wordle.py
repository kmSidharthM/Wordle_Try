# importing all required lin
import random
from colorama import Fore,Back
import colorama


colorama.init(autoreset=True)
rand_num=random.randrange(0,103985,7)

# opening the file and reading the answer
file=open('Wordle_Words.txt','r')
file.seek(rand_num)
answer=file.readline()



# running your tries
print('\n\n\n******************************WORDLE******************************')
print('YOU HAVE 5 TRIES TO GUESS THE WORD')
tries=1
flag=0
while(tries<=5):
    guess=input()
    if(len(guess)==5):
        if(guess==answer):
            print('\nCONGRATS!!!')
            flag=1
        else:
            for l in range(0,5):
                if(guess[l] in answer and guess[0:l+1].count(guess[l])<=answer.count(guess[l])):
                    if(guess[l]==answer[l]):
                        print(Back.GREEN+' '+guess[l]+' ',end='')
                    else:
                        print(Back.YELLOW+' '+guess[l]+' ',end='')
                else:
                    print(Back.RED+' '+guess[l]+' ',end='')
            print()
            tries+=1
    else:
        print("WORD NOT ACCEPTABLE!")
        
if(flag==0):
    print('The answer is:'+answer)
    print('BETTER LUCK NEXT TIME!!!')
file.close()
