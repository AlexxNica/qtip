##############################################################################
# Copyright (c) 2017 ZTE Corporation and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################


from qtip.reporter import filters
from jinja2 import Environment


def test_justify():
    env = Environment()
    env.filters['justify'] = filters.justify
    template = env.from_string('{{ kvpair|justify(width=10) }}')
    assert template.render(kvpair=('key', 'value')) == 'key..value'