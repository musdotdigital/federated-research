
import json
import cloudpickle

import substratools as tools

from substrafl.remote.remote_struct import RemoteStruct

from pathlib import Path

if __name__ == "__main__":
    # Load the wrapped user code
    remote_struct = RemoteStruct.load(src=Path(__file__).parent / 'substrafl_internal')

    # Create a Substra algo from the wrapped user code
    remote_instance = remote_struct.get_remote_instance()

    # Register the functions to substra-tools
    remote_instance.register_substratools_functions()

    # Execute the algo using substra-tools
    tools.execute()
