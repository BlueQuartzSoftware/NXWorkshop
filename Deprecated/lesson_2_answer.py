
import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
import nxutility
import numpy as np


def generate_ipf_maps():
    """
    This shows how to loop on a pipeline making changes each loop.
    
    The Pipeline is as follows
    [0]: Read EDAX EBSD Data (.ang)
    [1]: Rotate Euler Reference Frame
    [2]: Rotate Sample Reference Frame
    [3]: Multi-Threshold Objects
    [4]: Generate IPF Colors
    [5]: Write Image (ITK)
    [6]: Write DREAM3D NX File

    Filter [0] is the ReadAngDataFilter which we will need to adjust the input file
        https://www.dream3d.io/python_docs/OrientationAnalysis.html#OrientationAnalysis.ReadAngDataFilter
    Filter [5] is the image writing filter where we need to adjust the output file
        https://www.dream3d.io/python_docs/ITKImageProcessing.html#write-image-itk
    Filter [6] is the write dream3d file filter where we need to adjust the output file
        https://www.dream3d.io/python_docs/simplnx.html#write-dream3d-nx-file
    """

    for i in range(1, 6):
        # Create the DataStructure instance
        data_structure = nx.DataStructure()
        # Read the pipeline file
        pipeline = nx.Pipeline().from_file( 'Pipelines/lesson_2_ebsd.d3dpipeline')
        # Get the parameter dictionary for the first filter and
        # modify the input file. Then set the modified dictionary back into
        # the pipeine at the same location
        nxutility.modify_pipeline_filter(pipeline, 0, "input_file", f"Data/Small_IN100/Slice_{i}.ang")
        # read_ang_parameters = pipeline[0].get_args()
        # read_ang_parameters["input_file"] = f"Data/Small_IN100/Slice_{i}.ang"
        # pipeline[0].set_args(read_ang_parameters)

        # Do the same modification here for the 5th filter in the pipeline
        nxutility.modify_pipeline_filter(pipeline, 5, "file_name", f"Output/Edax_IPF_Colors/Small_IN100_Slice_{i}.png")
        # write_image_parameters = pipeline[5].get_args()
        # write_image_parameters["file_name"] = f"Output/Edax_IPF_Colors/Small_IN100_Slice_{i}.png"
        # pipeline[5].set_args(write_image_parameters)

        # Do the same modification here for the 6th filter in the pipeline
        nxutility.modify_pipeline_filter(pipeline, 6, "export_file_path", f"Output/Edax_IPF_Colors/Small_IN100_Slice_{i}.dream3d")
        # write_image_parameters = pipeline[6].get_args()
        # write_image_parameters["export_file_path"] = f"Output/Edax_IPF_Colors/Small_IN100_Slice_{i}.dream3d"
        # pipeline[6].set_args(write_image_parameters)

        # Execute the modified pipeline
        result = pipeline.execute(data_structure)
        nxutility.check_pipeline_result(result=result)

        pipeline.to_file(f"Small_IN100_Slice_{i}", f"Output/Edax_IPF_Colors/Small_IN100_Slice_{i}.d3dpipeline")


def print_pipeline_filters():
    """
    This function will print out all the filters in a pipeline with an index
    """
    # Read the pipeline file
    pipeline = nx.Pipeline().from_file( 'Pipelines/lesson_2_ebsd.d3dpipeline')
    for index, filter in enumerate(pipeline):
        print(f"[{index}]: {filter.get_filter().human_name()}")

def insert_pipeline_filter():
    """
    This shows how to create a filter and insert it into the pipeline and
    then execute that pipeline and save the pipeline
    """
    # Create the DataStructure instance
    data_structure = nx.DataStructure()
    # Read the pipeline file
    pipeline = nx.Pipeline().from_file( 'Pipelines/lesson_2.d3dpipeline')

    # Append a new filter onto the end of the pipeline
    create_geom_args : dict = {
            "array_handling": 0,
            "cell_attribute_matrix_name": "Cell Data",
            "dimensions": [ 100, 100, 100 ],
            "geometry_name": nx.DataPath("Output Geometry"),
            "geometry_type": 0,
            "length_unit_type": 7,
            "origin": [ 0.0, 0.0, 0.0 ],
            "spacing": [ 1.0, 1.0, 1.0 ],
            "warnings_as_errors": False,
            "x_bounds": nx.DataPath(""),
            "y_bounds": nx.DataPath(""),
            "z_bounds": nx.DataPath(""),
            "tetrahedral_list_name": nx.DataPath(""),
            "triangle_list_name": nx.DataPath(""),
            "vertex_attribute_matrix_name": "Vertex Data",
            "vertex_list_name": nx.DataPath(""),
            "quadrilateral_list_name": nx.DataPath(""),
            "hexahedral_list_name": nx.DataPath(""),
            "edge_attribute_matrix_name": "Edge Data",
            "edge_list_name": nx.DataPath(""),
            "face_attribute_matrix_name": "Face Data",
    }

    # insert the new filter just before the "Write DREAM3D Data File"
    pipeline.insert(2, nx.CreateGeometryFilter(), create_geom_args)
    # Execute the modified pipeline
    result = pipeline.execute(data_structure)
    nxutility.check_pipeline_result(result=result)
    # Save the modified pipeline to a file.
    pipeline.to_file( "Modified Pipeline", "Output/lesson_2a_modified_pipeline.d3dpipeline")


def modify_pipeline_filter():
    # Create the DataStructure instance
    data_structure = nx.DataStructure()
    # Read the pipeline file
    pipeline = nx.Pipeline().from_file( 'Pipelines/lesson_2.d3dpipeline')

    # Do the same modification here for the 5th filter in the pipeline
    create_data_array_params = pipeline[1].get_args()
    create_data_array_params["numeric_type"] = nx.NumericType.int8
    pipeline[1].set_args(create_data_array_params)

    # Execute the modified pipeline
    result = pipeline.execute(data_structure)
    nxutility.check_pipeline_result(result=result)
    # Save the modified pipeline to a file.
    pipeline.to_file( "Modified Pipeline", "Output/lesson_2b_modified_pipeline.d3dpipeline")


# insert_pipeline_filter()
# modify_pipeline_filter()
print_pipeline_filters()
generate_ipf_maps()
