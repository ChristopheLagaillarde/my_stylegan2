# Program : check_gender_choice
# Description : get the gender choice of the user
# Date : 28/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import sys
import logging


def check_gender_choice(choice: str) -> None:
    logging.basicConfig(level=logging.ERROR)

    if choice == 'Male' or choice == 'Female':
        return None
    else:
        logging.error('Only Male and Female accepted')
        sys.exit()