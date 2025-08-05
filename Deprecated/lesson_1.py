"""
This is the bare minimum python code. This probably should _not_ be
used in a production environment due to no error checking being performed.
"""
import simplnx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create the DataStructure


# Execute the CreateDataArrayFilter filter


# First get the array from the DataStructure
npdata = data_structure[nx.DataPath("2D Array")].npview()

#
rng = np.random.default_rng()
rng.standard_normal(out=npdata, dtype=np.float32)

plt.imshow(npdata)
plt.title("Random Data")
plt.axis('off')  # to turn off axes
plt.show()
