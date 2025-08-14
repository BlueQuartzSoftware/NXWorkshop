import simplnx as nx
import NXWorkshopPlugin

# Currently this is required to have this plugin's filters appear when loading from a pipeline file
nx.load_python_plugin(NXWorkshopPlugin)

# Use python debugger to step through python code

# PyFilter is necessary to make python filters behave the same as native ones
pyfilter = nx.PyFilter(NXWorkshopPlugin.Exercise1())

data_structure = nx.DataStructure()

result = pyfilter.execute2(data_structure)
