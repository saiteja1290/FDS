from scipy import stats

x1=[13,14,75,65,42,36]
x2=[45,65,53,86,47,65,23,54]
x3=[45,36,47,96,65,52.23,21]

#without using scipy
n1=len(x1)
n2=len(x2)
n3=len(x3)
mean1=sum(x1)/n1
mean2=sum(x2)/n2
mean3=sum(x3)/n3
k=3
n=n1+n2+n3
mean=(sum(x1)+sum(x2)+sum(x3))/n

def div(data, mean):
  v=0
  for i in data:
    v+=(i-mean)**2
  return v

msw=(div(x1,mean1)+div(x2,mean2)+div(x3,mean3))/(n-k)
msb=(n1*((mean1-mean)**2)+n2*((mean2-mean)**2)+n3*((mean3-mean)**2))/(k-1)

f_stat=msb/msw
print(f_stat)
f_critic=1.83

if f_stat<f_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")

#using scipy
f,p=stats.f_oneway(x1,x2,x3)
print(f)
if f<f_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")