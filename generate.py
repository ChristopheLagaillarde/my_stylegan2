# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

"""Generate images using pretrained network pickle."""
import logging
import os
from typing import Optional

import click
import dnnlib
import numpy as np
import PIL.Image
import torch

import legacy
from age_and_gender_detection import predict_age_and_gender
from check_age_choice import check_age_choice
from check_gender_choice import check_gender_choice
from confirm_if_is_wanted_result import confirm_if_is_wanted_result
from read_file import read_file

@click.command()
@click.pass_context
@click.option('--gender', 'wanted_gender', help='Wanted gender', required=True)
@click.option('--min-age', 'min_age', help='Minimal age', required=True)
@click.option('--max-age', 'max_age', help='Maximum age', required=True)
@click.option('--network', 'network_pkl', help='Network pickle filename', required=True)
@click.option('--trunc', 'truncation_psi', type=float, help='Truncation psi', default=1, show_default=True)
@click.option('--class', 'class_idx', type=int, help='Class label (unconditional if not specified)')
@click.option('--noise-mode', help='Noise mode', type=click.Choice(['const', 'random', 'none']), default='const', show_default=True)
@click.option('--outdir', help='Where to save the output images', type=str, required=True, metavar='DIR')
def generate_images(
    ctx: click.Context,
    wanted_gender: str,
    min_age: str,
    max_age: str,
    network_pkl: str,
    truncation_psi: float,
    noise_mode: str,
    outdir: str,
    class_idx: Optional[int],
):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    seed_file: str = 'seed.txt'
    seed: int = read_file(seed_file) + 1
    obtained_result: str = 'Starting'
    image_path: str = "images/seed.png"

    wanted_age: str = f'({min_age}, {max_age})'

    check_gender_choice(wanted_gender)
    check_age_choice(min_age, max_age)

    device = torch.device('cuda')
    with dnnlib.util.open_url(network_pkl) as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device) # type: ignore

    os.makedirs(outdir, exist_ok=True)

    # Labels.
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            ctx.fail('Must specify class label with --class when using a conditional network')
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print ('warn: --class=lbl ignored when running on an unconditional network')

    # Generate images.
    while True:
        z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
        img = G(z, label, truncation_psi=truncation_psi, noise_mode=noise_mode)
        img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)

        PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB').save(f'{outdir}/seed.png')
        obtained_result = predict_age_and_gender('images/seed.png')
        logging.info(obtained_result)

        if obtained_result is None:
            pass

        else:
            if wanted_gender in obtained_result and wanted_age in obtained_result:
                confirm_if_is_wanted_result(image_path, obtained_result, seed_file, seed)
                obtained_result = 'Reset'

        seed += 1


if __name__ == "__main__":
    generate_images()

