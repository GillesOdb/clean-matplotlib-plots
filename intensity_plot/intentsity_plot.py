import numpy as np
import matplotlib.pyplot as plt

from matplotlib import gridspec
from matplotlib import colors
from matplotlib import cm


def set_graph_letter(ax,letter):
    ax.set_title(letter, 
                    fontsize = default_font_size, 
                    loc='left', 
                    y=graph_letter_y_offset, 
                    x=graph_letter_x_offset, 
                    fontweight='bold')


def beautify_intensity_plot_axes(array_of_axes):
    for ax in array_of_axes:
        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(True) 
        ax.spines['top'].set_color(axes_font_color)
        ax.spines['bottom'].set_color(axes_font_color)
        ax.spines['left'].set_color(axes_font_color)
        ax.tick_params(axis='y', colors=axes_font_color)
        ax.tick_params(axis='x', colors=axes_font_color)
        adjust_spines(ax, ['left', 'bottom','top'])
        ax.yaxis.set_label_coords(-0.1,1.1)
        ax.xaxis.set_ticks_position('top')


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


def map_value(value, min_in, max_in, min_out, max_out):
    if value < min_in:
        return min_out
    elif value > max_in:
        return max_out
    else:
        return (value - min_in)*(max_out-min_out)/(max_in-min_in) + min_out


def map_nested_list(list_in, min_in, max_in, min_out, max_out):
    nr_of_rows = len(list_in)
    nr_of_cols = len(list_in[0])

    print("nr_of_rows = {}".format(nr_of_rows))
    print("nr_of_cols = {}".format(nr_of_cols))

    mapped_array = []

    for row in range(nr_of_rows):
        mapped_subarray = []
        for col in range(nr_of_cols):
            original_value = list_in[row][col]
            mapped_value = map_value(original_value, min_in, max_in, min_out, max_out)
            mapped_subarray.append(mapped_value)
        mapped_array.append(mapped_subarray)
    for sublist in mapped_array:
        print(sublist)
    return mapped_array



def plot_heatmap(ax, list_in, min_in, max_in, ticks_scale_bar, colormap, linewidths=1,):
    mapped_list = map_nested_list(list_in,min_value,max_value,0,1)

    c = ax.pcolor(mapped_list, 
                    edgecolors='w', 
                    cmap=colormap,
                    linewidths=linewidths)

    # Format colarbar on right
    norm = colors.Normalize(vmin=min_value,vmax=max_value)
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array([])
    cb = plt.colorbar(sm, 
                        ax=ax, 
                        ticks=((0,15,30,45,60)), 
                        boundaries=np.arange(0,max_value+1,min_value+1))

    # beautify colorbar
    # set colorbar label plus label color
    # cb.set_label('colorbar label', color=axes_font_color)
    # set colorbar tick color
    cb.ax.yaxis.set_tick_params(color=axes_font_color)
    cb.outline.set_edgecolor(axes_font_color)



# Set default values
default_font_size = 8
axes_font_color = '#363636' # grey
color_second_axis = '#009E73' # green
mrkr_size = 5
line_width = 1
thin_line_width = 0.5
graph_letter_x_offset = -0.1
graph_letter_y_offset = -0.2

fig_width = 6.5 # inch
fig_height = 2 # inch

plt.rcParams.update({'font.size': 8,
                        'legend.frameon': False, 
                        'font.style':'normal',
                        'font.weight':'normal',
                        'font.family': 'serif',
                        'font.serif': 'Times new Roman',
                        'mathtext.fontset':'stix'})


# Examples of colormaps
# cm.jet
# cm.viridis
# cm.binary
# cm.inferno
# to reverse colormap add "_r" to the colormap name
# cm.binary_r


fig = plt.figure()
# portrait graph of 3 plots
fig.set_size_inches(fig_width,fig_height)
gs = gridspec.GridSpec(1, 3)

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])

# Generate random data

input_list =   [[10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,30,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,35,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,45,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,55,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,60,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,55,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,45,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35],]


# Plot 1

ticks = (0,15,30)
max_value = 60
min_value = 0

plot_heatmap(ax=ax1, 
                list_in=input_list, 
                min_in=0, 
                max_in=60, 
                colormap=cm.viridis,
                ticks_scale_bar=(0,15,30,45,60),
                linewidths=0.5)



# Plot 2
ticks = (0,15,30)
max_value = 60
min_value = 0

plot_heatmap(ax=ax2, 
                list_in=input_list, 
                min_in=0, 
                max_in=60, 
                colormap=cm.inferno,
                ticks_scale_bar=(0,15,30,45,60),
                linewidths=1)


# Plot 3
ticks = (0,15,30)
max_value = 30 # values will clip at 30
min_value = 0

plot_heatmap(ax=ax3, 
                list_in=input_list, 
                min_in=0, 
                max_in=60, 
                colormap=cm.binary_r,
                ticks_scale_bar=(0,15,30,45,60),
                linewidths=0)



# Add graph labels and annotations
# Plot 1
set_graph_letter(ax1, "a)")
ax1.set_title("Value (unit)", y=1.05)
ax1.axis('off') # 'off' just turns all axes off
ax1.set_ylim(ax1.get_ylim()[::-1]) # invert y axis


# Plot 2
set_graph_letter(ax2, "b)")
ax2.set_title("Temperature (°C)", y=1.05)

ax2.axis('off') # 'off' just turns all axes off
# ax1.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5])
# ax1.set_xticklabels(["","2","","4","","6","","8","","10","","12","","14","","16"])

# ax1.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5])
# ax1.set_yticklabels(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"])

ax2.set_ylim(ax2.get_ylim()[::-1]) # invert y axis



# Plot 3
set_graph_letter(ax3, "c)")
ax3.set_title("Value (unit)", y=1.05)

ax3.axis('off') # 'off' just turns all axes off
ax3.set_ylim(ax3.get_ylim()[::-1]) # invert y axis


plt.subplots_adjust(top=0.821,
bottom=0.157,
left=0.035,
right=0.982,
hspace=0.2,
wspace=0.272)

# plt.tight_layout()

beautify_intensity_plot_axes([ax1,ax2])

plt.savefig('{}.png'.format("output_plot"),dpi=600)

plt.show()