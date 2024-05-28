import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
from pathlib import Path
from . import nxutility

#
# Tutorial Output Directory
#
output_dir = Path('/tmp/Tutorial_2a_Output')   # Modify this path to point to the directory where the Tutorial 2a output will be stored!
output_dir.mkdir(exist_ok=True)

#
# Tutorial Start
#

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
nxutility.check_pipeline_result(result=result)

# Save the modified pipeline to the output location
output_pipeline_file_path = output_dir / 'lesson_2a_modified_pipeline.d3dpipeline'
pipeline.to_file("Modified Pipeline", str(output_pipeline_file_path))