import unittest
from torn.api.route import Routing

class DummyController:
    pass

class RoutingTests(unittest.TestCase):
    def test_get(self):
        router = Routing()
        router.get("/", "index", DummyController)
        self.assertEqual(router.routes['index']['uri'], '/')
        self.assertEqual(router.routes['index']['method'][0], 'GET')


if __name__ == "__main__":
    unittest.main()