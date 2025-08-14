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
    return nx.Uuid('f141853b-c1f5-4e6a-bad4-6a46b1d0192b')

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

  def default_tags(self) -> list[str]:
    """This returns the default tags for this filter
    :return: The default tags for the filter
    :rtype: list
    """
    return ['python', 'Exercise1']


  """
  This section should contain the 'keys' that store each parameter. The value of the key should be snake_case. The name
  of the value should be ALL_CAPITAL_KEY
  """
  # INPUT_ARRAY_PATH_KEY = 'input_array_path'
  # OUTPUT_ARRAY_PATH_KEY = 'output_array_path'
  # DELTA_VALUE_KEY = 'delta_value'

  def parameters(self) -> nx.Parameters:
    """This function defines the parameters that are needed by the filter. Parameters collect the values from the user interface
    and pack them up into a dictionary for use in the preflight and execute methods.
    """
    params = nx.Parameters()

    # params.insert(nx.Parameters.Separator('Input Parameters'))
    # params.insert(nx.Int32Parameter(Exercise1.DELTA_VALUE_KEY, 'Incorrect value', 'The value to add', 0))

    # params.insert(
    #   nx.ArraySelectionParameter(
    #     Exercise1.INPUT_ARRAY_PATH_KEY,
    #     'Array Selection',
    #     'Example array selection help text',
    #     nx.DataPath(),
    #     {nx.DataType.float32},
    #     [[1]],
    #   )
    # )

    # params.insert(nx.Parameters.Separator("Output Parameters"))
    # params.insert(nx.ArrayCreationParameter(Exercise1.OUTPUT_ARRAY_PATH_KEY, 'Created Array', 'Array storing the data', nx.DataPath()))

    return params

  def parameters_version(self) -> int:
    """This method should initially return 1.
    Then whenever one or more parameters is added or removed from the filter
    the return value should be incremented.
    """
    return 1

  def preflight_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.PreflightResult:
    """This method preflights the filter and should ensure that all inputs are sanity checked as best as possible. Array
    sizes can be checked if the array sizes are actually known at preflight time. Some filters will not be able to report output
    array sizes during preflight (segmentation filters for example). If in doubt, set the tuple dimensions of an array to [1].
    :returns:
    :rtype: nx.IFilter.PreflightResult
    """

    # output_array_path: nx.DataPath = args[Exercise1.OUTPUT_ARRAY_PATH_KEY]
    # input_array_path: nx.DataPath = args[Exercise1.INPUT_ARRAY_PATH_KEY]
    # delta_value: int = args[Exercise1.DELTA_VALUE_KEY]

    # message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Delta Value: {delta_value}'))

    # input_array: nx.IDataArray = data_structure[input_array_path]

    output_actions = nx.OutputActions()

    # output_actions.append_action(nx.CreateArrayAction(input_array.data_type, input_array.tdims, input_array.cdims, output_array_path))

    return nx.IFilter.PreflightResult(output_actions=output_actions, errors=None, warnings=None, preflight_values=None)

  def execute_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.ExecuteResult:
    """This method actually executes the filter algorithm and reports results.
    :returns:
    :rtype: nx.IFilter.ExecuteResult
    """
    # input_array_path: nx.DataPath = args[Exercise1.INPUT_ARRAY_PATH_KEY]
    # output_array_path: nx.DataPath = args[Exercise1.OUTPUT_ARRAY_PATH_KEY]
    # delta_value: int = args[Exercise1.DELTA_VALUE_KEY]

    # input_array_view: np.ndarray = data_structure[input_array_path].npview()
    # output_array_view: np.ndarray = data_structure[output_array_path].npview()

    # message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Input: {input_array_view}'))
    # message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Output Before: {output_array_view}'))

    # output_array_view[:] = input_array_view + delta_value

    # message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Output After: {output_array_view}'))

    return nx.Result()
