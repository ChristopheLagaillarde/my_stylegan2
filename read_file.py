# Program : read_file
# Description : read the content of a file
# Date : 11/10/22
# Author : Christophe Lagaillarde
# Version : 1.0

def read_file(file_name: str) -> int:
    with open(file_name) as f:
        content: int = int(f.read())

    return content
