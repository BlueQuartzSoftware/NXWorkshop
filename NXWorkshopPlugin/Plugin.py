"""
Insert documentation here.
"""

_filters = []

"""
This section conditionally tries to import each filter
"""

# FILTER_START: Exercise1
try:
  from NXWorkshopPlugin.Exercise1 import Exercise1
  _filters.append(Exercise1)
except ImportError:
  pass
# FILTER_END: Exercise1

# FILTER_START: Exercise2
try:
  from NXWorkshopPlugin.Exercise2 import Exercise2
  _filters.append(Exercise2)
except ImportError:
  pass
# FILTER_END: Exercise2

# FILTER_START: Exercise3
try:
  from NXWorkshopPlugin.Exercise3 import Exercise3
  _filters.append(Exercise3)
except ImportError:
  pass
# FILTER_END: Exercise3

# FILTER_START: Exercise4
try:
  from NXWorkshopPlugin.Exercise4 import Exercise4
  _filters.append(Exercise4)
except ImportError:
  pass
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
    return nx.Uuid('43c68d9a-3205-479c-a280-648617837580')

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

