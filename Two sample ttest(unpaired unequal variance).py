from scipy import stats

x=[58,96,75,45,69,85,76,63]
y=[45,86,74,96,12,35,65,64]

#without scipy
n1=len(x)
n2=len(y)
mean1=sum(x)/n1
mean2=sum(y)/n2

def var(data, mean, n):
  v=0
  for i in data:
    v+=(i-mean)**2
  v=v/(n-1)
  return v

v1=var(x,mean1,n1)
v2=var(y,mean2,n2)

f_stat=v2/v1
f_critic=1.83
if f_stat<f_critic:
  print("Equal variance")
else:
  print("Unequal variance")

t_stat=(mean1-mean2)/((v1/n1+v2/n2)**0.5)
t_critic=1.83
if t_stat<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")

#using scipy
t,p=stats.ttest_ind(x,y,equal_var=False)
if t<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")   
