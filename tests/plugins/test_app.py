
import torn.plugins.app
import unittest
import os


class AppPluginsTests(unittest.TestCase):

    def test_settings_reader(self):
        class DummyApplication:
            def __init__(self):
                self.root_dir = os.getcwd() + "/tests/test_utils"
        
        instance = DummyApplication()
        instance = torn.plugins.app.settings(instance)

        assert instance.host == "http://localhost" and \
            instance.port == 7080 and \
            instance.debug == False and \
            instance.name == "app"

    def test_settings_default(self):
        class DummyApplication:
            def __init__(self):
                self.root_dir = os.getcwd() + "/tests/not_valid"
        
        instance = DummyApplication()
        instance = torn.plugins.app.settings(instance)

        assert instance.host == "http://localhost" and \
            instance.port == 8000 and \
            instance.debug == True and \
            instance.name == "Torn App"