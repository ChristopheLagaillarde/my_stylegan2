# Program : confirm_if_is_wanted_result
# Description : Confirm the
# Date : 02/06/22
# Author : Christophe Lagaillarde
# Version : 1.0
import logging

from change_registered_seed import change_registered_seed
from display_image import display_image

import shutil


def confirm_if_is_wanted_result(image_path: str, obtained_result: str, seed_file: str, seed: int) -> None:
    display_image('Obtained face', image_path)
<<<<<<< HEAD
    reply: str = str(input("Is this image what you are looking for ?(Y/N/Q(Quit))\n"))
=======
    reply: str = str(input("Is this image what you are looking for ?(Y/N/Q(quit)\n"))
>>>>>>> c55417290fbc59099da1764de2922b2512583c59
    if reply == 'Y':
        shutil.copyfile(image_path, f'/home/lain/PycharmProjects/my_stylegan2/saved/seed'
                        + str(seed)
                        + '.png')
        change_registered_seed(seed_file, seed)
        exit()

    if reply == 'Q':
        exit()

    else:
        print('Still searching...')

    change_registered_seed(seed_file, seed)

    return None
