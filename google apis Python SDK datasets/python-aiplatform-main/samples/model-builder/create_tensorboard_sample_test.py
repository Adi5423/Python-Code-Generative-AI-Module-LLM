# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import create_tensorboard_sample
import test_constants as constants


def test_create_tensorboard_sample(mock_sdk_init, mock_create_tensorboard):

    create_tensorboard_sample.create_tensorboard_sample(
        project=constants.PROJECT,
        display_name=constants.DISPLAY_NAME,
        location=constants.LOCATION,
    )

    mock_sdk_init.assert_called_once_with(
        project=constants.PROJECT, location=constants.LOCATION
    )

    mock_create_tensorboard.assert_called_once_with(
        display_name=constants.DISPLAY_NAME,
        project=constants.PROJECT,
        location=constants.LOCATION,
    )
