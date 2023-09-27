import matplotlib.pyplot as plt
import numpy as np

n_input = [2,4,6,8,10,12,14,16,18,20]

n_output = [1.8,3.2,3.3,3.4,4.1,4.8,4.4,5.3,4.9,5.3]

n_err = [0.45,0.45,0.48,0.52,0.7,0.8,0.9,0.9,0.7,0.9]

n_slope = [0.9,0.7, 0.05,0.05, 0.35,0.35,-0.2,0.45,-0.2,0.2]


n_input_array = np.array(n_input)
n_output_array = np.array(n_output)
n_err_array = np.array(n_err)





#plt.plot(n_input_array, n_output_array,'o-',color='blue')
#plt.plot(n_input_array, n_output_array - ((n_err_array)/2),'-',color='lightblue')
#plt.plot(n_input_array, n_output_array + ((n_err_array)/2),'-',color='lightblue')


#plt.fill_between(n_input_array, n_output_array - ((n_err_array)/2),n_output_array + ((n_err_array)/2))

#plt.errorbar(n_input_array, n_output_array, yerr = n_err_array, fmt='o', color='blue',
#             ecolor='lightgray', elinewidth=3, capsize=0)

plt.plot(n_input, n_slope,'-',color='blue')


plt.axvline(x = 14, color = 'black',ls=':')

#plt.fill_between(n_input_array, n_output_array - n_err_array, n_output_array - n_err_array,color='gray', alpha=0.2)
#plt.plot(60,10,'+',color='red')

plt.xlabel('$n_{input}$',fontsize=12)
plt.ylabel('$n_{output}$',fontsize=12)
#plt.title('RCW 120',fontsize=12)

plt.text(2, 0.8, 'RCW 120',fontsize=12)
plt.text(14.3, 0.8, 'first breaking point',fontsize=12)


plt.savefig('rcw120-n-out-in-slope-plot.png',dpi=500,bbox_inches='tight')
#plt.show()