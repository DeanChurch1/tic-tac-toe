print("terms")
puzzle="VNSSALCTTYKXAOGJVWDDEDEYRINPNJLLXTRXITIILZBDUTYYACRYNURBWEPVBNTTODILEGQZLUSDNRETGTXPEFVVTIVXYBPLPYWTMNRDTZERTBAMTMKPENKPRRJZZPLKMFQB"
c=0
print(puzzle)
print("word lists")
word_list="index","variable","function","def","len","print","class","double","attribute"
clue_list="the location of a charactor in a string","used to store information of any type","used to call and store repetitive code","starts a function dEFNITION","gets lenght of string","sends text to terminal", "a code envelope","stores double the normal integer max","a value of a object"
print(word_list)
def display_puzzle():
    print("  012345678910")
    print("0 "+puzzle[0:11])
    print("1 "+puzzle[12:23])
    print("2 "+puzzle[24:35])
    print("3 "+puzzle[36:47])
    print("4 "+puzzle[48:59])
    print("5 "+puzzle[60:71])
    print("6 "+puzzle[72:83])
    print("7 "+puzzle[84:95])
    print("8 "+puzzle[95:107])
    print("9 "+puzzle[108:119])
    print("10"+puzzle[120:131])
display_puzzle()#prints puzzle
word2=""#temporary word storage for conversion
e=10# number of words
z=0#count storage
attempts = 1#used to count attempts
word1=input("enter the index positions of "+clue_list[0]+" split by commas")#get first word
try:
    word2=word1.split(",")#split the chars
    word2 = list(map(int, word2))#send indexes to list
    i=0#really temporary count storage to isolate questions
    foundword = ""#word your looking for
except:
    print("WRONG!")
while z<11:#while within count
    print("score = " ,e)#print score
    while i<len(word_list[z]):#while runn9ng:
        index=word2[i]#index wordc
        index=int(index)#read placeholders
        foundword = foundword+puzzle[index+1]#found it? if so continue
  

    foundword = foundword.lower#lower the case
    if foundword in word_list:#if in: run
        display()
    else: attempts = attempts+1#fails, then increase attempt by 1
    word1=input("enter the index positions of "+"a "+clue_list[1]+" split by commas")#secondary get posiot
    word2=word1.split(",")#split to index
    word2 = list(map(int, word2))#read positions rom list
    i=0#reset count
    foundword = ""#reset foundwoerd
def display():#display gthe scxores
    e = e+(100/attempts)#calculate score
    attempts = 1#reset attempt
    z=z+1
    score = str(e)#turn score to string
    print("score = " +score+" you've got a word: ",foundword)#print succes
    


input("press enter to exit")#number exit
