from color import Color

class Car_meta(type):
    def __init__(cls, *args, **kwargs):
        cls._instances = set()
        cls._log_creation_deletion = True

    @property
    def log_creation_deletion(cls):
        return cls._log_creation_deletion

    @log_creation_deletion.setter
    def log_creation_deletion(cls, val: bool):
        cls._log_creation_deletion = val

class Car(metaclass=Car_meta):
    _instances: set
    _log_creation_deletion: bool

    def __init__(self, brand: str, model: str, production_year: int, vin: str, color: Color, mileage: float):
        expected_types = {
            'brand': str,
            'model': str,
            'production_year': int,
            'vin': str,
            'color': Color,
            'mileage': (float, int)
        }

        for attr, expected_type in expected_types.items():
            value = locals()[attr]
            if not isinstance(value, expected_type):
                raise TypeError(f"Argument '{attr}' must be {expected_type}, not {type(value)}")

        if(mileage < 0):
            raise ValueError("Mileage cannot be negative")

        if(production_year < 1885):
            raise ValueError("Cars are not invented yet")

        self.brand: str = brand
        self.model: str = model
        self.production_year: int = production_year
        self.vin: str = vin
        self.color: Color = color
        self.mileage: float = float(mileage)
        i = 0
        while(i in type(self)._instances):
            i += 1

        type(self)._instances.add(i)
        self.__id = i
        if(type(self)._log_creation_deletion):
            print(f"Created car ID {i}")

    def __str__(self):
        return f"{self.brand} {self.model} manufactured at {self.production_year} with VIN {self.vin}, color code 0x{'0' * (8 - len(hex(self.color.color_code))) + hex(self.color.color_code)[2:]} and with mileage {self.mileage} kilometers"

    def __repr__(self):
        dct = self.to_dict()
        dct["color"] = repr(self.color)
        return "class Car " + str(dct)

    def __del__(self):
        try:
            type(self)._instances.remove(self.__id)
            if(type(self)._log_creation_deletion):
                print(f"Destroyed car ID {self.__id}")
        except:
            if(type(self)._log_creation_deletion):
                print(f"Removed car ID ???")

    def __copy__(self):
        return type(self).from_dict(self.to_dict())

    def __lt__(self, other):
        return self.mileage < other.mileage

    def __gt__(self, other):
        return self.mileage > other.mileage

    def __eq__(self, other):
        return type(self) == type(other) and self.brand == other.brand and self.model == other.model

    def to_dict(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'production_year': self.production_year,
            'vin': self.vin,
            'color': self.color.color_code,
            'mileage': self.mileage
        }

    @classmethod
    def from_dict(cls, d):
        if(len(d) != 6):
            raise ValueError(f'Expected dict length to be 6, found {len(d)}')

        try:
            return cls.__init__(d['brand'], d['model'], d['production_year'], d['vin'], Color(d['color']), d['mileage'])
        except KeyError as e:
            raise ValueError(f"Field {e.args[0]} not found")

