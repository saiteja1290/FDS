from scipy import stats

x=[12,13,48,65,15,45,23,25]
y=[42,32,65,12,32,14,25,26]

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

v1=var(x, mean1, n1)
v2=var(y, mean2, n2)

#pooled variance
s=0
for i in x:
  s+=(i-mean1)**2
for i in y:
  s+=(i-mean2)**2
s=s/(n1+n2-2)

f_stat=v2/v1
f_critic=1.83
if f_stat<f_critic:
  print("Equal variance")
else:
  print("Unequal variance")

t_stat=(mean1-mean2)/((s*(1/n1+1/n2))**0.5)
t_critic=1.83
if t_stat<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")

#using scipy
t,p=stats.ttest_ind(x,y,equal_var=True)
if t<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")