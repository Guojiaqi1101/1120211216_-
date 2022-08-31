随机共振检测故障信号
=
本系统用于检测微弱故障信号，与传统微弱信号检测方法不同，本系统使用随机共振放大故障信号，将降噪变为用噪，为了优化系统的效果，使用粒子群算法优化随机共振模型参数。

# 文件介绍

* `212.xlsx`：美国西储大学实验数据
* `main_simulation.py`：仿真信号主函数
* `main_true.py`：美国西储大学实验数据主函数
* `generate_white_noise.py`：生成高斯白噪声文件
* `import_data.py`：导入美国西储大学数据文件
* `find_best.py`：粒子群算法优化参数文件
* `CBSR.py`：四阶龙格库塔数值求解文件
* `SNR.py`：计算信噪比文件

# 使用说明
运行`main_simulation.py`文件得到仿真信号检测图像，运行`main_true.py`文件得到美国西储大学实验数据检测图像。

# 运行结果

## 仿真信号
设驱动信号为𝑠(𝑡)=𝐴sin(2𝜋𝑓𝑡)，其中信号幅值为0.25，频率为60Hz，噪声强度为4，采样频率为10000Hz，下图为为添加噪声的原始信号，上面的图为时域图，下面的图为频域图。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure11.png"  /></div>
下图为添加高斯白噪声后的时域图和频域图，可以看出信号的特征明显被噪声干扰，在噪声中淹没，并且序列杂乱，频谱图中突显不出驱动信号的频率，高频区域的幅值较高，幅值无法区别于低频区
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure21.png"  /></div>
由于随机共振需满足绝热近似原理的小参数要求，需要对原信号进行变尺度。通过粒子群优化算法得到最优的参数，下图为经过粒子群算法优化的随机共振检测结果，观察下图可发现，信号经过粒子群优化的双稳随机共振模型后，时域图中的特征明显，噪声干扰减小，波形被调制，更接近周期正弦信号，频域图中高频区的幅值明显减小，低频信号的幅值增加，并且输入信号的频率能在频域图中突显出来。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure31.png"  /></div>
下图为粒子群算法迭代过程中的适应值变化曲线。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure41.png"  /></div>

## 美国西储大学实验数据
西储大学的实验装置的采样频率为12kHz，转速为1728r/min。表3-1详细地显示了驱动滚子轴承的尺寸。以内圈故障为例，内圈故障频率的理论值为155.96Hz。由于随机共振是在绝热近似理论条件下实现的，工程中的故障频率通常是几十赫兹或几百赫兹，为解决高频信号的随机共振问题，需要进行二次采样，二次采样频率为6Hz。通过计算得其转频28.8Hz，特征频率156Hz。

下图显示了轴承内圈故障信号的波形和频谱。上图包含了周期性冲击和振动的波形，在下图的频谱中，谱能量分布在宽频率范围内，峰值范围为1-2kHz。这种冲击是轴承部件的第一次自然模式振动，因此在原始信号的频谱图中，低频部分看不到明显的故障信号的振动特性。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure12.png"  /></div>
通过粒子群优化算法得到最优的参数，通过观察下图发现，经过自适应随机共振系统后，检测出来内圈故障的频率为156Hz，接近理论值155.96Hz。并且经过随机共振后，特征频率处的幅值更加突出，信号幅值更集中，这表明噪声将更多能量传递给故障信号，增加其在故障频率处的振幅并在频谱中突出显示。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure32.png"  /></div>
下图为粒子群算法迭代过程中的适应值变化。
<div align=center><img src="https://github.com/Guojiaqi1101/picture/blob/main/Figure42.png"  /></div>
