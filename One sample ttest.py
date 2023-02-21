from scipy import stats

x=[90,89.56,78,99,86,65]

#without using scipy
n=len(x)
mean=sum(x)/n
v=0
for i in x:
    v+=(i-mean)**2
v=v/(n-1)
t_stat=(mean-x[0])/(v/(n**0.5))
t_critic=1.83
if t_stat<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")

#with using scipy
t,p=stats.ttest_1samp(x,x[0])
if t<t_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")
          
