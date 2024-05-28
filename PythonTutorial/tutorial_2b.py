import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor
from pathlib import Path
from . import nxutility

#
# Tutorial Output Directory
#
output_dir = Path('/tmp/Tutorial_2b_Output')   # Modify this path to point to the directory where the Tutorial 2b output will be stored!
output_dir.mkdir(exist_ok=True)

#
# Tutorial Start
#

# Create the data structure
data_structure = nx.DataStructure()

# Get the pipeline from the pipeline file
pipeline_file_path = Path(__file__).parent / 'Pipelines' / 'lesson_2.d3dpipeline'
pipeline = nx.Pipeline().from_file(str(pipeline_file_path))

# Modify the numeric type of filter 2 in the pipeline
nxutility.modify_pipeline_filter(pipeline, 1, "numeric_type", nx.NumericType.int8)

# Execute the pipeline
result = pipeline.execute(data_structure)

# Check the execution result
nxutility.check_pipeline_result(result=result)

# Save the modified pipeline to the output location
output_pipeline_file_path = output_dir / 'lesson_2b_modified_pipeline.d3dpipeline'
pipeline.to_file("Modified Pipeline", str(output_pipeline_file_path))

