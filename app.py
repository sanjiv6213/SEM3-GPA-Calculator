import streamlit as st
import pandas as pd

st.title("!!GPA Calculator!!")

st.subheader("Enter your Probability and Statistics Grade:")
a=st.selectbox("Grade",("O","A+","A","B+","B","C"))
if (a=="O"):
    b=10*4
elif (a=="A+"):
    b=9*4
elif (a=="A"):
    b=8*4
elif (a=="B+"):
    b=7*4
elif (a=="B"):
    b=6*4
elif (a=="C"):
    b=5*4
else:
    b="RA"
st.write("Your Grade Point",b)

st.subheader("Enter your Data Structures Grade:")
c=st.selectbox("grade",("O","A+","A","B+","B","C"))
if (c=="O"):
    d=10*3
elif (c=="A+"):
    d=9*3
elif (c=="A"):
    d=8*3
elif (c=="B+"):
    d=7*3
elif (c=="B"):
    d=6*3
elif (c=="C"):
    d=5*3
else:
    d="RA"
st.write("Your Grade Point",d)

st.subheader("Enter your Computer Organisation and Architecture Grade:")
e=st.selectbox("GRADE",("O","A+","A","B+","B","C"))
if e=="O":
    f=10*3
elif e=="A+":
    f=9*3
elif e=="A":
    f=8*3
elif e=="B+":
    f=7*3
elif e=="B":
    f=6*3
elif e=="C":
    f=5*3
else:
    f="RA"
st.write("Your Grade Point",f)

st.subheader("Enter your Introduction to AI Grade:")
g=st.selectbox("GRADE.",("O","A+","A","B+","B","C"))
if g=="O":
    h=10*3
elif g=="A+":
    h=9*3
elif g=="A":
    h=8*3
elif g=="B+":
    h=7*3
elif g=="B":
    h=6*3
elif g=="C":
    h=5*3
else:
    h="RA"
st.write("Your Grade Point",h)

st.subheader("Enter your Foundation of Data Science Grade:")
i=st.selectbox("Grade.",("O","A+","A","B+","B","C"))
if i=="O":
    j=10*3
elif i=="A+":
    j=9*3
elif i=="A":
    j=8*3
elif i=="B+":
    j=7*3
elif i=="B":
    j=6*3
elif i=="C":
    j=5*3
else:
    j="RA"
st.write("Your Grade Point",j)

st.subheader("Enter your OOPS Grade:")
k=st.selectbox(".grade",("O","A+","A","B+","B","C"))
if k=="O":
    l=10*4
elif k=="A+":
    l=9*4
elif k=="A":
    l=8*4
elif k=="B+":
    l=7*4
elif k=="B":
    l=6*4
elif k=="C":
    l=5*4
else:
    l="RA"
st.write("Your Grade Point",l)

st.subheader("Enter your Data Structures LAB using python Grade:")
m=st.selectbox(".Grade",("O","A+","A","B+","B","C"))
if m=="O":
    n=10*2
elif m=="A+":
    n=9*2
elif m=="A":
    n=8*2
elif m=="B+":
    n=7*2
elif m=="B":
    n=6*2
elif m=="C":
    n=5*2
else:
    n="RA"
st.write("Your Grade Point",n)

st.subheader("Enter your AI LAB Grade:")
o=st.selectbox(".grade.",("O","A+","A","B+","B","C"))
if o=="O":
    p=10*2
elif o=="A+":
    p=9*2
elif o=="A":
    p=8*2
elif o=="B+":
    p=7*2
elif o=="B":
    p=6*2
elif o=="C":
    p=5*2
else:
    p="RA"
st.write("Your Grade Point",p)

total=b+d+f+h+j+l+n+p
result=total/24

st.subheader("GPA")

st.write("GPA =",result)

l1=["Probability and Statistics","Data Structures","Computer Organisation and Architecture","Introduction to AI","Foundation of Data Science","OOPS","Data Structures LAB using python"," AI LAB"]
l2=[4,3,3,3,3,4,2,2]
l3=[a,c,e,g,i,k,m,o]
l4=[b,d,f,h,j,l,n,p]

tab=pd.DataFrame(list(zip(l1,l2,l3,l4)))

tab.columns =['Subject','Credits', 'Grade', 'Grade Points Earned']

st.table(tab)

st.write("GPA =",total,"/",24)

st.success(result)