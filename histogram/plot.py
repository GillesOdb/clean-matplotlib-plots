import matplotlib.pyplot as plt  
import numpy as np

from natsort import natsorted
from matplotlib import gridspec

import math

def beautify_axes(array_of_axes):
    for ax in array_of_axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True) 
        ax.spines['bottom'].set_color(axes_font_color)
        ax.spines['left'].set_color(axes_font_color)
        ax.tick_params(axis='y', colors=axes_font_color)
        ax.tick_params(axis='x', colors=axes_font_color)
        adjust_spines(ax, ['left', 'bottom'])
        ax.yaxis.set_label_coords(-0.1,1.1)

def beautify_second_axes(array_of_axes):
    for ax in array_of_axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(True)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False) 
        ax.spines['bottom'].set_color(color_second_axis)
        ax.spines['right'].set_color(color_second_axis)
        ax.tick_params(axis='y', colors=color_second_axis)
        # ax.tick_params(axis='x', colors=axes_font_color)
        # adjust_spines(ax, ['right', 'bottom'])
        ax.yaxis.set_label_coords(1,1.37)

def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points
        else:
            spine.set_color('none')  # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])

def set_graph_letter(ax,letter):
    ax.set_title(letter, 
                    fontsize = default_font_size, 
                    loc='left', 
                    y=graph_letter_y_offset, 
                    x=graph_letter_x_offset, 
                    fontweight='bold')


def custom_errorbar_plot(ax, x_data, y_data, color):
    x_data = np.array(x_data, dtype="object")  
    y_data = np.array(y_data, dtype="object")

    x_len = x_data.size
    y_len = y_data.size

    if x_len != y_len:
        print("ERROR - Array sizes do not match")
        return

    i = 0
    # plot points
    for x in x_data:

        for y in y_data[i]:
            ax.plot(x,y,
                        '.',
                        color=color,
                        markersize=mrkr_size, 
                        linewidth=thin_line_width,
                        alpha=0.4)

        mean = np.mean(y_data[i])
        st_dev = np.std(y_data[i])
        ax.errorbar(x, mean, 
                        yerr=st_dev,
                        color=axes_font_color, 
                        elinewidth=0.7,
                        solid_capstyle='projecting', 
                        capsize=3)

        i+=1




# Set default values
default_font_size = 8
axes_font_color = '#363636' # grey
color_second_axis = '#009E73' # green
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

color_palette = ['#0072B2', 
                    '#009E73', 
                    '#D55E00', 
                    '#CC79A7', 
                    '#F0E442', 
                    '#56B4E9'] #seaborn colorblind


fig = plt.figure()
# portrait graph of 3 plots
fig.set_size_inches(fig_width,1*fig_height)
gs = gridspec.GridSpec(1, 1)

ax1 = plt.subplot(gs[0])



# Plot 1


n = 10000

mean_mu1 = 60
sd_sigma1 = 15
data1 = np.random.normal(mean_mu1, sd_sigma1, n)

mean_mu2 = 80
sd_sigma2 = 15
data2 = np.random.normal(mean_mu2, sd_sigma2, n)


w = 1
n1 = math.ceil((data1.max() - data1.min())/w)
n2 = math.ceil((data2.max() - data2.min())/w)


ax1.hist(data1, bins=n1, alpha=0.5, label="data1")
ax1.hist(data2, bins=n2, alpha=0.5, label="data2")
ax1.hist(data1+data2, bins=100, alpha=0.5, label="data3")



# Add graph labels and annotations
# Plot 1
set_graph_letter(ax1,'a)')
ax1.set_xlabel('X value',color=axes_font_color)
ax1.set_ylabel('Count',color=axes_font_color, rotation='horizontal')

x_min = 0
x_max = 300
# y_min = 0
# y_max = 0.8
ax1.spines['bottom'].set_bounds((x_min, x_max))
# ax1.spines['left'].set_bounds((y_min, y_max))

ax1.set_yticks((0,250,500))
ax1.set_xticks((mean_mu1,mean_mu2,mean_mu1+mean_mu2))

ax1.axvline(x=mean_mu1, linewidth=thin_line_width, color='black', linestyle= '--', zorder=0)
ax1.axvline(x=mean_mu2, linewidth=thin_line_width, color='black', linestyle= '--', zorder=0)
ax1.axvline(x=mean_mu1+mean_mu2, linewidth=thin_line_width, color='black', linestyle= '--', zorder=0)


ax1.legend(bbox_to_anchor=(0.9, 1.05))


plt.subplots_adjust(left=0.17,
bottom=0.348,
right=0.757,
top=0.774,
wspace=0.798, # note: value can be >1 here
hspace=0.31)

beautify_axes([ax1])

plt.savefig('{}.png'.format("output_plot"),dpi=600)


plt.show()
