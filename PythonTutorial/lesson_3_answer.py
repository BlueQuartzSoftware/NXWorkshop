
import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
import nxutility
import nx_dump_data_structure

import numpy as np


"""


https://www.dream3d.io/python_docs/simplnx.html#simplnx.ReadDREAM3DFilter

"""

# Create the DataStructure Object
data_structure = nx.DataStructure()

# Create a Dream3dImportParameter parameter and then execute the ReadDREAM3DFilter filter.
import_param = nx.Dream3dImportParameter.ImportData()
import_param.file_path = "Output/Edax_IPF_Colors/Small_IN100_Slice_1.dream3d"
import_param.data_paths = None  # Use 'None' to import the entire file.

result = nx.ReadDREAM3DFilter.execute(data_structure,
                              import_file_data=import_param)
nxutility.check_filter_result( nx.ReadDREAM3DFilter(), result)

# Dump the current DataStructure heirarchy
print(f'{data_structure.hierarchy_to_str()}')

nx_dump_data_structure.show_data_structure_heirarchy(data_structure=data_structure)

# Generate Quaternions from the Euler Angles
# input_type = 0
# output_type = 2
result = nxor.ConvertOrientationsFilter.execute(data_structure=data_structure, 
                                          input_orientation_array_path=nx.DataPath("DataContainer/Cell Data/EulerAngles"), 
                                          input_type=0, 
                                          output_orientation_array_name="Quats", 
                                          output_type=2)
nxutility.check_filter_result( nx.WriteDREAM3DFilter(), result)

# Use the WriteDREAM3DFilter to write out the modified DataStructure to disk
result = nx.WriteDREAM3DFilter.execute(data_structure=data_structure,
                                       export_file_path="Output/lesson_3.dream3d",
                                       write_xdmf_file=False)
nxutility.check_filter_result( nx.WriteDREAM3DFilter(), result)
