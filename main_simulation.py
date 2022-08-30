import matplotlib.pyplot as plt
from numpy import pi, sin, linspace
from numpy.fft import fft, fftfreq
import generate_white_noise as noise
import math
import CBSR 
import find_best as search
import numpy as np
# %%仿真信号
# clear all clc close all
fs=10000
f0=60
Ts=1/fs
N=4000
t = linspace(0,(N-1)/fs,4000)
f = linspace(0,fs/2-fs/N,2000)
T=np.argwhere(f==f0)
A=0.25
D=10
x1=A*sin(2*pi*f0*t)
Ampx1=abs(fft(x1,N))
Ampx1=Ampx1/(N//2)
Ampx1=Ampx1[0:N//2]

noise=noise.wgn(N)
# arr_mean = np.mean(noise)
# arr_var = np.var(noise)
# print('mean',arr_var)
x2=x1+math.sqrt(2*D)*noise
Ampx2=abs(fft(x2,N))
Ampx2=Ampx2/(N//2)
Ampx2=Ampx2[0:N//2]

ax = plt.gca()
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
#指定坐标的位置
ax.xaxis.set_ticks_position('bottom') # 设置bottom为x轴
ax.yaxis.set_ticks_position('left') # 设置left为x轴
ax.spines['bottom'].set_position(('data',0))#这个位置的括号要注意
ax.spines['left'].set_position(('data',0))
x=f[T[0]]
y=Ampx1[T[0]]
plt.annotate("Falut Frequence", (f[T],Ampx1[T]),xytext=(+30,-30),arrowprops=dict(arrowstyle='->'),textcoords='offset points') 
#plt.text(x,y,(x,y),color='r')
print(x,y)


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


fsr=10
h=1/fsr
print(N)
#粒子群寻优
[Gbest,result]=search.PSO_simulation(x2,h)
a=Gbest[0]
b=Gbest[1]
print(a,b)
print(result)
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
