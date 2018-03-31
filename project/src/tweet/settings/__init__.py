from .base import *
from .production import *
try:
    from .local import *
except:
    pass

# base and local can be same
# production and local will override base
