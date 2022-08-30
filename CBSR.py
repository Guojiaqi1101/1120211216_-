import numpy as np
import warnings
# warnings.filterwarnings("ignore")
def srrr(a,b,h,x1):
	# warnings.filterwarnings("ignore")
	np.seterr(divide='ignore',invalid='ignore')
	x=np.zeros(len(x1),dtype=float)
	x.dtype='float64'
	# print(len(x1))
	for i in range(1,len(x1)):
		# print('CBSR_i',i)
		k1=h*(a*x[i-1]-b*x[i-1]**3+x1[i-1])
		k2=h*(a*(x[i-1]+k1/2)-b*(x[i-1]+k1/2)**3+x1[i-1])
		k3=h*(a*(x[i-1]+k2/2)-b*(x[i-1]+k2/2)**3+x1[i])
		k4=h*(a*(x[i-1]+k3)-b*(x[i-1]+k3)**3+x1[i])
		x[i]=x[i-1]+(1/6)*(k1+2*k2+2*k3+k4)
		#x[i]=np.around(x[i],6)
	return x
