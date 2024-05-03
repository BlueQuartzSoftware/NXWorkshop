import simplnx as nx
import numpy as np
import matplotlib.pyplot as plt
import nxutility

# Create the DataStructure instance
data_structure = nx.DataStructure()

result = nx.CreateDataGroupFilter.execute(data_structure=data_structure, 
                                    data_object_path=nx.DataPath("Top Level Group"))

# Loop to create a bunch of DataGroups.
for i in range(1, 6):
    current_data_group_path = nx.DataPath(f"Top Level Group {i}")
    result = nx.CreateDataGroupFilter.execute(data_structure=data_structure, 
                                        data_object_path=current_data_group_path)

# Execute the filter
result = nx.CreateDataArrayFilter().execute(data_structure=data_structure, 
                                    component_count=1, 
                                    initialization_value_str="0", 
                                    numeric_type_index=nx.NumericType.float32, 
                                    output_array_path=nx.DataPath("Top Level Group/2D Array"), 
                                    tuple_dimensions=[[4,5]])
nxutility.check_filter_result( nx.CreateDataArrayFilter(), result)
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

