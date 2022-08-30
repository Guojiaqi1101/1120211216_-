import matplotlib.pyplot as plt
from numpy import pi, sin, linspace
from numpy.fft import fft, fftfreq
import generate_white_noise as noise
import math
import CBSR 
import find_best as search
import numpy as np
import import_data
fs=12000  # 采样频率
N=4000    # 样本数目
f0=156    # 故障频率大小
t = linspace(0,(N-1)/fs,4000)
f = linspace(0,fs/2-fs/N,2000)

D=3
noise=noise.wgn(N)
signal=import_data.read_date(N)
x1=(signal-np.mean(signal))/np.std(signal);
Ampx1=abs(fft(x1,N))
Ampx1=Ampx1/(N//2)
Ampx1=Ampx1[0:N//2]
x2=x1+math.sqrt(2*D)*noise
Ampx2=abs(fft(x2,N))
Ampx2=Ampx2/(N//2)
Ampx2=Ampx2[0:N//2]

T=np.argwhere(f==f0)
plt.figure(1)
plt.title("原始信号")
plt.subplot(211)
plt.plot(t,x1,linewidth=1)
plt.xlabel('t')
plt.ylabel('amplitude')
plt.subplot(212)
plt.plot(f,Ampx1,linewidth=1)
plt.xlabel('f')
plt.ylabel('amplitude')
plt.annotate("Falut Frequence", (f[T],Ampx1[T]),xytext=(+30,-30),arrowprops=dict(arrowstyle='->'),textcoords='offset points') 

plt.figure(2)
plt.title("加噪信号")
plt.subplot(211)
plt.plot(t,x2,linewidth=1)
plt.xlabel('t')
plt.ylabel('amplitude')
plt.subplot(212)
plt.plot(f,Ampx2,linewidth=1)
plt.xlabel('f')
plt.ylabel('amplitude')
plt.annotate("Falut Frequence", (f[T],Ampx2[T]),xytext=(+30,-30),arrowprops=dict(arrowstyle='->'),textcoords='offset points') 

fsr=6
h=1/fsr
print(N)
# 粒子群寻优
[Gbest,result]=search.PSO_true(x2,h)
a=Gbest[0]
b=Gbest[1]
# a=1
# b=1
# print(a,b)
# print(result)
x0=CBSR.srrr(a,b,h,x2)   #数值求解多稳态随机共振方程
print('x0',x0)
Ampx0=abs(fft(x0,N))/(N//2)
Ampx0=Ampx0[0:N//2]
#输出信号
plt.figure(3)
plt.subplot(211)
plt.plot(t,x0,linewidth=1)
plt.xlabel('t')
plt.ylabel('amplitude')
plt.subplot(212)
plt.plot(f,Ampx0,linewidth=1)
plt.xlabel('f')
plt.ylabel('amplitude')
plt.annotate("Falut Frequence", (f[T],Ampx0[T]),xytext=(+30,-30),arrowprops=dict(arrowstyle='->'),textcoords='offset points') 

plt.figure(4)
plt.plot(result,linewidth=1)
plt.xlabel('T')
plt.ylabel('fit')

plt.show()
