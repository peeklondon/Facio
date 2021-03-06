import os
import sys
import unittest


class BaseTestCase(unittest.TestCase):

    test_tpl_path = os.path.join(os.path.dirname(__file__), 'test_template')
    test_cfg_base_path = os.path.join(os.path.dirname(__file__),
            'test_cfgs')

    def _test_cfg_path(self, fname):
        return os.path.join(self.test_cfg_base_path, fname)

    @property
    def empty_cfg(self):
        return self._test_cfg_path('empty.cfg')

    @property
    def multiple_templates_cfg(self):
        return self._test_cfg_path('multiple_templates.cfg')
