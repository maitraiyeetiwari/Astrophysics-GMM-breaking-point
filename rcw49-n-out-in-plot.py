import matplotlib.pyplot as plt
import numpy as np

n_input = [2,4,6,8,10,12,14,16,18,20]
n_output = [2,4,6,7,8,8.9,10.7,10.8,11,12.4]
n_err = [0,0,0,1.05,0.82,0.88,1.25,1.87,1.63,0.84]


n_input_array = np.array(n_input)
n_output_array = np.array(n_output)
n_err_array = np.array(n_err)





#plt.plot(n_input_array, n_output_array,'o-',color='blue')
#plt.plot(n_input_array, n_output_array - ((n_err_array)/2),'-',color='lightblue')
#plt.plot(n_input_array, n_output_array + ((n_err_array)/2),'-',color='lightblue')


#plt.fill_between(n_input_array, n_output_array - ((n_err_array)/2),n_output_array + ((n_err_array)/2))

plt.errorbar(n_input_array, n_output_array, yerr = n_err_array, fmt='o', color='blue',
             ecolor='lightgray', elinewidth=3, capsize=0)


plt.axvline(x = 16, color = 'black',ls=':')

#plt.fill_between(n_input_array, n_output_array - n_err_array, n_output_array - n_err_array,color='gray', alpha=0.2)
#plt.plot(60,10,'+',color='red')

plt.xlabel('$n_{input}$',fontsize=12)
plt.ylabel('$n_{output}$',fontsize=12)
#plt.title('RCW 120',fontsize=12)

plt.text(2, 13, 'RCW 49',fontsize=12)
plt.text(9.2, 6, 'first breaking point',fontsize=12)


plt.savefig('rcw49-n-out-in-plot.png',dpi=500,bbox_inches='tight')
#plt.show()