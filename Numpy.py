import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)

#minimum
print("Minimum:", np.amin(a))
print("Minimum in each column:", np.amin(a,axis=0))
print("Minimum in each row:", np.amin(a,axis=1))

#maximum
print("Maximum:",np.amax(a))
print("Maximum in each column:", np.amax(a,axis=0))
print("Maximum in each row:", np.amax(a,axis=1))

#mean
print("Mean:", np.mean(a))
print("Mean in each column:", np.mean(a,axis=0))
print("Mean in each row:", np.mean(a,axis=1))

#median
print("Median:", np.median(a))
print("Median in each column:", np.median(a,axis=0))
print("Median in each row:", np.median(a,axis=1))

#standard deviation
print("Standard deviation:",np.std(a))
print("Standard deviation in each column:", np.std(a,axis=0))
print("Standard deviation in each row:", np.std(a,axis=1))

#variance
print("Variance:", np.var(a))
print("Variance in each column:", np.var(a,axis=0))
print("Variance in each row:", np.var(a,axis=1))

#average
#if the weight is not specified then the average is same as mean
wt=np.array([[1.5,1.5,1.5,1.5],[2,2,2,2]])
print("Average:", np.average(a,weights=wt))

#percentile
'''
it determines the percentile of the data along specified axis
syntax: np.percentile(array,q,axis)
q: it is the percentile which it calculates of the array elements between 0-100
'''
print("Percentile along axis 0:", np.percentile(a,6,0))
print("Percentile along axis 1:", np.percentile(a,6,1))

#peak to peak
print("PTP along axis 0:", np.ptp(a,0))
print("PTP along axis 0:", np.ptp(a,1))
