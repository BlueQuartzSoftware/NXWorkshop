
import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
import nxutility

import numpy as np


"""
The filters documentation pages lists the "Representation Type" that will be needed for the filter. Look in the "Data Layout" table.

https://www.dream3d.io/nx_reference_manual/html/OrientationAnalysis/ConvertOrientations.html

The Euler Angles are located at: "DataContainer/Cell Data/EulerAngles"

You can use: print(f'{data_structure.hierarchy_to_str()}') to dump the data structure

"""

# Create the DataStructure Object
data_structure = nx.DataStructure()

# Create a Dream3dImportParameter parameter and then execute the ReadDREAM3DFilter filter.
# https://www.dream3d.io/python_docs/simplnx.html#simplnx.ReadDREAM3DFilter


# Dump the current DataStructure heirarchy
print(f'{data_structure.hierarchy_to_str()}')


# Generate Quaternions from the Euler Angles using the "ConvertOrientations" filter
# https://www.dream3d.io/nx_reference_manual/html/OrientationAnalysis/ConvertOrientations.html
# input_type = 0
# output_type = 2


# Use the WriteDREAM3DFilter to write out the modified DataStructure to disk
# https://www.dream3d.io/python_docs/simplnx.html#write-dream3d-nx-file
# export_file_path="Output/lesson_3.dream3d",
