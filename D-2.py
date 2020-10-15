'''
AM = int(input("아메리카노:"))
CL = int(input("카페라떼:"))
CP = int(input("카푸치노:"))
print("총 매출은",(2000*AM+3000*CL+CP*3500),"입니다")

xx = int(input("x:"))
yy = int(input("y:"))
print("두 수의 합:",(xx+yy))
print("두 수의 차:",(xx-yy))
print("두 수의 곱:",(xx*yy))
print("두 수의 평균:",((xx+yy)/2))
print("큰 수:", max(xx,yy))
print("작은 수", min(xx,yy))
'''
'''
xx = int(input("정수를 입력하시오:"))

total = 0 
total += xx//1000 
xx = xx%1000 

total += xx//100
xx = xx%100

total += xx//10
total += xx%10 

print("자리수의 합 : ", total)

import turtle
turtle.Turtle()
turtle.shape("turtle")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
data= turtle.textinput("입력한 제목","설명라인")
turtle.write("안녕하세요?"+data+"씨, 텨틀 인사드립니다")
turtle.done()

print("안녕하세요?")
name =input("이름이 어떻게 되시나요?")
print("만나서 반갑습니다",name,"씨")
print("이름의 길이는 다음과 같군요",len(name))
age= int(input("나이가 어떻게 되시나요?"))
print("내년이면",age+1,"이 되시는 군요.")

n =input("기호를 입력하시오:")
sli =input("중간에 삽입할 문자열을 입력하시오:")
print(n[0]+sli+n[1])
'''
'''
s =int(input("x1:"))
a =int(input("y1:"))
ss=int(input("x2:"))
aa=int(input("y2:"))
sss=int(input("y3:"))
aaa=int(input("y3:"))
import turtle
turtle.shape("turtle")
turtle.up()
turtle.goto(s,a)
turtle.down()
turtle.goto(ss,aa)
turtle.goto(sss,aaa)
turtle.done()

import turtle

turtle.Turtle()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.done()
'''


pls = int(input("정수를 입력하시오"))#1234

number = 0
number += pls//1000 #1
pls = pls%1000 #234

number += pls//100 #1+2=3
pls = pls%100 #34

number += pls//10 #3+3=6
number += pls%10 #6+4=10

print("자리 수의 합", number)






