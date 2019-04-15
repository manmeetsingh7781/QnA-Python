""""
Create a quiz and record the name and score in the seprate file
Quiz will be on Python programming language
It will have level of difficulties
https://www.guru99.com/python-interview-questions-answers.html
"""
from random import randint

Q_A1 = [
        "Q: What is Python?\n",
        "1. Python is a programming language with objects, modules, threads, exceptions and automatic memory management.\n",
        "2. A coding convention, a set of recommendation, about how to write your Python code more readable.\n",
        "3. Python language is an interpreted language. Python program runs directly from the source code. \n",
        "4. Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.\n"]

Q_A2 = ["Q: What are the benefits of using Python?\n",
        "1. The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.\n",
        "2. Python is a programming language with objects, modules, threads, exceptions and automatic memory management.\n\n",
        "3. Python is simple and easy, portable, extensible, build-in data structure and it is an open source.\n",
        "4. Python language is an interpreted language. Python program runs directly from the source code.\n"];

Q_A3 = ["Q: What is PEP 8?\n",
        f"{Q_A2[1]}\n",
        f"{Q_A2[3]}\n",
        f"{Q_A1[2]}\n",
        f"4. The syntax constructions to ease the creation of a Dictionary or List based on existing iterable.\n"];

Q_A4 = ["Q: What is pickling?\n",
        "1. A Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling.\n",
        "2. A program runs directly from the source code.\n",
        f"{Q_A2[3]}\n",
        f"{Q_A1[4]}\n"];

Q_A5 = ["Q: What is unpickling?\n",
        "1. The process of retrieving original Python objects from the stored string representation\n",
        f"{Q_A3[4]}\n",
        f"{Q_A1[1]} \n",
        "4. They are syntax constructions to ease the creation of a Dictionary or List based on existing iterable.\n"];

Answers = [Q_A1[1], Q_A2[3], Q_A3[3], Q_A4[1]]

def getRandomQuestion(*args):
        whole  = args[randint(0,len(args))-1];
        for each in whole:
                print(each)
getRandomQuestion(Q_A1, Q_A2, Q_A3, Q_A4, Q_A5)
