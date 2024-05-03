from typing import List
import simplnx as nx

class Exercise3:

# -----------------------------------------------------------------------------
# These methods should not be edited
# -----------------------------------------------------------------------------
  def uuid(self) -> nx.Uuid:
    """This returns the UUID of the filter. Each filter has a unique UUID value
    :return: The Filter's Uuid value
    :rtype: string
    """
    return nx.Uuid('23f9cded-a94e-4d79-a283-fd573abbdee2')

  def class_name(self) -> str:
    """The returns the name of the class that implements the filter
    :return: The name of the implementation class
    :rtype: string
    """
    return 'Exercise3'

  def name(self) -> str:
    """The returns the name of filter
    :return: The name of the filter
    :rtype: string
    """
    return 'Exercise3'

  def clone(self):
    """Clones the filter
    :return: A new instance of the filter
    :rtype:  Exercise3
    """
    return Exercise3()

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
    return 'Exercise3 (Python)'
 
  def default_tags(self) -> List[str]:
    """This returns the default tags for this filter
    :return: The default tags for the filter
    :rtype: list
    """
    return ['python', 'Exercise3']
  
  
  """
  This section should contain the 'keys' that store each parameter. The value of the key should be snake_case. The name
  of the value should be ALL_CAPITOL_KEY
  """
  A_BOOLEAN_KEY = 'my_boolean_value'

  def parameters(self) -> nx.Parameters:
    """This function defines the parameters that are needed by the filter. Parameters collect the values from the user interface
    and pack them up into a dictionary for use in the preflight and execute methods.
    """
    params = nx.Parameters()
    params.insert(nx.BoolParameter(Exercise3.A_BOOLEAN_KEY, 'Cause Error', 'This will cause an error', False))

    return params

  def preflight_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.PreflightResult:
    """This method preflights the filter and should ensure that all inputs are sanity checked as best as possible. Array
    sizes can be checked if the array sizes are actually known at preflight time. Some filters will not be able to report output
    array sizes during preflight (segmentation filters for example). If in doubt, set the tuple dimensions of an array to [1].
    :returns:
    :rtype: nx.IFilter.PreflightResult
    """
    bool_value = args[Exercise3.A_BOOLEAN_KEY]

    # Create an OutputActions object to hold any DataStructure modifications that we are going to make
    output_actions = nx.OutputActions()
    
    # Create the Errors and Warnings Lists to commuicate back to the user if anything has gone wrong
    # errors = []
    warnings = []
    # preflight_values = []

    # Create a nx.Warning and append it onto the warnings[] list.
    warnings.append(nx.Warning(-65020, "Warning from preflight"))

    if bool_value:
      return nx.IFilter.PreflightResult(None, [nx.Error(-8700, f"Preflight threw an error")])


    # Return the output_actions so the changes are reflected in the User Interface.
    return nx.IFilter.PreflightResult(output_actions=output_actions, errors=None, warnings=warnings, preflight_values=None)

  def execute_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.ExecuteResult:
    """ This method actually executes the filter algorithm and reports results.
    :returns:
    :rtype: nx.IFilter.ExecuteResult
    """

    # -----------------------------------------------------------------------------
    # If you want to send back progress on your filter, you can use the message_handler
    # -----------------------------------------------------------------------------
    message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Information Message'))

    # -----------------------------------------------------------------------------
    # If you have a long running process, check the should_cancel to see if the user cancelled the filter
    # -----------------------------------------------------------------------------
    if not should_cancel:
      return nx.Result()


    return nx.Result()




