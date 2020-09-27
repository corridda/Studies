"""https://t.me/pythonetc/231"""

import os.path

from pathlib import Path


"""Python allows you to work with filesystem paths with the os.path module.
The module contains a lot of functions that treat strings as paths and perform useful operations
like concating paths and stuff like that:"""
print(f"os.path.join('/usr', 'local'): {os.path.join('/usr', 'local')}")
print(f"os.path.dirname('/var/log'): {os.path.dirname('/var/log')}\n")

"""However, since Python 3.4 the new pathlib module is available which offers an object-oriented approach:"""
print(f"Path('/usr') / Path('local'): {Path('/usr') / Path('local')}")
print(f"Path('/usr') / 'local': {Path('/usr') / 'local'}")
print(f"Path('/var/log').parent: {Path('/var/log').parent}")
print(f"Path('/var/log').parent.name'): {Path('/var/log').parent.name}")
