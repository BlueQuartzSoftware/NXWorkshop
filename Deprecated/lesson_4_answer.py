
import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
import nxutility
import nx_dump_data_structure

import numpy as np

"""

"""


# Create the DataStructure Object
data_structure = nx.DataStructure()

# Read the STL file
# Don't believe the parameter key hinting at "path". Check the documentation
result = nx.ReadStlFileFilter.execute(data_structure=data_structure, 
                                face_attribute_matrix="Face Data", 
                                face_normals_data_path="Normals", 
                                scale_factor=1.0, 
                                scale_output=False, 
                                stl_file_path="Data/star_model.stl", 
                                triangle_geometry_name=nx.DataPath("StarModel"), 
                                vertex_attribute_matrix="Vertex Data")
nxutility.check_filter_result( nx.ReadDREAM3DFilter(), result)

# To get a numpy_view of the vertices there are a few options
# You can get a reference to the Triangle Geometry and then ask for the vertices and then get the numpy view
geometry: nx.TriangleGeom = data_structure[nx.DataPath("StarModel")]
vertices_view = geometry.vertices.npview()
faces_view = geometry.faces.npview()

# OR you can ask directly for the vertices from the DataStructure knowing that DREAM3D always names
# the vertices 'SharedVertexList'
vertices_view = data_structure["StarModel/SharedVertexList"].npview()

# Now that we have the vertices, use numpy to translate the the entire model in the +XYZ
# diagonal 
vertices_view += (100.0)

# Add 100 to the X Coordinate, effectively translating it in the +X direction
vertices_view[:, 0] += 100.0

# Use the WriteDREAM3DFilter to write out the modified DataStructure to disk
result = nx.WriteDREAM3DFilter.execute(data_structure=data_structure,
                                       export_file_path="Output/lesson_4.dream3d",
                                       write_xdmf_file=False)
nxutility.check_filter_result( nx.WriteDREAM3DFilter(), result)
