
"""
Insert documentation here for NXWorkshopPlugin
"""
from .Plugin import NXWorkshopPlugin

__all__ = ['NXWorkshopPlugin', 'get_plugin']

"""
This section conditionally tries to import each filter
"""

# FILTER_START: Exercise1
from .Exercise1 import Exercise1
__all__.append('Exercise1')
# FILTER_END: Exercise1

# FILTER_START: Exercise2
from .Exercise2 import Exercise2
__all__.append('Exercise2')
# FILTER_END: Exercise2

# FILTER_START: Exercise3
from .Exercise3 import Exercise3
__all__.append('Exercise3')
# FILTER_END: Exercise3

# FILTER_START: Exercise4
from .Exercise4 import Exercise4
__all__.append('Exercise4')
# FILTER_END: Exercise4



def get_plugin():
  return NXWorkshopPlugin()
