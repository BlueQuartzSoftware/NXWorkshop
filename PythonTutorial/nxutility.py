''' 
This module contains some convenience functions that are useful
when writing DREAM3D-NX Python codes
'''

import simplnx as nx


def modify_pipeline_filter(nxfilter: nx.PipelineFilter, key: str, value):
  param_dict = nxfilter.get_args()
  param_dict[key] = value
  nxfilter.set_args(param_dict)


def check_filter_result(filter: nx.IFilter, result: nx.IFilter.ExecuteResult) -> None:
  """
  This function will check the `result` for any errors. If errors do exist then a 
  `RuntimeError` will be thrown. Your own code to modify this to return something
  else that doesn't just stop your script in its tracks.
  """
  for w in result.warnings:
    print(f'Warning: ({w.code}) {w.message}')

  if result.errors:
    for err in result.errors:
      print(f'Error: ({err.code}) {err.message}')
    raise RuntimeError(result)

  print(f"{filter.name()} :: No errors running the filter")

def check_pipeline_result(result: nx.Result) -> None:
  """
  This function will check the `result` for any errors. If errors do exist then a 
  `RuntimeError` will be thrown. Your own code to modify this to return something
  else that doesn't just stop your script in its tracks.
  """
  for w in result.warnings:
    print(f'Warning: ({w.code}) {w.message}')

  if result.errors:
    for err in result.errors:
      print(f'Error: ({err.code}) {err.message}')
    raise RuntimeError(result)

  print(f"Pipeline :: No errors running the pipeline")
