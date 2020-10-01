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

from typing import Any
from typing import Optional

import pluggy

from nox.sessions import Session


manager = pluggy.PluginManager("nox")
hookimpl = pluggy.HookimplMarker("nox")
hookspec = pluggy.HookspecMarker("nox")


@hookspec(firstresult=True)
def nox_session_install(session: Session, *args: str, **kwargs: Any) -> Optional[bool]:
    """Install packages inside the session environment."""


def load():
    """Load the plugins."""
    manager.add_hookspecs(nox.plugins)
    manager.load_setuptools_entrypoints("nox")
    manager.check_pending()
