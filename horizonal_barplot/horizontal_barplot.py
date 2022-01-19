import matplotlib.pyplot as plt  
import numpy as np 

from natsort import natsorted
from matplotlib import gridspec


def beautify_axes(array_of_axes):
    for ax in array_of_axes:
        ax.spines['top'].set_visible(True)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False) 
        ax.spines['bottom'].set_color(axes_font_color)
        ax.spines['top'].set_color(axes_font_color)
        ax.spines['left'].set_color(axes_font_color)
        ax.spines['right'].set_color(axes_font_color)
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top') 
        ax.tick_params(axis='y', colors='k', left=False) # left=False to hide ticks
        ax.tick_params(axis='x', colors=axes_font_color)
        ax.spines['left'].set_position(('outward', 8))
        ax.spines['top'].set_position(('outward', 5))
        # ax.spines['bottom'].set_position(('outward', 5))
        # adjust_spines(ax, ['left', 'bottom'])
        ax.yaxis.set_label_coords(-0.1,1.1)



# Set default values
default_font_size = 8
axes_font_color = '#363636'
mrkr_size = 5
line_width = 1
thin_line_width = 0.5
graph_letter_x_offset = -0.1
graph_letter_y_offset = -0.45

fig_width = 3.25 # inches
fig_height = 1.66 # 1.66 inch per plot)

plt.rcParams.update({'font.size': 8,
                        'legend.frameon': False, 
                        'font.style':'normal',
                        'font.weight':'normal',
                        'font.family': 'serif',
                        'font.serif': 'Times new Roman',
                        'mathtext.fontset':'stix'})


fig = plt.figure()
fig.set_size_inches(fig_width,fig_height)
gs = gridspec.GridSpec(1, 1)
ax1 = plt.subplot(gs[0])



# Your data
items = [
    {'name': "Liam", 'age': 55},
    {'name': "Olivia", 'age': 35},
    {'name': "Noah", 'age': 45},
    {'name': "Emma", 'age': 28},
    {'name': "Oliver", 'age': 19},
    {'name': "Isabella", 'age': 60},
]


# Sort data
sorted_items = sorted(items, key = lambda i: i['age'], reverse=True)
sorted_labels = [d['name'] for d in sorted_items]
sorted_values = [d['age'] for d in sorted_items]


y_pos = np.arange(len(sorted_labels))
max_x = np.max(sorted_values) * 1.1 # make 10% wider


# Plot data
plot_numbers_flush_right = True 

if plot_numbers_flush_right:
    # plot all values flush right
    for y in y_pos: 
        ax1.plot([0,max_x],[y,y], color="#a8a8a8", linewidth=thin_line_width, zorder=0) # without error
        ax1.barh(y, sorted_values[y], color="#0072B2", height=0.4, zorder=1) # without error
        ax1.text(max_x,y,"   {}".format(sorted_values[y]), verticalalignment='center')
else:
    # Plot all values nex to the bar
    for y in y_pos:
        ax1.barh(y, sorted_values[y], color="#0072B2", height=0.4, zorder=1) # without error
        ax1.text(sorted_values[y],y,"   {}".format(sorted_values[y]), verticalalignment='center')



ax1.set_yticks(y_pos)
ax1.set_yticklabels(sorted_labels)
ax1.invert_yaxis()  # labels read top-to-bottom
ax1.set_xlabel('Age (years)')
ax1.set_xlim(0,max_x)

beautify_axes([ax1])

plt.subplots_adjust(top=0.687,
bottom=0.081,
left=0.201,
right=0.904,
hspace=0.2,
wspace=0.2)

plt.savefig('{}.png'.format("horizontal_barplot"),dpi=600)

plt.show()
