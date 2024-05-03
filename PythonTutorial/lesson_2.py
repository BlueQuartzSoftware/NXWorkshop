import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
import nxutility

import numpy as np

"""
The Pipeline is as follows
[0]: Read EDAX EBSD Data (.ang)
[1]: Rotate Euler Reference Frame
[2]: Rotate Sample Reference Frame
[3]: Multi-Threshold Objects
[4]: Generate IPF Colors
[5]: Write Image (ITK)
[6]: Write DREAM3D NX File

The pipeline file is located at 'Pipelines/lesson_2_ebsd.d3dpipeline'

You will need to setup a loop that does the following:
    - Creates a DataStructure object
    - Read the pipeline file
    - modify the [0] index filter parameter
    - modify the [5] index filter parameter
    - execute the pipeline

    [0]: Read EDAX EBSD Data (.ang) file
        https://www.dream3d.io/python_docs/OrientationAnalysis.html#readangdatafilter
        Modify the 'input_file' dictionary key

    [5]: Write Image (ITK)
        https://www.dream3d.io/python_docs/ITKImageProcessing.html#ITKImageProcessing.ITKImageWriter
        Modify the 'file_name' dictionary key

    [6] [6]: Write DREAM3D NX File
        https://www.dream3d.io/python_docs/simplnx.html#write-dream3d-nx-file    
        Mofify the 'export_file_path' dictionary key
    

https://www.dream3d.io/python_docs/DataObjects.html#PipelineFilter has the API descriptions    
"""

for i in range(1, 6):
    print(f'Starting Iteration {i}')
    # Read the pipeline
    pipeline = nx.Pipeline.from_file("Pipelines/lesson_2_ebsd.d3dpipeline")

    # get the parameter dictionary
    param_dict = pipeline[0].get_args()

    # modify the parameter dictionary
    param_dict["input_file"] = f"Data/Small_IN100/Slice_{i}.ang"

    # set the parameters back into the pipeline at the proper spot
    pipeline[0].set_args(param_dict)


    # get the parameter dictionary
    param_dict = pipeline[5].get_args()

    # modify the parameter dictionary
    param_dict["file_name"] = f"Output/Small_IN100/Slice_{i}.png"

    # set the parameters back into the pipeline at the proper spot
    pipeline[5].set_args(param_dict)



    # create a nx.DataStructure instance
    data_structure = nx.DataStructure()

    # Execute the pipeline
    result = pipeline.execute(data_structure)

