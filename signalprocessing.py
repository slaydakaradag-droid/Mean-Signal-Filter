import numpy as np 
time = np.linspace(0,2*np.pi,200)
sin_result = np.sin(time)
print(sin_result)
noise = np.random.normal (loc = 0 , scale= 0.2 , size = 200)
noisy_signal = sin_result+noise
print(noisy_signal)
filtered_signal = []
window_size = 5
for i in range(len(noisy_signal)-window_size+1):
 window = noisy_signal[i : i+ window_size]
 window_mean = np.mean(window)
filtered_signal.append(window_mean)
filtered_signal = np.array(filtered_signal)
print(filtered_signal[:10])
#
results = ((sin_result[:len(filtered_signal)] - filtered_signal)*2)
mean = np.mean(results)
print(f'Filtreleme sonrası ortalama hata :',mean)

      


