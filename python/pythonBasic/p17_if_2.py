#!/usr/bin/env python

while True:
    i = input("Input the first number: ")

    if(i=='q'):
        print("프로그램이 끝났습니다.")
    elif i.isalpha():
        print('다시 입력해주세요.')
        continue
    else:
        i = int(i)
        if(i>0):
            print("a는 양수 입니다")
        elif(i==0):
            print("a는 0 입니다")
        else:
            print("a는 음수 입니다")
