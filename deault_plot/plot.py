import matplotlib.pyplot as plt  
import numpy as np

from natsort import natsorted
from matplotlib import gridspec

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
fig.set_size_inches(fig_width,3*fig_height)
gs = gridspec.GridSpec(3, 1)

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])


# Plot 1
data_1_x = [0,0.2,0.5,0.6,0.8,1.0,1.2]
data_1_y = [0.010,0.015,0.030,0.100,0.200,0.400, 0.800]

ax1.plot(data_1_x,
            data_1_y,
            '.-',
            color=color_palette[0],
            markersize=mrkr_size, 
            linewidth=thin_line_width)


# Plot 2
data_2_x = [0,10,20,30,40,50]
data_2_y = [1,5,8,-4,3,0]
data_2_y_b = [2,6,5,-2,5,0]

ax2_b = ax2.twinx()
            
ax2.plot(data_2_x,
            data_2_y,
            '.-',
            color=color_palette[0],
            markersize=mrkr_size, 
            linewidth=thin_line_width)


ax2_b.plot(data_2_x,
            data_2_y_b,
            '.-',
            color=color_second_axis,
            markersize=mrkr_size, 
            linewidth=thin_line_width)


# Plot 3 - errorbar plot
data_3_x = [10,20,30,40]
data_3_y = [[1,2,3,4,5],[2,5,6,7,8,31,7],[1,2,54,53,3,2,5,1,0],[1,2,5,66,7,4,2]]

custom_errorbar_plot(ax3, data_3_x, data_3_y, color_palette[2])




# Add graph labels and annotations
# Plot 1
set_graph_letter(ax1,'a)')
ax1.set_xlabel(r'Time (s$^{1/2}$)',color=axes_font_color)
ax1.set_ylabel(r'$\Delta$U (V)',color=axes_font_color, rotation='horizontal')

ax1.set_yticks((0,0.5))
ax1.set_xticks((0,0.7,1.1))
ax1.set_yticklabels((r'0.000', r'0.500'))

ax1.axvline(x=0.7, linewidth=thin_line_width, color='black', linestyle= '--')
ax1.axvline(x=1.1, linewidth=thin_line_width, color='black', linestyle= '--')


# Plot 2
set_graph_letter(ax2,'b)')
ax2.set_xlabel("Time (min)",color=axes_font_color)
ax2.set_ylabel('Change in \n slope (%)',color=axes_font_color, rotation='horizontal')

ax2.set_ylim(-10,10)
ax2.arrow(32, 8, 0, -3 , fc=axes_font_color, ec=axes_font_color,head_width=1, head_length=1.25,color=axes_font_color)
ax2.text(32, 9, 'Arrow \n here',fontweight='normal',horizontalalignment='center',verticalalignment='bottom',color=axes_font_color)

ax2.set_yticks((-10,0,10))
ax2_b.set_yticks((-10,0,10))
ax2_b.set_ylabel('Test 2nd\naxis',color=color_second_axis, rotation='horizontal')


# Plot 3
set_graph_letter(ax3,'c)')
ax3.set_xlabel("Group label",color=axes_font_color)
ax3.set_ylabel('Change in \n offset (%)',color=axes_font_color, rotation='horizontal')
# For text labels on x axis
ax3.set_xticks(data_3_x)
ax3.set_xticklabels(('Group 1', 'Group 2', 'Group 3', 'Group 4'))


plt.subplots_adjust(top=0.945,
bottom=0.124,
left=0.186,
right=0.88,
hspace=1.4, # note: value can be >1 here
wspace=0.31)

beautify_axes([ax1,ax2,ax3])
beautify_second_axes([ax2_b])

plt.savefig('{}.png'.format("output_plot"),dpi=600)


plt.show()
