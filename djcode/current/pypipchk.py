'''
    pip
'''
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


dists = importlib_metadata.distributions()
for dist in dists:
    name = dist.metadata["Name"]
    version = dist.version
    oslicense = dist.metadata["License"]
    print(f'found distribution {name}=={version}')
