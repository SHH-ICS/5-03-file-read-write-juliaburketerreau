# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
filehandle = open("testFile.txt", 'w')
question = input("What is your question?\n" )
filehandle.write(question)
print("Enter in answer options below")
for i in range (4):
    answer =input( " " )
    filehandle.write("\n" + answer)
correct= input("Enter your correct input: " )
filehandle.write("\n" + correct)
filehandle.close()