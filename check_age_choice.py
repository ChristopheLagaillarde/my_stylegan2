# Program : check_age_choice
# Description : get the age choice of the user
# Date : 28/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import logging
import sys


def check_age_choice(choice_age_interval_1: str, choice_age_interval_2: str) -> None:
    try:
        choice_age_interval_1: int = int(choice_age_interval_1)
        choice_age_interval_2: int = int(choice_age_interval_2)
        available_age_interval: list = [(0, 2), (4, 6), (8, 12), (15, 20), (25, 32), (38, 43), (48, 53), (60, 100)]

        if choice_age_interval_1 > choice_age_interval_2:
            logging.error(f'Please put the age interval in the correct order:\n'
                          f'({choice_age_interval_2},{choice_age_interval_1}) and not '
                          f'({choice_age_interval_1},{choice_age_interval_2})')
            sys.exit()

        if (choice_age_interval_1, choice_age_interval_2) not in available_age_interval:
            logging.error(f' Age interval should be either:\n'
                          f'(0, 2),(4, 6), (8, 12),(15, 20),(25, 32),'
                          f'(38, 43),(48, 53) or (60, 100)\n'
                          f'But got ({choice_age_interval_1}, {choice_age_interval_2}) instead')
            sys.exit()

        return None

    except ValueError:
        logging.error(f'Age should be a number written a number like 15,32... '
                      f'and not "{choice_age_interval_1}" or "{choice_age_interval_2}"')
        sys.exit()


