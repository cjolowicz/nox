# Copyright 2020 Alethea Katherine Flowers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools
from typing import Any
from typing import Optional
from typing import Tuple

import pluggy

import nox
from nox.sessions import Session


_manager = pluggy.PluginManager("nox")
hookimpl = pluggy.HookimplMarker("nox")
hookspec = pluggy.HookspecMarker("nox")
hooks = _manager.hook


@hookspec(firstresult=True)
def nox_session_install(
    session: Session, *args: str, **kwargs: Any
) -> Optional[Tuple[()]]:
    """Install packages inside the session environment."""


# Avoid multiple initialization during unit tests.
@functools.lru_cache(maxsize=None)
def load():
    """Load the plugins."""
    _manager.add_hookspecs(nox.plugins)
    _manager.load_setuptools_entrypoints("nox")
    _manager.check_pending()
