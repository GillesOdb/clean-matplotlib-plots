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

    print(x_data)
    print(y_data)

    x_len = len(x_data)
    y_len = len(y_data)

    print(x_len)
    print(y_len)

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

# Plot 1 - errorbar plot
x_data = [10,20,30,40]
y_data = [[1,2,3,4,5],[2,5,6,7,8,31,7],[1,2,54,53,3,2,5,1,0],[1,2,5,66,7,4,2]]

custom_errorbar_plot(ax1, [x_data[0]], [y_data[0]], color_palette[0])
custom_errorbar_plot(ax1, [x_data[1]], [y_data[1]], color_palette[1])
custom_errorbar_plot(ax1, [x_data[2]], [y_data[2]], color_palette[2])
custom_errorbar_plot(ax1, [x_data[3]], [y_data[3]], color_palette[3])




# Add graph labels and annotations

# Plot 1
ax1.set_xlabel("Group label",color=axes_font_color)
ax1.set_ylabel('Change in \n offset (%)',color=axes_font_color, rotation='horizontal')
# For text labels on x axis
ax1.set_xticks(x_data)
ax1.set_xticklabels(('Group 1', 'Group 2', 'Group 3', 'Group 4'))


plt.subplots_adjust(top=0.777,
bottom=0.368,
left=0.18,
right=0.938,
hspace=1.0,
wspace=0.31)

beautify_axes([ax1])


plt.savefig('{}.png'.format("output_plot"),dpi=600)


plt.show()
