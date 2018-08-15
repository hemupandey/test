# name = "PythonBo"
#machine = "HAL"
#print("Nice to meet you {0}. I am {1} 
# print("Hello, %s!" % name)
#data = ("John", "Doe", 53.44)
#format_string = "Hello"
#print("%s" % format_string "%s" % data)
#name=input("Enter your Name:- ")
#print("Hello, ",name)
#num=eval(input("Enter number value:- "))
#print("Your number square value is:- ",num*num)
# print("Himanshu","Pandey","Hemu",sep=" : ")
# print("himanshu Pandey",end=":")
# print("Hemu")
# temp=eval(input("Please enter numeric value:- "))
# if temp > 5 :
    # print("Value is higher then 5")
# else :
    # print("Value is less then or equal to 5")
# for i in range(1,4):
    # print(" "*(4-i),end = "")
    # print("*"*(2*i-1))
# for i in range(1,4):
    # print(" "*(i-1),end="")
    # print("*"*(8-2*i-1))
# for i in range(4):
    # print("A")
    # for j in range(2):
        # print("B")
# num=eval(input("Please input the letter size:- "))
# for i in range(num):
#     print(" "*((2*num)-i),end="")
#     if i==num/2:
#         print("*"*(2*i+1),end="")
#     else:
#         print("*",end="")
#         print(" "*(2*i-1),end="")
#         print("*",end="")
#     print("")
# s='hemupandey'
# print(s[2:5])
# print(s[ : :-1])
# print(s[ : :2])
# print(s[ :-2])
# s=input("Enter the string")
# doubled_s=''
# for c in s:
#     doubled_s=doubled_s+c*2
# print(doubled_s)
# s=input("Enter the string:- ")
# cnt=1
# for c in s:
#     if c == ' ':
#         cnt = cnt + 1
# print("Number of words in given string:-",cnt)
# s=input("Enter a string:- ")
# print(s[ : :-1])
# if s == s[ : :-1]:
#     print("String is Panindrom")
# for i in range(len(s)):
#     if s[i] == 'a':
#         s[i]='e'
# s=s.replace('a','e')
# print(s)
# l=eval(input("Enter the list:- "))
# print(l)
# for i in range(len(l)):
#     print(l[i])
# l=l+[7,8,9]
# print(l)
# s='Hi! This is a test.'
# l=s.split()
# print(s)
# print(l)
# from string import punctuation
# for c in punctuation:
#     s = s.replace(c,'')
# print(s)
# print(s.split(' '))
# l1=s.split(' ')
# print(list(s))
# print('*******'.join(l1))
# l2 = [i for i in range(5)]
# print(l2)
# from pprint import pprint
# pprint(l2)
# i = 0
# while i<50:
#     print (i)
#     i=i+2
# print('Bye!')
# lines = [line.strip() for line in open ('example.txt')]
# print(lines)
# s = open('example.txt').read()
# print(s)
# f = open('write.txt','w')
# print('this is the first line')
# print('this is the second line')
# f.close()
# s = open('write.txt').read()
# print(s)
# d = {'dog' : 'has a tail and goes woof!',
# 'cat' : 'says meow',
# 'mouse' : 'chased by cats'}
# d[word] = input('Enter a word: ')
# print('The definition is:', d[word])
# def print_hello():
#     print('Hello !')
#     print('Printing through function')
# print('12345')
# print_hello()
# def multi_print(s,n=1):
#     print(s*n)
#     print()
# multi_print('Hello')
# multi_print('A',10)

# def fancy_print(text,color='black',background='white',
#                     style='normal',justify='left'):

# fancy_print('Himanshu',style='bold')
# fancy_print('Pandey',color='yellow',background='black')
# fancy_print('Hemu')
# def func1():
#     for i in range(10):
#         print(i)
# def func2():
#     i=100
#     func1()
#     print(i)
# func2()
# def func1(x):
#     x = x + 1
#     return x
# def func2(L):
#     copy = L[:]
#     copy = copy + [1]
#     return copy
# a=3
# M=[1,2,3]
# a = func1(a)
# M = func2(M)
# print(a)
# print(M)
# # print(copy)
# class example:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
# e = example(8,6)
# print(e.add())

# from string import panctuation
# import string

# class Analyzer:
#     def __init__(self,s):
#         for c in panctuation:
#             s = s.replace(c,' ')
#         s = s.lower()
#         self.words = s.split()
#     def number_of_words(self):
#         print(self.words)
#         return len(self.words)
#     def starts_with(self, s):
#         return len([w for w in self.words if w[:len(s)]==s])
# s = 'This is a test of the class.'
# analyzer = Analyzer(s)
# print(analyzer.words)
# print('Number of words:', analyzer.number_of_words())
# print('Number of words starting with "t":', analyzer.starts_with('t'))
# from tkinter import *
# def calculate():
#     temp = int(entry.get())
#     temp = 9/5*temp+32
#     output_label.configure(text = 'Converted: {:.1f}'.format(temp))
#     entry.delete(0,END)
# root = Tk()
# message_label = Label(text='Enter a temperature',
# font=('Verdana', 16))
# output_label = Label(font=('Verdana', 16))
# entry = Entry(font=('Verdana', 16), width=4)
# calc_button = Button(text='Ok', font=('Verdana', 16),
# command=calculate)
# message_label.grid(row=0, column=0)
# entry.grid(row=0, column=1)
# calc_button.grid(row=0, column=2)
# output_label.grid(row=1, column=0, columnspan=3)
# mainloop()

# from tkinter import *
# def concat():
#     fname = entf.get()
#     lname = entl.get()
#     # name = fname + lname
#     out.configure(text='Full Name')
#     print(fname)
#     entf.delete(0,END)
#     entl.delete(0,END)
# root = Tk()
# # hello_label = Label(text='hello')
# msg = Label(text='Enter first name',font=('Verdan',16))
# msg.grid(row=0,column=0)
# out = Label(font=('Verdan',16))
# # out.grid(row=0,column=0)
# entf = Entry(font=('Verdan',16),width=40)
# entf.grid(row=0,column=1)
# msg = Label(text='Enter last name',font=('Veredan',16))
# msg.grid(row=1,column=0)
# entl = Entry(font=('Verdan',16),width=40)
# entl.grid(row=1,column=1)
# but = Button(text='OK',font=('Verdan',16),command=concat)
# but.grid(row=0,column=2)
# out.grid(row=2, column=0, columnspan=3)
# mainloop()

# number = 3
# python_course = True

# if not number == 3 and python_course:
#     print ("this will execute")
# a = 1
# b = 2
# print("bigger" if a > b else "smaller")
# student = ["Mark","Katarina","Jessica"]
for i in range(10):
    for j in range(i):
        print(i)







