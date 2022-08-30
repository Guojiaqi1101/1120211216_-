import math
import numpy as np
import CBSR
from numpy.fft import fft, fftfreq
def SNR_simulation(x1,a,b,h):
    fs=10000   # 采样频率
    f0=60      # 样本数目
    N=4000     # 故障频率大小
    x2=CBSR.srrr(a,b,h,x1)
    y=abs(fft(x2,N))
    # y=y/(N//2)
    # py=y[0:N//2]
    py=y*y.conjugate()/N
   #py=np.multiply(y,y.conjugate())/N
    #print('py',py)
    #G=sum(py[1:(N//20)-1])
    # print('G',G)
    Frequence=np.linspace(0,fs/2-fs/N,2000)
    T=np.argwhere(Frequence==f0)
    H=py[T]
    # print('T',T[0,0])
    # print('H',H)
    #GG=G-H
    # G=sorted(py,reverse=True)
    # GG=G[1]
    # print(H,GG)
    G=0
    for i in range(1,N//2):
        G=G+py[i]
    GG=G-H
    SNR=10*np.log10(H/GG)
    # print('GG',GG)
    if np.isnan(SNR):
        SNR=-1000  
    return SNR

def SNR_true(x1,a,b,h):
    fs=12000  # 采样频率
    N=4000    # 样本数目
    f0=156    # 故障频率大小
    x2=CBSR.srrr(a,b,h,x1)
    y=abs(fft(x2,N))
    # y=y/(N//2)
    # py=y[0:N//2]
    #py=y*y.conjugate()/N
    py=np.multiply(y,y.conjugate())/N
    #print('py',py)
    #G=sum(py[0:N//20])
    G=0
    for i in range(1,N//2):
        G=G+py[i]
    # print('G',G)
    Frequence=np.linspace(0,fs/2-fs/N,2000)
    T=np.argwhere(Frequence==f0)
    H=py[T[0,0]]
    # print('T',T[0,0])
    # print('H',H)
    GG=G-H
    # G=sorted(py,reverse=True)
    # GG=G[0]
    print(H,GG)
    SNR=10*np.log10(H/GG)
    # print('GG',GG)
    if np.isnan(SNR):
        SNR=-1000  
    return SNR