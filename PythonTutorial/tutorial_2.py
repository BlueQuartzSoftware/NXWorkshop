import simplnx as nx
import itkimageprocessing as nxitk
import orientationanalysis as nxor

import numpy as np


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
    else:
        print(f"{filter.name()} :: No errors running the filter")