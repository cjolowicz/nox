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

import pluggy

hookimpl = pluggy.HookimplMarker("nox")

def get_plugin_manager():
    """Initialize the plugin manager."""
    pm = pluggy.PluginManager("nox")

    pm.add_hookspecs(nox.plugins)
    pm.load_setuptools_entrypoints("nox")
    pm.check_pending()

    return pm
