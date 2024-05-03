from typing import List
import simplnx as nx
import numpy as np


class Exercise1:

# -----------------------------------------------------------------------------
# These methods should not be edited
# -----------------------------------------------------------------------------
  def uuid(self) -> nx.Uuid:
    """This returns the UUID of the filter. Each filter has a unique UUID value
    :return: The Filter's Uuid value
    :rtype: string
    """
    return nx.Uuid('91a6ba07-4f1b-4d73-94f0-de422e00f105')

  def class_name(self) -> str:
    """The returns the name of the class that implements the filter
    :return: The name of the implementation class
    :rtype: string
    """
    return 'Exercise1'

  def name(self) -> str:
    """The returns the name of filter
    :return: The name of the filter
    :rtype: string
    """
    return 'Exercise1'

  def clone(self):
    """Clones the filter
    :return: A new instance of the filter
    :rtype:  Exercise1
    """
    return Exercise1()

# -----------------------------------------------------------------------------
# These methods CAN (and probably should) be updated. For instance, the 
# human_name() is what users of the filter will see in the DREAM3D-NX GUI. You
# might want to consider putting spaces between workd, using proper capitalization
# and putting "(Python)" at the end of the name (or beginning if you want the 
# filter list to group your filters togther)
# -----------------------------------------------------------------------------
  def human_name(self) -> str:
    """This returns the name of the filter as a user of DREAM3DNX would see it
    :return: The filter's human name
    :rtype: string
    """
    return 'Exercise1 (Python)'
 
  def default_tags(self) -> List[str]:
    """This returns the default tags for this filter
    :return: The default tags for the filter
    :rtype: list
    """
    return ['python', 'Exercise1']
  
  
  """
  This section should contain the 'keys' that store each parameter. The value of the key should be snake_case. The name
  of the value should be ALL_CAPITOL_KEY
  """
  INPUT_ARRAY_PATH_KEY = "input_array_path"
  OUTPUT_ARRAY_NAME_KEY = 'output_array_name'

  def parameters(self) -> nx.Parameters:
    """This function defines the parameters that are needed by the filter. Parameters collect the values from the user interface
    and pack them up into a dictionary for use in the preflight and execute methods.
    """
    params = nx.Parameters()

    params.insert(nx.Parameters.Separator("Required Data Objects"))

    # Use an Array Selection Parameter to get a Float32 array with 3 components ONLY.
    # https://www.dream3d.io/python_docs/Developer_API.html#ArraySelectionParameter
    params.insert(nx.ArraySelectionParameter(Exercise1.INPUT_ARRAY_PATH_KEY, 'Input Euler Array', 'Input Array with angular data', nx.DataPath(), {nx.DataType.float32}, [[3]]))

    params.insert(nx.Parameters.Separator("Created Data Objects"))

    # https://www.dream3d.io/python_docs/Developer_API.html#DataObjectNameParameter
    params.insert(nx.DataObjectNameParameter(Exercise1.OUTPUT_ARRAY_NAME_KEY, 'Created Array Name', 'OUtput Array storing the data', "Converted Data"))

    params.insert(nx.GeneratedFileListParameter)

    return params

  def preflight_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.PreflightResult:
    """This method preflights the filter and should ensure that all inputs are sanity checked as best as possible. Array
    sizes can be checked if the array sizes are actually known at preflight time. Some filters will not be able to report output
    array sizes during preflight (segmentation filters for example). If in doubt, set the tuple dimensions of an array to [1].
    :returns:
    :rtype: nx.IFilter.PreflightResult
    """

    # Extract the values from the user interface from the 'args' 
    input_array_path: nx.DataPath = args[Exercise1.INPUT_ARRAY_PATH_KEY]
    output_array_name: str = args[Exercise1.OUTPUT_ARRAY_NAME_KEY]
      
    # Create an OutputActions object to hold any DataStructure modifications that we are going to make
    output_actions = nx.OutputActions()
    
    # Create the Errors and Warnings Lists to commuicate back to the user if anything has gone wrong
    # errors = []
    # warnings = []
    # preflight_values = []

    # The goal is to create another array, at the same level as the selected array, and with the same number of tuples and components
    # Extract the Tuple Dimensions and the Component Dimensions
    input_data_array: nx.IDataArray = data_structure[input_array_path]
    input_tdims = input_data_array.tuple_shape
    input_cdims = input_data_array.component_shape

    # Generate a new nx.DataPath using the nx.DataPath API
    output_array_path = input_array_path.with_name(output_array_name)

    # Append a "CreateArrayAction" 
    output_actions.append_action(nx.CreateArrayAction(nx.DataType.float32, input_tdims, input_cdims, output_array_path))

    # Send back any messages that will appear in the "Output" widget in the UI. This is optional.
    # You can use this as a crude debugging aid if needed.
    message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f"Creating array at: '{output_array_path.to_string('/')}'"))

    # Return the output_actions so the changes are reflected in the User Interface.
    return nx.IFilter.PreflightResult(output_actions=output_actions, errors=None, warnings=None, preflight_values=None)
  
  def execute_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.ExecuteResult:
    """ This method actually executes the filter algorithm and reports results.
    :returns:
    :rtype: nx.IFilter.ExecuteResult
    """
    # Extract the values from the user interface from the 'args'
    # This is basically repeated from the preflight because the variables are scoped to the method()
    input_array_path: nx.DataPath = args[Exercise1.INPUT_ARRAY_PATH_KEY]
    output_array_name: str = args[Exercise1.OUTPUT_ARRAY_NAME_KEY]
    
    # Generate the proper output array nx.DataPath
    output_array_path = input_array_path.with_name(output_array_name)

    # The output array has been properly allocated at this point. Get a numpy
    # view of the input and output data arrays
    input_array_view = data_structure[input_array_path].npview()
    output_array_view = data_structure[output_array_path].npview()

    # Now you can go off and use numpy or anything else that can use a numpy view to modify the data
    # or use the data in another calculation. Any operation that works on the numpy view in-place
    # has an immediate effect within the DataStructure
    np.degrees(input_array_view, out=output_array_view)

    # -----------------------------------------------------------------------------
    # If you want to send back progress on your filter, you can use the message_handler
    # -----------------------------------------------------------------------------
    message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Conversion complete'))

    # -----------------------------------------------------------------------------
    # If you have a long running process, check the should_cancel to see if the user cancelled the filter
    # -----------------------------------------------------------------------------
    if not should_cancel:
      return nx.Result()






