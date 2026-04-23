class Planet:
    __instances: set = set()
    __log_creation_deletion: bool = true

    __id: int = 0
    name: string = 'none'
    radius: float = 0.0
    mass: float = 0.0
    sun_distance: float = 0.0
    type: string = 'none'

    def __init__(name: string, radius: float, mass: float, sun_distance: float, type: string):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.sun_distance = sun_distance
        self.type = type
        i = 0
        while(i in type(self).__instances):
            i += 1
        type(self).__instances.add(i)
        __id = i
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

    @property
    def log_creation_deletion(self):
        return type(self).__log_creation_deletion

    @log_creation_deletion.setter
    def log_creation_deletion(self, val: bool):
        type(self).__log_creation_deletion = val

    def to_dict(self):
        return {
            'name': self.name,
            'radius': self.radius,
            'mass': self.mass,
            'sun_distance': sun_distance
            'type': type
        }

    @classmethod
    def from_dict(cls, d):
        if(len(d) != 5):
            raise ValueError(f'Expected dict lenght to be 5, found {len(d)}')

        try:
            return cls.__init__(d['name'], d['radius'], d['mass'], d['sun_distance'], d['type'])
        except KeyError as e:
            raise ValueError(f"Field {e.args[0]} not found")

