''' 
This module contains some convenience functions that are useful
when writing DREAM3D-NX Python codes
'''

import os
import shutil
from pathlib import Path

import simplnx as nx


def modify_pipeline_filter(pipeline: nx.Pipeline, index: int, key: str, value):
  param_dict = pipeline[index].get_args()
  param_dict[key] = value
  pipeline[index].set_args(param_dict)


def check_filter_result(filter: nx.IFilter, result: nx.IFilter.ExecuteResult) -> None:
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
  
  print(f"{filter.name()} :: No errors running the filter")

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
    #print(f'Pipeline :: Errors: {result.errors}')
    for err in result.errors:
      print(f'Error: ({err.code}) {err.message}')
    raise RuntimeError(result)
  
  print(f"Pipeline :: No errors running the pipeline")
