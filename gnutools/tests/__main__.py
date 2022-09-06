import os
from .functional import test_imports
from gnutools.fs import parent
test_imports(parent(os.path.realpath(__file__), level=2))