
"""
Insert documentation here for NXWorkshopPlugin
"""
from NXWorkshopPlugin.Plugin import NXWorkshopPlugin

__all__ = ['NXWorkshopPlugin', 'get_plugin']

"""
This section conditionally tries to import each filter
"""

# FILTER_START: Exercise1
try:
  from NXWorkshopPlugin.Exercise1 import Exercise1
  __all__.append('Exercise1')
except ImportError:
  pass
# FILTER_END: Exercise1

# FILTER_START: Exercise2
try:
  from NXWorkshopPlugin.Exercise2 import Exercise2
  __all__.append('Exercise2')
except ImportError:
  pass
# FILTER_END: Exercise2

# FILTER_START: Exercise3
try:
  from NXWorkshopPlugin.Exercise3 import Exercise3
  __all__.append('Exercise3')
except ImportError:
  pass
# FILTER_END: Exercise3

# FILTER_START: Exercise4
try:
  from NXWorkshopPlugin.Exercise4 import Exercise4
  __all__.append('Exercise4')
except ImportError:
  pass
# FILTER_END: Exercise4

def get_plugin():
  return NXWorkshopPlugin()
