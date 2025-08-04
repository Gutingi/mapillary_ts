# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'gutingi.dev@gmail.com'
__date__ = '2025-07-29'
__copyright__ = 'Copyright 2025, Gutingi'

import unittest

from qgis.PyQt.QtGui import QIcon



class mapillary_traffic_signsDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/mapillary_traffic_signs/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(mapillary_traffic_signsResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



