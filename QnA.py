""""

Create a quiz and record the name and score in the seprate file Quiz will be on Python programming language It will have level of difficulties
https://www.guru99.com/python-interview-questions-answers.html

"""
from random import randint

Q_A1 = [
        "Q: What is Python?\n",
        "Python is a programming language with objects, modules, threads, exceptions and automatic memory management.",
        "A coding convention, a set of recommendation, about how to write your Python code more readable.",
        "Python language is an interpreted language. Python program runs directly from the source code.",
        "Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc."]

Q_A2 = ["Q: What are the benefits of using Python?\n",
        "The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.",
        "Python is a programming language with objects, modules, threads, exceptions and automatic memory management.",
        "Python is simple and easy, portable, extensible, build-in data structure and it is an open source.",
        "Python language is an interpreted language. Python program runs directly from the source code."];

Q_A3 = ["Q: What is PEP 8?\n",
        f"{Q_A2[1]}",
        f"{Q_A2[3]}",
        f"{Q_A1[2]}",
        f"The syntax constructions to ease the creation of a Dictionary or List based on existing iterable."];

Q_A4 = ["Q: What is pickling?\n",
        "A Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling.",
        "A program runs directly from the source code.",
        f"{Q_A2[3]}",
        f"{Q_A1[4]}"];

Q_A5 = ["Q: What is unpickling?\n",
        "The process of retrieving original Python objects from the stored string representation",
        f"{Q_A3[4]}",
        f"{Q_A1[1]}",
        "They are syntax constructions to ease the creation of a Dictionary or List based on existing iterable."];

Answers = [Q_A1[1], Q_A2[3], Q_A3[3], Q_A4[1]]

def getRandomQuestion(*args):
        whole  = args[randint(0,len(args))-1];
        counter = 0;
        print(whole[0])
        for each in whole:
                if(counter > 0):
                        print(str(counter) + ". " + each)
                counter += 1;
getRandomQuestion(Q_A1, Q_A2, Q_A3, Q_A4, Q_A5)

answer = input("\nPick a number to answer the following question\n->");
print("You picked {}".format(answer))
