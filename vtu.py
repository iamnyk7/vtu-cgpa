mark=[]
print("VTU CSE 4TH SEM SGPA CALCULATOR")
sub1=['18MAT31',"SUB 2(4 credit)","SUB 3","SUB 4","SUB 5","SUB 6","LAB1","LAB2","(KAN/CIP)"]
for i in range (9):
        print("Enter",sub1[i],"External Marks")
        mark.append(int(input()))
def con(mark,num):
    listc=[]
    for item in mark:
        ele=item*50
        con=ele/num
        listc.append(con)
    return listc
def avg(listc):
    sum=0
    for item in listc:
        sum+=item
    return sum/9
print("You had kannada press y if you had else n")
choice=input()
if choice=='y':
    mark[8]=(mark[8]*60)/100
k=con(mark,60)
avg=avg(k)

cie=[]
sub2=["18MAT41","SUB 2(4 credit)","SUB3 ","SUB4","SUB5","SUB6","LAB1","LAB2",'CIP/KANNADA']
print("INTERNAL MARKS 4TH SEM")
for i in range (9):
        print("Enter",sub2[i],"marks")
        cie.append(int(input()))
m=con(cie,40)
def add(list,avg):
    fmarks=[]
    for item in list:
        sum=item+avg
        fmarks.append(sum)
    return fmarks
marks=add(m,avg)

def cgpa(marks):
    grade=[]
    for item in marks:
       if item>=90:
           grade.append(10)
       elif item>=80:
           grade.append(9)
       elif item>=70:
           grade.append(8)
       elif item>=60:
           grade.append(7)
       elif item>=50:
           grade.append(6)
       else:
           grade.append(5)
    m1= grade[0]*3
    m2= grade[1]*4
    m3 = grade[2] * 3
    m4 = grade[3] * 3
    m5 = grade[4] * 3
    m6 = grade[5] * 3
    m7 = grade[6] * 2
    m8 = grade[7] * 2
    m9=grade[8]*1
    fo=(m1+m2+m3+m4+m5+m6+m7+m8+m9)/24
    return fo
# cgpa=cgpa(marks)
# print("SGPA IS",cgpa)
# print("Created by santhosh Nayak")
