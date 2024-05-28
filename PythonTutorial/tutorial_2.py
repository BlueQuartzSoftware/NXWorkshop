import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
from pathlib import Path

#
# Helper Methods
#
def check_pipeline_result(result: nx.Result) -> None:
    """
    This function will check the `result` for any errors. If errors do exist then a 
    `RuntimeError` will be thrown. Your own code to modify this to return something
    else that doesn't just stop your script in its tracks.
    """
    if len(result.warnings) != 0:
        for w in result.warnings:
            print(f'Warning: ({w.code}) {w.message}')
    
    has_errors = len(result.errors) != 0 
    if has_errors:
        for err in result.errors:
            print(f'Error: ({err.code}) {err.message}')
        raise RuntimeError(result)
    
    print(f"Pipeline :: No errors running the pipeline")

def modify_pipeline_filter(pipeline: nx.Pipeline, index: int, key: str, value):
    # The get_args method retrieves the current arguments, and set_args applies the modifications.
    param_dict = pipeline[index].get_args()
    param_dict[key] = value
    pipeline[index].set_args(param_dict)

#
# Tutorial Start
#

output_dir = Path('/tmp/Tutorial_2_Output')   # Modify this path to point to the directory where the Tutorial 2 output will be stored
output_dir.mkdir(exist_ok=True)

# Create the data structure
data_structure = nx.DataStructure()

# Get the pipeline from the pipeline file
pipeline_file_path = Path(__file__).parent / 'Pipelines' / 'lesson_2.d3dpipeline'
pipeline = nx.Pipeline().from_file(str(pipeline_file_path))

# Print the pipeline
for index, filter in enumerate(pipeline):
  print(f"[{index}]: {filter.get_filter().human_name()}")

# Define the CreateDataGroup filter arguments
create_data_group_args = {
        "data_object_path": nx.DataPath("Small IN100/EBSD Data")
    }

# Insert CreateDataGroup filter into the pipeline
pipeline.insert(2, nx.CreateDataGroup(), create_data_group_args)

# Print the pipeline again
for index, filter in enumerate(pipeline):
  print(f"[{index}]: {filter.get_filter().human_name()}")

# Execute the pipeline
result = pipeline.execute(data_structure)

# Check the execution result
check_pipeline_result(result=result)

# Save the modified pipeline to the output location
output_pipeline_file_path = output_dir / 'lesson_2a_modified_pipeline.d3dpipeline'
pipeline.to_file("Modified Pipeline", str(output_pipeline_file_path))

# Modify the numeric type of filter 2 in the pipeline
modify_pipeline_filter(pipeline, 1, "numeric_type", nx.NumericType.int8)

# Save the modified pipeline to the output location
output_pipeline_file_path = output_dir / 'lesson_2b_modified_pipeline.d3dpipeline'
pipeline.to_file("Modified Pipeline", str(output_pipeline_file_path))

# Loop over the EBSD pipeline
edax_ipf_colors_output_dir = output_dir / 'Edax_IPF_Colors'
edax_ipf_colors_output_dir.mkdir(exist_ok=True)
for i in range(1, 6):
    # Create the data structure
    data_structure = nx.DataStructure()

    # Read the pipeline file
    pipeline_file_path = Path(__file__).parent / 'Pipelines' / 'lesson_2_ebsd.d3dpipeline'
    pipeline = nx.Pipeline().from_file(str(pipeline_file_path))

    # Modify file paths for the 1st, 6th, and 7th filters
    modify_pipeline_filter(pipeline, 0, "input_file", str(Path(__file__).parent / 'Data' / 'Small_IN100' / f'Slice_{i}.ang'))
    modify_pipeline_filter(pipeline, 5, "file_name", str(edax_ipf_colors_output_dir / f'Small_IN100_Slice_{i}.png'))
    modify_pipeline_filter(pipeline, 6, "export_file_path", str(edax_ipf_colors_output_dir / f'Small_IN100_Slice_{i}.dream3d'))

    # Execute the modified pipeline
    result = pipeline.execute(data_structure)
    check_pipeline_result(result=result)

    # Output the modified pipeline
    output_pipeline_file_path = edax_ipf_colors_output_dir / f'Small_IN100_Slice_{i}.d3dpipeline'
    pipeline.to_file(f"Small_IN100_Slice_{i}", str(output_pipeline_file_path))
