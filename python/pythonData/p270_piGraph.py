#!/usr/bin/env python

import matplotlib.pyplot as plt

plt.rcParams['font.family']= 'NanumBarunGothic'

slices = [1,2,3,4]
hobbies = ['잠자기','외식','여행','운동']
mycolors = ['blue','#6Aff00','green','#ff003c']

plt.pie(x=slices, labels=hobbies, shadow=mycolors, explode=[0,0.1,0,0], colors=mycolors, autopct='%1.2f%%',startangle=90, counterclock=False)

plt.legend(loc=4)

filename= 'p270_piGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'saved...')
plt.show()