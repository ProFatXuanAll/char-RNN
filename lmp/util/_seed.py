r"""Helper function for setting random seed.

Usage:
    import lmp.util

    lmp.set_seed(...)
    lmp.set_seed_by_config(...)
"""


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import random

import numpy as np
import torch


def set_seed(seed: int) -> None:
    r"""Helper function for setting random seed.

    Args:
        seed:
            Control random seed and let experiment reproducible. Must be bigger
            than or equal to `1`.

    Raises:
        TypeError:
            When `seed` is not an instance of `int`.
        ValueError:
            When `seed < 1`.
    """
    # Type check.
    if not isinstance(seed, int):
        raise TypeError('`seed` must be an instance of `int`.')

    # Value check.
    if seed < 1:
        raise ValueError('`seed` must be bigger than or equal to `1`.')

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

