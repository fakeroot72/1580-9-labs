class Planet_meta(type):
    def __init__(cls, *args, **kwargs):
        cls._instances = set()
        cls._log_creation_deletion = True

    @property
    def log_creation_deletion(cls):
        return cls._log_creation_deletion

    @log_creation_deletion.setter
    def log_creation_deletion(cls, val: bool):
        cls._log_creation_deletion = val

class Planet(metaclass=Planet_meta):
    _instances: set
    _log_creation_deletion: bool

    def __init__(self, name: str, radius: float, mass: float, sun_distance: float, planet_type: str):
        expected_types = {
            'name': str,
            'radius': float,
            'mass': (float, int),
            'sun_distance': (float, int),
            'planet_type': str
        }

        for attr, expected_type in expected_types.items():
            value = locals()[attr]
            if not isinstance(value, expected_type):
                raise TypeError(f"Argument '{attr}' must be {expected_type}, not {type(value)}")

        self.name: str = name
        self.radius: float = radius
        self.mass: float = mass
        self.sun_distance: float = sun_distance
        self.type: str = planet_type
        i = 0
        while(i in type(self)._instances):
            i += 1

        type(self)._instances.add(i)
        self.__id = i
        if(type(self)._log_creation_deletion):
            print(f"Created planet ID {i}")

    def __str__(self):
        return f"Planet {self.name} with radius {self.radius} meters, mass {self.mass} kilograms, distance to sun {self.sun_distance / 10**9} million kilometers and type \"{self.type}\""

    def __repr__(self):
        return "class Planet " + str(self.to_dict())

    def __del__(self):
        try:
            type(self)._instances.remove(self.__id)
            if(type(self)._log_creation_deletion):
                print(f"Destroyed planet ID {self.__id}")
        except:
            if(type(self)._log_creation_deletion):
                print(f"Destroyed planet ID ???")

    def __copy__(self):
        return type(self).from_dict(self.to_dict())

    # less by sun distance and equality by name just feels wrong...
    def __lt__(self, other):
        return self.sun_distance < other.sun_distance

    def __gt__(self, other):
        return self.sun_distance > other.sun_distance

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

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

