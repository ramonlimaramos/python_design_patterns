import abc
from enum import IntEnum

class PlanetEnum(IntEnum):
    MERCURY = 1
    VENUS = 2
    EARTH = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8


class PlanetHandler(metaclass=abc.ABCMeta):
    def __init__(self):
        self.next_handler = None

    @abc.abstractmethod
    def handle_request(self, request):
        pass

    def set_next_handler(self, handler):
        self.next_handler = handler


class MercuryHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.MERCURY:
            print("MercuryHandler handles " + request.name)
            print("Mercury is hot.")
        else:
            print("MercuryHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


class VenusHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.VENUS:
            print("VenusHandler handles " + request.name)
            print("Venus is poisonous.")
        else:
            print("VenusHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


class EarthHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.EARTH:
            print("EarthHandler handles " + request.name)
            print("Earth is comfortable.")
        else:
            print("EarthHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


def set_up_chain():
    mercury_handler = MercuryHandler()
    venus_handler = VenusHandler()
    earth_handler = EarthHandler()

    mercury_handler.set_next_handler(venus_handler)
    venus_handler.set_next_handler(earth_handler)

    return mercury_handler


if __name__ == '__main__':
    chain = set_up_chain()

    chain.handle_request(PlanetEnum.VENUS)
    chain.handle_request(PlanetEnum.MERCURY)
    chain.handle_request(PlanetEnum.EARTH)
    chain.handle_request(PlanetEnum.JUPITER)