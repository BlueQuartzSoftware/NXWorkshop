import simplnx as nx
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import nxutility

# #############################################################################
# Script Starts Here
# #############################################################################

# Tutorial Output Directory
output_dir = Path(__file__).parent / 'Output' / 'Tutorial_1_Output'
output_dir.mkdir(exist_ok=True, parents=True)

# Create the DataStructure instance
data_structure = nx.DataStructure()

result = nx.CreateDataGroup.execute(data_structure=data_structure, 
                                    data_object_path=nx.DataPath("Top Level Group"))
nxutility.check_filter_result(nx.CreateDataGroup(), result)

# Loop to create a bunch of DataGroups.
for i in range(1, 6):
    current_data_group_path = nx.DataPath(f"Top Level Group {i}")
    result = nx.CreateDataGroup.execute(data_structure=data_structure, 
                                        data_object_path=current_data_group_path)
    nxutility.check_filter_result(nx.CreateDataGroup(), result)

# Execute the CreateDataArray filter
result = nx.CreateDataArray().execute(data_structure=data_structure, 
                                    component_count=1, 
                                    initialization_value="0", 
                                    numeric_type=nx.NumericType.float32, 
                                    output_data_array=nx.DataPath("Top Level Group/2D Array"), 
                                    tuple_dimensions=[[4,5]])
nxutility.check_filter_result(nx.CreateDataArray(), result)
print(f'{data_structure.hierarchy_to_str()}')

# Try to get the array from the DataStructure
try:
    array_view = data_structure["Top Level Group/2D Array"].npview()
except AttributeError as attrerr:
    print(f'{attrerr}')
    quit(1) # This is pretty harsh! Maybe something more elegant to unwind from this error

# Fill the numpy data view with random numbers
rng = np.random.default_rng()
rng.standard_normal(out=array_view, dtype=np.float32)

print(f'{array_view}')

# Show the result
plt.imshow(array_view)
plt.title("Random Data")
plt.axis('off')  # to turn off axes
plt.show()

# Use the WriteDREAM3DFilter to write out the modified DataStructure to disk
result = nx.WriteDREAM3DFilter.execute(data_structure=data_structure,
                                    export_file_path=str(output_dir / 'tutorial_1.dream3d'),
                                    write_xdmf_file=False)
nxutility.check_filter_result( nx.WriteDREAM3DFilter(), result)

