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

import pluggy

_manager = pluggy.PluginManager("nox")
hooks = _manager.hook


# Avoid multiple initialization during unit tests.
@functools.lru_cache(maxsize=None)
def load() -> None:
    """Load the plugins.

    Register the hook specifications (:mod:`nox.hookspec`) and the default hook
    implementations (:mod:`nox.hookimpl`), then scan the setuptools entry
    points for Nox plugins. Plugins may be registered by including a section like
    the following in setup.cfg, for an imaginary ``nox-example`` plugin::

    .. code-block:: ini

        [options.entry_points]
        nox =
            example = nox_example

    .. note::

        To facilitate testing, this function may be called multiple times. It
        is a no-op after the first call.
    """
    import nox.hookspec
    import nox.hookimpl

    _manager.add_hookspecs(nox.hookspec)
    _manager.register(nox.hookimpl)
    _manager.load_setuptools_entrypoints("nox")
    _manager.check_pending()
