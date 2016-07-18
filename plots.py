## plotting utils 
## Author: Zichen Wang
## 3/27/2014

import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42 ## Output Type 3 (Type3) or Type 42 (TrueType)
rcParams['font.sans-serif'] = 'Arial'


COLORS10 = [
'#1f77b4',
'#ff7f0e',
'#2ca02c',
'#d62728',
'#9467bd',
'#8c564b',
'#e377c2',
'#7f7f7f',
'#bcbd22',
'#17becf',
]

def enlarge_tick_fontsize(ax,fontsize):
	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(fontsize)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(fontsize)
