class Planet_meta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instances = set()
        cls.__log_creation_deletion = True

    @property
    def log_creation_deletion(cls):
        return cls.__log_creation_deletion

    @log_creation_deletion.setter
    def log_creation_deletion(cls, val: bool):
        cls.__log_creation_deletion = val

class Planet(metaclass=Planet_meta):
    __instances: set
    __log_creation_deletion: bool

    def __init__(self, name: str, radius: float, mass: float, sun_distance: float, planet_type: str):
        self.name: str = name
        self.radius: float = radius
        self.mass: float = mass
        self.sun_distance: float = sun_distance
        self.type: str = planet_type
        i = 0
        while(i in type(self).__instances):
            i += 1

        type(self).__instances.add(i)
        self.__id = i
        if(type(self).__log_creation_deletion):
            print(f"Created planet ID {i}")

    def __str__(self):
        return f"Planet {self.name} with radius {self.radius} meters, mass {self.mass} kilograms, distance to sun {self.sun_distance / 10**9} million kilometers and type \"{self.type}\""

    def __repr__(self):
        return str(self.to_dict())

    def __del__(self):
        type(self).__instances.remove(self.__id)
        if(type(self).__log_creation_deletion):
            print(f"Destroyed planet ID {self.__id}")

    def __copy__(self):
        return type(self).from_dict(self.to_dict())

    # less by sun distance and equality by name just feels wrong...
    def __lt__(self, other):
        return self.sun_distance < other.sun_distance

    def __gt__(self, other):
        return self.sun_distance > other.sun_distance

    def __eq__(self, other):
        return self.name == other.name

    def to_dict(self):
        return {
            'name': self.name,
            'radius': self.radius,
            'mass': self.mass,
            'sun_distance': self.sun_distance,
            'type': self.type
        }

    @classmethod
    def from_dict(cls, d):
        if(len(d) != 5):
            raise ValueError(f'Expected dict lenght to be 5, found {len(d)}')

        try:
            return cls.__init__(d['name'], d['radius'], d['mass'], d['sun_distance'], d['type'])
        except KeyError as e:
            raise ValueError(f"Field {e.args[0]} not found")

