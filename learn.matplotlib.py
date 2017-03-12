#learn matplotlib
 

# Key events no pude lograr :(

import numpy as np
import matplotlib.pyplot as plt

def on_press(event):
   if event.inaxes is None: return
   for line in event.inaxes.lines:
       if event.key=='t':
           visible = line.get_visible()
           line.set_visible(not visible)
   event.inaxes.figure.canvas.draw()

fig, ax = plt.subplots(1)

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(2, 20))

plt.show()

# import matplotlib.pyplot as plt

# # With Backend and Artist
# # Import the FigureCanvas from the backend of your choice
# #  and attach the Figure artist to it.
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# fig = Figure()
# canvas = FigureCanvas(fig)

# # Import the numpy library to generate the random numbers.
# import numpy as np
# x = np.random.randn(10000)

# # Now use a figure method to create an Axes artist; the Axes artist is
# #  added automatically to the figure container fig.axes.
# # Here "111" is from the MATLAB convention: create a grid with 1 row and 1
# #  column, and use the first cell in that grid for the location of the new
# #  Axes.
# ax = fig.add_subplot(111)

# # Call the Axes method hist to generate the histogram; hist creates a
# #  sequence of Rectangle artists for each histogram bar and adds them
# #  to the Axes container.  Here "100" means create 100 bins.
# ax.hist(x, 100)

# # Decorate the figure with a title and save it.
# ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
# fig.savefig('matplotlib_histogram1.png')


# # all with scripting layer
# # MUST be matplotlib.pyplot with .pyplot for the scripting
# x = np.random.randn(10000)
# plt.hist(x, 100)
# plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
# plt.savefig('matplotlib_histogram2.png')
# plt.show()