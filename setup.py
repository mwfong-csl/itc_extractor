# Copyright 2009-2012, Simon Kennedy, code@sffjunkie.co.uk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join
from distutils.core import setup

setup(name='itc',
    version='0.3.4',
    description='Extracts images from iTunes .itc files.',
    long_description="""Python2 script that extracts PNG, JPEG, and ARGB
    cover art from iTunes `.itc` files.""",
    author='Martin Fong',
    url="https://github.com/mwfong-csl/itc_extractor",
    license='Apache-2.0',
    scripts=[join('itc', 'itc.py')],
)
