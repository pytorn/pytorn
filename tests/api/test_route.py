import unittest
from torn.api.route import Routing, Router
from torn.api import Controller
from torn.exception import TornNotFoundError

class DummyController(Controller):
    pass

class DummyTornadoApplication():
    pass

def create_dummy_http_request(tpath, tmethod):
    class HTTPRequest:
        def __init__(self, tpath, tmethod):
            self.path = tpath
            self.method = tmethod

    return HTTPRequest(tpath, tmethod)

class RoutingTests(unittest.TestCase):
    def test_add_route(self):
        router = Routing()
        router.add("/", DummyController)

        new_request = create_dummy_http_request("/", "GET")
        route = router.getRouteCollection().match(new_request)
        assert route.uri == "/"

    def test_route_not_found(self):
        router = Routing()
        router.add("/some-route", DummyController)

        new_request = create_dummy_http_request("/some-other-route", "GET")
        try:
            route = router.getRouteCollection().match(new_request)
            assert False
        except TornNotFoundError:
            assert True
        else:
            assert False


    def test_var_handling(self):
        router = Routing()
        router.add("/user/{userId}", DummyController).args({ 'userId': '[0-9]+' })
        
        new_request = create_dummy_http_request("/user/123", "GET")
        
        route = router.getRouteCollection().match(new_request)
        args = route.get_args(new_request)

        assert args['userId'] == '123'

        router.add("/profile/{userId}/{type}", DummyController).args({ 'userId': '[0-9]+' })

        new_request = create_dummy_http_request("/profile/123/photo", "GET")

        route = router.getRouteCollection().match(new_request)
        args = route.get_args(new_request)

        assert args['userId'] == '123' and args['type'] == 'photo'

    def test_default_var(self):
        router = Routing()
        router.add("/user/{userId}", DummyController).args({ 'userId': '[0-9]+' }).defaults({ 'userId': '2' })

        new_request = create_dummy_http_request("/user/", "GET")

        route = router.getRouteCollection().match(new_request)
        args = route.get_args(new_request)
        
        assert args['userId'] == '2'

        router.add("/profile/{userId}/{type}", DummyController).args({ 'userId': '[0-9]+' }).defaults({ 'userId': '2', 'type': 'photo'})

        new_request = create_dummy_http_request("/profile/", "GET")

        route = router.getRouteCollection().match(new_request)
        args = route.get_args(new_request)

        assert args['userId'] == '2' and args['type'] == 'photo'

        router.add("/profile/{userId}/{type}", DummyController).args({ 'userId': '[0-9]+' }).defaults({ 'userId': '2', 'type': 'photo'})
        new_request = create_dummy_http_request("/profile/123", "GET")

        route = router.getRouteCollection().match(new_request)
        args = route.get_args(new_request)
        
        assert args['userId'] == '123' and args['type'] == 'photo'

    def test_url_name(self):
        routing = Routing()
        routing.add("/", DummyController).name("index")
        routing.add("/user/{userId}", DummyController).name("userHandler")

        router = Router(DummyTornadoApplication(), routing)
        uri = router.url_for("index")

        assert uri == "/"

        uri = router.url_for("userHandler", { 'userId': '123' })

        assert uri == "/user/123"

        uri = router.url_for("nonExists")

        assert uri == ""


if __name__ == "__main__":
    unittest.main()