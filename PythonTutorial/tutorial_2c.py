import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
from pathlib import Path
import nxutility

#
# Tutorial Start
#

#
# Tutorial Output Directory
#
output_dir = Path(__file__).parent / 'Output' / 'Tutorial_2c_Output'
output_dir.mkdir(exist_ok=True, parents=True)

# Loop over the EBSD pipeline
edax_ipf_colors_output_dir = output_dir / 'Edax_IPF_Colors'
edax_ipf_colors_output_dir.mkdir(exist_ok=True, parents=True)
for i in range(1, 6):
    # Create the data structure
    data_structure = nx.DataStructure()

    # Read the pipeline file
    pipeline_file_path = Path(__file__).parent / 'Pipelines' / 'lesson_2_ebsd.d3dpipeline'
    pipeline = nx.Pipeline().from_file(str(pipeline_file_path))

    # Modify file paths for the 1st, 6th, and 7th filters
    nxutility.modify_pipeline_filter(pipeline, 0, "input_file", str(Path(__file__).parent / 'Data' / 'Small_IN100' / f'Slice_{i}.ang'))
    nxutility.modify_pipeline_filter(pipeline, 5, "file_name", str(edax_ipf_colors_output_dir / f'Small_IN100_Slice_{i}.png'))
    nxutility.modify_pipeline_filter(pipeline, 6, "export_file_path", str(edax_ipf_colors_output_dir.parent / f'Small_IN100_Slice_{i}.dream3d'))

    # Execute the modified pipeline
    result = pipeline.execute(data_structure)
    nxutility.check_pipeline_result(result=result)

    # Output the modified pipeline
    output_pipeline_file_path = edax_ipf_colors_output_dir / f'Small_IN100_Slice_{i}.d3dpipeline'
    pipeline.to_file(f"Small_IN100_Slice_{i}", str(output_pipeline_file_path))
