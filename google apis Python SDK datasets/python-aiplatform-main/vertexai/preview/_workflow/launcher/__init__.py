# -*- coding: utf-8 -*-

# Copyright 2023 Google LLC
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
#

from typing import Any

from vertexai.preview._workflow import executor
from vertexai.preview._workflow import shared


class _WorkflowLauncher:
    """Launches workflows either locally or remotely."""

    def launch(self, invokable: shared._Invokable, global_remote: bool, rewrapper: Any):

        local_remote = invokable.vertex_config.remote

        if local_remote or (local_remote is None and global_remote):
            result = self._remote_launch(invokable, rewrapper)
        else:
            for _, arg in invokable.bound_arguments.arguments.items():
                if "bigframes" in repr(type(arg)):
                    raise ValueError(
                        "Bigframes not supported if vertexai.preview.init(remote=False)"
                    )
            result = self._local_launch(invokable)
        return result

    def _remote_launch(self, invokable: shared._Invokable, rewrapper: Any) -> Any:
        result = executor._workflow_executor.remote_execute(
            invokable, rewrapper=rewrapper
        )
        # TODO(b/277343861) workflow tracking goes here
        # E.g., initializer.global_config.workflow.add_remote_step(invokable, result)

        return result

    def _local_launch(self, invokable: shared._Invokable) -> Any:
        result = executor._workflow_executor.local_execute(invokable)
        # TODO(b/277343861) workflow tracking goes here
        # E.g., initializer.global_config.workflow.add_local_step(invokable, result)

        return result
