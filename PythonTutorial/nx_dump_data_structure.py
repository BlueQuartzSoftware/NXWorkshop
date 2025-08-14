"""
This demo file requries the pygraphviz package to be install
`conda install pygraphviz -y`
"""

import simplnx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import io

def show_data_structure_heirarchy(data_structure: nx.DataStructure) -> None:
    """
    This method will create an image and then show that image in MatPlotLib
    """

    # This will generate the hierarchy as a GraphViz formatted string that you can
    # print or save to a file
    graphviz_content = data_structure.hierarchy_to_graphviz()

    # Create a graph from the DOT string using pygraphviz
    G = pgv.AGraph(string=graphviz_content)

    # Render the graph to a PNG file
    image_data = G.draw(None, format='png', prog='dot')

    # Use Matplotlib to display the generated image
    img = plt.imread(io.BytesIO(image_data))
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')  # Hide axes
    plt.show()


def create_data_structure() -> nx.DataStructure:
    #------------------------------------------------------------------------------
    # Create a DataStructure will something in it 
    #------------------------------------------------------------------------------
    data_structure = nx.DataStructure()

    assert nx.CreateDataGroupFilter.execute(
        data_structure=data_structure,
        data_object_path=nx.DataPath('Small IN100'),
    )
    assert nx.CreateDataGroupFilter.execute(
        data_structure=data_structure,
        data_object_path=nx.DataPath('Small IN100/Scan Data'),
    )
    assert nx.CreateDataGroupFilter.execute(
        data_structure=data_structure,
        data_object_path=nx.DataPath('Small IN100/Phase Data'),
    )
    assert nx.CreateDataArrayFilter.execute(
        data_structure=data_structure,
        component_count=3,
        initialization_value_str="3.14159",
        numeric_type_index=nx.NumericType.float32,
        output_array_path=nx.DataPath('Small IN100/Scan Data/Eulers'),
        tuple_dimensions=[[5, 5]],
    )
    assert nx.CreateDataArrayFilter.execute(
        data_structure=data_structure,
        component_count=1,
        initialization_value_str="0",
        numeric_type_index=nx.NumericType.int32,
        output_array_path=nx.DataPath('Small IN100/Scan Data/Phases'),
        tuple_dimensions=[[5, 5]],
    )
    assert nx.CreateDataArrayFilter.execute(
        data_structure=data_structure,
        component_count=1,
        initialization_value_str="0",
        numeric_type_index=nx.NumericType.uint32,
        output_array_path=nx.DataPath('Small IN100/Phase Data/Crystal Structures'),
        tuple_dimensions=[[5, 5]],
    )
    return data_structure

if __name__ == '__main__':
    data_structure = create_data_structure()
    # Call the function to render the DataStructure heirarchy in a window.
    show_data_structure_heirarchy(data_structure)
