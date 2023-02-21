from scipy import stats

x=[12,45,63,44,23,16,32]
y=[23,62,12,45,32,63,25]

#without using scipy
n=len(x)
d=0
d_square=0
for i in range(n):
  d+=x[i]-y[i]
  d_square+=(x[i]-y[i])**2
f_stat=d/((n*d_square-d**2)/n-1)
f_critic=1.83
if f_stat<f_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")

#with using scipy
f,p=stats.ttest_rel(x,y)
if f<f_critic:
    print("Null hpothesis is accepted")
else:
    print("Null hpothesis is rejected")