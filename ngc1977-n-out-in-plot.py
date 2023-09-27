import matplotlib.pyplot as plt
import numpy as np

n_input = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
n_output = [1,3.4,4.3,4.7,4.9,5.8,6.0,6.4,6.2,7.1,7.7,8,8.2,8.6,8.8]
n_err = [0,0.52,0.82,0.67,0.88,1.55,0.92,0.7,1.03,0.88,0.67,1.4,1.03,1.35,1.69]


n_input_array = np.array(n_input)
n_output_array = np.array(n_output)
n_err_array = np.array(n_err)





#plt.plot(n_input_array, n_output_array,'o-',color='blue')
#plt.plot(n_input_array, n_output_array - ((n_err_array)/2),'-',color='lightblue')
#plt.plot(n_input_array, n_output_array + ((n_err_array)/2),'-',color='lightblue')


#plt.fill_between(n_input_array, n_output_array - ((n_err_array)/2),n_output_array + ((n_err_array)/2))

plt.errorbar(n_input_array, n_output_array, yerr = n_err_array, fmt='o', color='blue',
             ecolor='lightgray', elinewidth=3, capsize=0)


plt.axvline(x = 18, color = 'black',ls=':')

#plt.fill_between(n_input_array, n_output_array - n_err_array, n_output_array - n_err_array,color='gray', alpha=0.2)
#plt.plot(60,10,'+',color='red')

plt.xlabel('$n_{input}$',fontsize=12)
plt.ylabel('$n_{output}$',fontsize=12)
#plt.title('RCW 120',fontsize=12)

plt.text(2, 10.1, 'NGC 1977',fontsize=12)
plt.text(19, 5, 'first breaking point',fontsize=12)


plt.savefig('ngc1977-n-out-in-plot.png',dpi=500,bbox_inches='tight')
#plt.show()