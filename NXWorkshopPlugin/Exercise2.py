from typing import List
import simplnx as nx

class Exercise2:

# -----------------------------------------------------------------------------
# These methods should not be edited
# -----------------------------------------------------------------------------
  def uuid(self) -> nx.Uuid:
    """This returns the UUID of the filter. Each filter has a unique UUID value
    :return: The Filter's Uuid value
    :rtype: string
    """
    return nx.Uuid('ea370568-14cb-4ed5-9d7c-464b2bde334b')

  def class_name(self) -> str:
    """The returns the name of the class that implements the filter
    :return: The name of the implementation class
    :rtype: string
    """
    return 'Exercise2'

  def name(self) -> str:
    """The returns the name of filter
    :return: The name of the filter
    :rtype: string
    """
    return 'Exercise2'

  def clone(self):
    """Clones the filter
    :return: A new instance of the filter
    :rtype:  Exercise2
    """
    return Exercise2()

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
    return 'Exercise2 (Python)'
 
  def default_tags(self) -> List[str]:
    """This returns the default tags for this filter
    :return: The default tags for the filter
    :rtype: list
    """
    return ['python', 'Exercise2']
  
  
  """
  This section should contain the 'keys' that store each parameter. The value of the key should be snake_case. The name
  of the value should be ALL_CAPITOL_KEY
  """
  A_BOOLEAN_KEY = 'my_boolean_value'
  IMAGE_DIMS_KEY = 'image_dims'
  INTERPOLATION_METHOD_KEY = "interpolation_method"
  INTERPOLATION_VALUE_KEY = "interpolation_value"

  def parameters(self) -> nx.Parameters:
    """This function defines the parameters that are needed by the filter. Parameters collect the values from the user interface
    and pack them up into a dictionary for use in the preflight and execute methods.
    """
    params = nx.Parameters()

    params.insert(nx.Parameters.Separator("Linking to a Boolean Parameter"))

    # Use the insert_linkable_parameter API to insert a parameter to which _another_ parameter will be "linked".
    params.insert_linkable_parameter(nx.BoolParameter(Exercise2.A_BOOLEAN_KEY, 'Resize the Image', 'Should we resize the image', False))

    # Insert the parameter that will be linked, is not required to be the next parameter added.
    params.insert(nx.VectorUInt64Parameter(Exercise2.IMAGE_DIMS_KEY, 'Image Size', 'The width and height of the output image.', [800, 600], ['Width', 'Height']))

    # Tell the nx.Parameters object that these to parameters are linked together and what value it is linked to.
    params.link_parameters(Exercise2.A_BOOLEAN_KEY, Exercise2.IMAGE_DIMS_KEY, True)


    params.insert(nx.Parameters.Separator("Linking to a Choice Parameter"))
    params.insert_linkable_parameter(nx.ChoicesParameter(Exercise2.INTERPOLATION_METHOD_KEY, 'Interpolation Method', 'The method used to interpolate the input data.', 0, ['Nearest', 'Linear', 'Cubic']))
    params.insert(nx.Float32Parameter(Exercise2.INTERPOLATION_VALUE_KEY, "Interpolation Value", "The value to use for interpolation", 1.0))
    params.link_parameters(Exercise2.INTERPOLATION_METHOD_KEY, Exercise2.INTERPOLATION_VALUE_KEY, 1)


    return params

  def preflight_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.PreflightResult:
    """This method preflights the filter and should ensure that all inputs are sanity checked as best as possible. Array
    sizes can be checked if the array sizes are actually known at preflight time. Some filters will not be able to report output
    array sizes during preflight (segmentation filters for example). If in doubt, set the tuple dimensions of an array to [1].
    :returns:
    :rtype: nx.IFilter.PreflightResult
    """

    # Extract the values from the user interface from the 'args' 

      
    # Create an OutputActions object to hold any DataStructure modifications that we are going to make
    output_actions = nx.OutputActions()
    
    # Create the Errors and Warnings Lists to commuicate back to the user if anything has gone wrong
    # errors = []
    # warnings = []
    # preflight_values = []

    # Send back any messages that will appear in the "Output" widget in the UI. This is optional.

    # Return the output_actions so the changes are reflected in the User Interface.
    return nx.IFilter.PreflightResult(output_actions=output_actions, errors=None, warnings=None, preflight_values=None)

  def execute_impl(self, data_structure: nx.DataStructure, args: dict, message_handler: nx.IFilter.MessageHandler, should_cancel: nx.AtomicBoolProxy) -> nx.IFilter.ExecuteResult:
    """ This method actually executes the filter algorithm and reports results.
    :returns:
    :rtype: nx.IFilter.ExecuteResult
    """
    # Extract the values from the user interface from the 'args'
    # This is basically repeated from the preflight because the variables are scoped to the method()
    
    
    # At this point the array has been allocated with the proper number of tuples and components. And we can access
    # the data array through a numpy view.
    


    # Now you can go off and use numpy or anything else that can use a numpy view to modify the data
    # or use the data in another calculation. Any operation that works on the numpy view in-place
    # has an immediate effect within the DataStructure

    # -----------------------------------------------------------------------------
    # If you want to send back progress on your filter, you can use the message_handler
    # -----------------------------------------------------------------------------
    message_handler(nx.IFilter.Message(nx.IFilter.Message.Type.Info, f'Information Message:'))

    # -----------------------------------------------------------------------------
    # If you have a long running process, check the should_cancel to see if the user cancelled the filter
    # -----------------------------------------------------------------------------
    if not should_cancel:
      return nx.Result()


    return nx.Result()




