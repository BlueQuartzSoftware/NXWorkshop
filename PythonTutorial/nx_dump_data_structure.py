"""
This demo file requries the pygraphviz package to be install
`conda install pygraphviz -y`
"""

import simplnx as nx
import nxutility

import numpy as np
import matplotlib.pyplot as plt
import pygraphviz as pgv
import os

def show_data_structure_heirarchy(data_structure: nx.DataStructure) -> None:
    """
    This method will create an image and then show that image in MatPlotLib
    """

    # This will generate the hierarchy as a GraphViz formatted string that you can
    # print or save to a file
    graphviz_content = data_structure.hierarchy_to_graphviz()

    # Create a graph from the DOT string using pygraphviz
    G = pgv.AGraph(string=graphviz_content)
    temp_file_path = '.graphviz_output.png'

    # Render the graph to a PNG file
    G.draw(temp_file_path, format='png', prog='dot')
  
    # Use Matplotlib to display the generated image
    img = plt.imread(temp_file_path)
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')  # Hide axes
    plt.show()

    # Check if the file exists to avoid an error if the file is not found
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
        print("File has been deleted successfully.")

def create_data_structure():

    #------------------------------------------------------------------------------
    # Create a DataStructure will something in it 
    #------------------------------------------------------------------------------
    data_structure = nx.DataStructure()

    result = nx.CreateDataGroupFilter.execute(data_structure=data_structure,
                                        data_object_path=nx.DataPath('Small IN100'))
    result = nx.CreateDataGroupFilter.execute(data_structure=data_structure,
                                        data_object_path=nx.DataPath('Small IN100/Scan Data'))
    result = nx.CreateDataGroupFilter.execute(data_structure=data_structure,
                                        data_object_path=nx.DataPath('Small IN100/Phase Data'))
    result = nx.CreateDataArrayFilter.execute(data_structure=data_structure, 
                                        component_count=3, 
                                        initialization_value="3.14159", 
                                        numeric_type=nx.NumericType.float32, 
                                        output_data_array=nx.DataPath('Small IN100/Scan Data/Eulers'), 
                                        tuple_dimensions=[[5,5]] )
    result = nx.CreateDataArrayFilter.execute(data_structure=data_structure, 
                                        component_count=1, 
                                        initialization_value="0", 
                                        numeric_type=nx.NumericType.int32, 
                                        output_data_array=nx.DataPath('Small IN100/Scan Data/Phases'), 
                                        tuple_dimensions=[[5,5]] )
    result = nx.CreateDataArrayFilter.execute(data_structure=data_structure, 
                                        component_count=1, 
                                        initialization_value="0", 
                                        numeric_type=nx.NumericType.uint32, 
                                        output_data_array=nx.DataPath('Small IN100/Phase Data/Crystal Structures'), 
                                        tuple_dimensions=[[5,5]] )
    # Call the function to render the DataStructure heirarchy in a window.
    show_data_structure_heirarchy(data_structure=data_structure)
