# SPDX-FileCopyrightText: Copyright (c) 2023-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest
from _test_utils.examples.run_command import run_vlm_ptq_command
from _test_utils.model import LLAVA_PATH
from _test_utils.torch_misc import minimum_gpu


@pytest.mark.parametrize("quant", ["fp16"])
@minimum_gpu(2)
def test_llava_multi_gpu(quant):
    run_vlm_ptq_command(model=LLAVA_PATH, type="llava", quant=quant, tp=2)
