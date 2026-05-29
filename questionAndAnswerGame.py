print("Lets play a game")
isPlaying = input("Would you like to play a game?")

if isPlaying.lower() != 'yes' :
    quit()

print("great, kindly provide the full meaning of the following abbrevation")
result = 0

answer = input("What is full meaning of w.h.o? ")
if answer.lower() == 'world health organization' :
    print ('Thats correct!')
    result += 1
else: 
    print('Thats incorrect')


answer = input("What is full meaning of g.p.u? ")
if answer.lower() == 'graphical processing unit' :
    print ('Thats correct!')
    result += 1
else: 
    print('Thats incorrect')


answer = input("What is full meaning of p.d.f? ")
if answer.lower() == 'printable document file' :
    print ('Thats correct!')
    result +=1
else: 
    print('Thats incorrect')


answer = input("What is full meaning of css? ")
if answer.lower() == 'carscading style sheet' :
    print ('Thats correct!')
    result += 1
else: 
    print('Thats incorrect')


answer = input("What is full meaning of html? ")
if answer.lower() == 'hypertext markup language' :
    print ('Thats correct!')
    result += 1
else: 
    print('Thats incorrect')


answer = input("What is the full meaning of http? ")
if answer.lower() == 'hypertext transfer protocol' :
    print('Thats correct')
    result += 1
else:
    print('Thats Incorrect!')



answer = input("What is the full meaning of RAM? ")
if answer.lower() == 'random access memory' :
    print('Thats correct')
    result += 1
else:
    print('Thats Incorrect!')

print("Your Score is:" + str(result)  + "/7")