# Program : read_file
# Description : read the content of a file
# Date : 11/10/22
# Author : Christophe Lagaillarde
# Version : 1.0

def change_registered_seed(file_name: str, current_seed: int) -> str:
    new_seed: str = str(current_seed + 1)

    with open(file_name, 'w') as f:
        f.write(new_seed)

    return new_seed
