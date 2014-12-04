#!/usr/bin/python
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import optparse
import os
import sys
import unittest


USAGE = """%prog TEST_PATH
Run unit tests for App Engine apps.
TEST_PATH   Path to package containing test modules.
Please set GOOGLE_APPENGINE_SDK_PATH environment varialbe.
"""

PROJECT_DIR = os.path.abspath(
    os.path.dirname(
        os.path.dirname(__file__)))


def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    sys.path.insert(0, PROJECT_DIR)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 1:
        print 'Error: Exactly 1 argument required.'
        parser.print_help()
        sys.exit(1)
    sdk_path = os.environ.get('GOOGLE_APPENGINE_SDK_PATH')
    test_path = args[0]
    main(sdk_path, test_path)
