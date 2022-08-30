import numpy as np
import matplotlib.pyplot as plt

def  wgn(N):
	noise = np.random.randn(N)
	return noise