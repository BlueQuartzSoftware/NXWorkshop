"""
Insert documentation here.
"""

_filters = []

"""
This section conditionally tries to import each filter
"""

# FILTER_START: Exercise1
from .Exercise1 import Exercise1
_filters.append(Exercise1)
# FILTER_END: Exercise1

# FILTER_START: Exercise2
from .Exercise2 import Exercise2
_filters.append(Exercise2)
# FILTER_END: Exercise2

# FILTER_START: Exercise3
from .Exercise3 import Exercise3
_filters.append(Exercise3)
# FILTER_END: Exercise3

# FILTER_START: Exercise4
from .Exercise4 import Exercise4
_filters.append(Exercise4)
# FILTER_END: Exercise4



import simplnx as nx

class NXWorkshopPlugin:
  """
  This class defines the plugin's basic information. 
  """
  def __init__(self) -> None:
    pass

  def id(self) -> nx.Uuid:
    """This returns the UUID of the filter. Each Plugin has a unique UUID value. DO NOT change this.
    :return: The Plugins's Uuid value
    :rtype: string
    """
    return nx.Uuid('eecde429-e9f8-41cf-9fd1-9623a7b22de7')

  def name(self) -> str:
    """The returns the name of plugin. DO NOT Change this
    :return: The name of the plugin
    :rtype: string
    """    
    return 'NXWorkshopPlugin'

  def description(self) -> str:
    """This returns the description of the plugin. Feel free to edit this.
    :return: The plugin's descriptive text
    :rtype: string
    """    
    return 'NXWorkshopPlugin'

  def vendor(self) -> str:
    """This returns the name of the organization that is writing the plugin. Feel free to edit this.
    :return: The plugin's organization
    :rtype: string
    """
    return 'Description'

  def get_filters(self):
    return _filters

