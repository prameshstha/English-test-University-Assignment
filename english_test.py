# Name: Pramesh Shrestha
# Student Number: 10400927


#Importing random module
import random

#This function count the number of vowels in the selected word.
def countVowels(word):
    vowels= list('aeiouAEIOU')
    CountVow=sum(letter in vowels for letter in word)
    return CountVow

print('Welcome to the English test.')
score=0
wordList = ['HELLO', 'GOODBYE', 'NAME', 'DAY', 'NIGHT', 'HOUR', 'POTATO', 'BIG', 'SMALL', 'GOOD', 'BAD', 'YES', 'NO', 'HOUSE', 'QUESTION', 'BALLOON', 'CAT', 'DUCK', 'PIGEON', 'POSTER', 'TELEVISION', 'SPY', 'RHYTHM', 'SUBSTANTIAL', 'SNOW', 'MAGNET', 'TOWEL', 'WALKING', 'SPEAKER', 'UNCHARACTERISTICALLY']
randomQuestions = ['How many letters does the word contain?','How many vowels does the word contain?','How many consonants does the word contain?','What is # letter of the word?']
            
while True:
    try:
        numWords=int(input('How many words do you like to test?\n>'))
        for i in range (numWords):            
            questionCount=i+1
            word=random.choice(wordList)
            print('Word',questionCount,'/',numWords,':', word)
            questionToPrint=random.choice(randomQuestions)
            
            #replacing '#' with suffix
            if questionToPrint=='What is # letter of the word?':
                wordLengthRange=range(len(word))
                nthNum=random.choice(wordLengthRange)
                numNoSuffix=nthNum+1
                if numNoSuffix==1:
                    numSuffix='1st'
                elif numNoSuffix==2:
                    numSuffix='2nd'
                elif numNoSuffix==3:
                    numSuffix='3rd'
                elif numNoSuffix>3:
                    numSuffix=str(numNoSuffix)+'th'
                print(questionToPrint.replace('#',numSuffix))
            else:
                print(questionToPrint)
            


        #counting letters
            if questionToPrint=='How many letters does the word contain?':
                lettersLength=len(word)
                ans=input('>')
                ansStr=str(ans)
                correctAnsStr=str(lettersLength)
                if(ansStr==correctAnsStr):
                    print('Correct!\n')
                    score+=1
                
                else:
                    print('Incorrect! Correct answer was', lettersLength,'.\n')
                
            
        #counting vowels
            elif questionToPrint=='How many vowels does the word contain?':
                CountVow=countVowels(word)
                ans=input('>')
                ansStr=str(ans)
                correctAnsStr=str(CountVow)
                if(ansStr==correctAnsStr):
                    print('Correct!\n')
                    score+=1
                
                else:
                    print('Incorrect! Correct answer was', CountVow,'.\n')

                
        #counting consonnants
            elif questionToPrint== 'How many consonants does the word contain?':
                CountVow=countVowels(word)
                letterCount=len(word)
                consonant=letterCount-CountVow
                ans=input('>')
                ansStr=str(ans)
                correctAnsStr=str(consonant)
                if(ansStr==correctAnsStr):
                    print('Correct!\n')
                    score+=1
                
                else:
                    print('Incorrect! Correct answer was', consonant,'.\n')

                
        #nth letter
            elif questionToPrint== 'What is # letter of the word?':
                nthLetter=word[nthNum]
                ans=input('>')
                if ans.isalpha():
                   ans=ans.upper()
                ansStr=str(ans)
                correctAnsStr=str(nthLetter)
                if(ansStr==correctAnsStr):
                    print('Correct!\n')
                    score+=1
                
                else:
                    print('Incorrect! Correct answer was', nthLetter,'.\n')
                
            
    except ValueError:
        print('Invalid input!. Please enter an integer.')
        continue
    else:
        break
print('Game Over. Your score is', score,'/',numWords,'.')
input('Press ENTER to exit')

#optional additional requirements
#Repeat the program as the user wants
#input integer only in not message invalid input
#at least one question is asked
