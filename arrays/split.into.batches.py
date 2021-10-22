
   
# coding=utf-8
# Copyright 2020 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Functions that are used on array like variables/objects"""

import numpy as np
import warnings

def batch_array(list_values, batch_size):
    r"""
    Split a list into batches/chunks. Last batch size is remaining of list values.
    Note:
      This is also called chunking. I call it batches since I use it more in ML.
    Arguments:
        list_values (:obj:`list / np.ndarray`):
            Can be any kind of list/array.
        batch_size (:obj:`int`):
            Value of the batch length.
    Returns:
        :obj:`np.ndarray`: List of batches from list_values.
    Raises:
        UserWarning: If `batch_size` is greater than length of `list_values`.
        ValueError: If `list_values` is not valid format.
    """

    if isinstance(list_values, list) or isinstance(list_values, np.ndarray):
        # make sure to warn user if `list_value` has correct type

        if len(list_values) < batch_size:
            # make sure batch size is not greater than length of list
            warnings.warn("`batch_size` is greater than length of `list_values`!", UserWarning)

            return [list_values]

        # create new list of batches
        batched_list = [list_values[i * batch_size:(i + 1) * batch_size] for i in
                        range((len(list_values) + batch_size - 1) // batch_size)]

        return batched_list

    else:
        # raise error if `list_values` is not of type array
        raise ValueError("`list_values` must be of type list!")