import numpy as np
import SNR
def PSO_simulation(x1,h):
    N=30         #粒子个数
    D=2          #粒子维数
    T=30         #最大迭代次数
    C1=1.5        #因子
    C2=1.5        #学习因子
    MaxInertia=0.8 #惯性权重最大值
    MinInertia=0.4 #惯性权重最小值
    MaxVelocity=5 #速度最大值
    MinVelocity=-5#速度最小值
    Location=5*np.random.rand(N,D)  #初始化位置
    Velocity=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(N,D)  #初始化速度
    Pbest=5*np.random.rand(N,D)    #个体最佳初始化
    FitPbest=np.zeros(N,dtype=complex)
    fit=np.zeros(N,dtype=complex)
    result=np.zeros(T,dtype=complex)
    result1=np.zeros(T,dtype=float)
    for i in range(N):
        a=Pbest[i,0]
        b=Pbest[i,1]
        FitPbest[i]=SNR.SNR_simulation(x1,a,b,h)
 
    Gbest=5*np.random.rand(D)    #群体最佳初始化
    FitGbest=SNR.SNR_simulation(x1,Gbest[0],Gbest[1],h)
    t=1
    while t<=T:
        w=MaxInertia-(MaxInertia-MinInertia)*t/T
        for i in range(N):
            #避免陷入局部最优，当粒子位置与群体最佳一致时
            if (Location[i,:]==Gbest).all():
                Location[i,:]=5*np.random.rand(1,D)    
            #速度更新
            Velocity[i,:]=w*Velocity[i,:]+C1*np.random.rand(1)*(Pbest[i,:]-Location[i,:])+C2*np.random.rand(1)*(Gbest-Location[i,:])
            #避免速度太大，超出速度限制
            x=np.argwhere(Velocity[i,:]>MaxVelocity)  #大于最大速度
            y=np.argwhere(Velocity[i,:]<MinVelocity)  #小于最小速度
            Velocity[i,x]=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(1)          #超出最大速度设为最大速度
            Velocity[i,y]=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(1)          #超出最小速度设为最小速度
            #粒子更新
            Location[i,:]=Location[i,:]+Velocity[i,:]
            for j in range(D):
                if Location[i,j]<=0 or Location[i,j]>5:
                    Location[i,j]=5*np.random.rand(1)
            fit[i]=SNR.SNR_simulation(x1,Location[i-1,0],Location[i-1,1],h)
            if fit[i]>FitPbest[i]:           #替换个体最优
                 FitPbest[i]=fit[i]
                 Pbest[i,:]=Location[i,:]
        G=max(FitPbest)
        if FitGbest<G :         #替换群体最优
            FitGbest=max(FitPbest)
            row=np.argwhere(FitPbest==max(FitPbest))
            Gbest=Location[row[0,0],:]
        result[t-1]=FitGbest
        result1[t-1]=np.around(result[t-1].real,6)
        # print('FitGbest',FitGbest)
        print(t)
        # print(result)
        t=t+1
    # disp(Pbest)
    # disp(FitPbest)
    # disp(FitGbest)
    # figure(2)
    # plot(result)
    return [Gbest,result1]


def PSO_true(x1,h):
    N=30         #粒子个数
    D=2          #粒子维数
    T=30         #最大迭代次数
    C1=1.5        #因子
    C2=1.5        #学习因子
    MaxInertia=0.8 #惯性权重最大值
    MinInertia=0.4 #惯性权重最小值
    MaxVelocity=2 #速度最大值
    MinVelocity=-2#速度最小值
    Location=5*np.random.rand(N,D)  #初始化位置
    Velocity=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(N,D)  #初始化速度
    Pbest=5*np.random.rand(N,D)    #个体最佳初始化
    FitPbest=np.zeros(N,dtype=complex)
    fit=np.zeros(N,dtype=complex)
    result=np.zeros(T,dtype=complex)
    result1=np.zeros(T,dtype=float)
    for i in range(N):
        a=Pbest[i,0]
        b=Pbest[i,1]
        FitPbest[i]=SNR.SNR_true(x1,a,b,h)
 
    Gbest=5*np.random.rand(D)    #群体最佳初始化
    FitGbest=SNR.SNR_true(x1,Gbest[0],Gbest[1],h)
    t=1
    while t<=T:
        w=MaxInertia-(MaxInertia-MinInertia)*t/T
        for i in range(N):
            #避免陷入局部最优，当粒子位置与群体最佳一致时
            if (Location[i,:]==Gbest).all():
                Location[i,:]=5*np.random.rand(1,D)    
            #速度更新
            Velocity[i,:]=w*Velocity[i,:]+C1*np.random.rand(1)*(Pbest[i,:]-Location[i,:])+C2*np.random.rand(1)*(Gbest-Location[i,:])
            #避免速度太大，超出速度限制
            x=np.argwhere(Velocity[i,:]>MaxVelocity)  #大于最大速度
            y=np.argwhere(Velocity[i,:]<MinVelocity)  #小于最小速度
            Velocity[i,x]=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(1)          #超出最大速度设为最大速度
            Velocity[i,y]=MinVelocity+(MaxVelocity-MinVelocity)*np.random.rand(1)          #超出最小速度设为最小速度
            #粒子更新
            Location[i,:]=Location[i,:]+Velocity[i,:]
            for j in range(D):
                if Location[i,j]<=0 or Location[i,j]>5:
                    Location[i,j]=5*np.random.rand(1)
            fit[i]=SNR.SNR_true(x1,Location[i-1,0],Location[i-1,1],h)
            if fit[i]>FitPbest[i]:           #替换个体最优
                 FitPbest[i]=fit[i]
                 Pbest[i,:]=Location[i,:]
        G=max(FitPbest)
        if FitGbest<G :         #替换群体最优
            FitGbest=max(FitPbest)
            row=np.argwhere(FitPbest==max(FitPbest))
            Gbest=Location[row[0,0],:]
        result[t-1]=FitGbest
        result1[t-1]=np.around(result[t-1].real,6)
        # print('FitGbest',FitGbest)
        print(t)
        # print(result)
        t=t+1
    # disp(Pbest)
    # disp(FitPbest)
    # disp(FitGbest)
    # figure(2)
    # plot(result)
    return [Gbest,result1]
