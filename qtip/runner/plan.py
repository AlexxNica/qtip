##############################################################################
# Copyright (c) 2016 ZTE Corp and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

from qtip.base.benchmark import Benchmark, Property
from qtip.runner.suite import Suite


class Plan(Benchmark):
    """
    a benchmark plan is consist of basic information and  several suites"""

    DEFAULT_DIR = 'plans'

    def __init__(self, name, paths=None):
        super(Plan, self).__init__(name, paths=paths)
        content = self.content()

        self.info = content[Property.INFO]
        self.suites = [Suite(suite, paths=paths)
                       for suite in content[Property.SUITES]]