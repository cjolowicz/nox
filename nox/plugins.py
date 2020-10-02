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

import enum
import functools
from typing import Any, Dict, List, Optional, Tuple

import nox
import pluggy
from nox.sessions import Session

_manager = pluggy.PluginManager("nox")
hookimpl = pluggy.HookimplMarker("nox")
hookspec = pluggy.HookspecMarker("nox")
hooks = _manager.hook


class Done(enum.Enum):
    """Return from `firstresult` hooks to terminate pluggy's call loop."""

    DONE = "done"


DONE = Done.DONE


@hookspec(firstresult=True)
def nox_session_install(
    session: Session, args: List[str], kwargs: Dict[str, Any]
) -> Optional[Done]:
    """Install packages inside the session environment."""


# Avoid multiple initialization during unit tests.
@functools.lru_cache(maxsize=None)
def load() -> None:
    """Load the plugins."""
    _manager.add_hookspecs(nox.plugins)
    _manager.load_setuptools_entrypoints("nox")
    _manager.check_pending()
