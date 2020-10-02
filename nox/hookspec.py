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
from typing import Any, Dict, List, Optional

import pluggy
from nox.sessions import Session

hookspec = pluggy.HookspecMarker("nox")
hookimpl = pluggy.HookimplMarker("nox")


class Done(enum.Enum):
    """Return from `firstresult` hooks to terminate pluggy's call loop."""

    DONE = "done"


DONE = Done.DONE


@hookspec(firstresult=True)
def nox_session_install(
    session: Session, args: List[str], kwargs: Dict[str, Any]
) -> Optional[Done]:
    """Install packages inside the session environment.

    Args:
        session (~nox.sessions.Session): The session object.
        args (List[str]): Command-line arguments for the installer. Plugins are
            allowed to modify the argument list for processing by another hook
            implementation.
        kwargs (Dict[str, Any]): Keyword arguments for
            :meth:`nox.sessions.Session.run`. Plugins are allowed to modify the
            keyword arguments for processing by another hook implementation.

    Returns:
        Plugins should return :const:`nox.hookspec.DONE` if they have serviced
        the installation request and control should return to the user. Return
        ``None`` instead to let the default implementation (and any potential
        other plugins) service the request.
    """
