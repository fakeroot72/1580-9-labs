from planet import Planet
from car import Car
from db import DataBaseManager
from color import Color

def print_help():
    print("""0. Create new database (DB)
1. Load DB
2. Save DB
3. Print DB
4. Add to DB
5. Find DB field
6. Edit DB field
7. Delete DB field
8. Sort DB fields
9. Help (print this menu)
10. Exit
""", end='')

def create_planet() -> Planet:
    print("--- Creating a new Planet ---")
    try:
        name = input("Name: ")
        radius = float(input("Radius (meters): "))
        mass = float(input("Mass (kilograms): "))
        sun_distance = float(input("Distance to sun (meters): "))
        planet_type = input("Planet type (e.g., Gas Giant, Terrestrial): ")
        return Planet(name, radius, mass, sun_distance, planet_type)
    except ValueError as e:
        print(str(e))
        return None

def create_car() -> Car:
    print("--- Creating a new Car ---")
    try:
        brand = input("Brand: ")
        model = input("Model: ")
        production_year = int(input("Production Year: "))
        vin = input("VIN: ")
        color_hex = int(input("Color Code (in hex, e.g. 0xff0000 for red): "), 16)
        mileage = float(input("Mileage: "))
        return Car(brand, model, production_year, vin, Color(color_hex), mileage)
    except ValueError as e:
        print(str(e))
        return None

def main():
    print_help()
    db: DataBaseManager = None
    unsaved_changes = False
    while(True):
        try:
            choose = input("Command: ")
            match choose:
                case '0':
                    if(unsaved_changes):
                        if(input("This will overwrite existing database. Are you sure? (y/N): ").lower() != 'y'):
                            print("Not overwriting")
                            continue

                    db = DataBaseManager()
                    print("Database created")

                case '1':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    if(unsaved_changes):
                        if(input("This will overwrite existing database. Are you sure? (y/N): ").lower() != 'y'):
                            print("Not overwriting")
                            continue

                    filename = input("Name of file where db is located: ")
                    try:
                        db.load(filename)
                    except OSError:
                        print("Failed to open database file (does it exists?)")
                        continue

                    print("Database loaded")

                case '2':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    filename = input("Name of file where db will be saved: ")
                    try:
                        db.save(filename)
                    except OSError:
                        print("Failed to open database file")
                        continue

                    unsaved_changes = False
                    print("Database saved")

                case '3':
                    print(str(db.db))

                case '4':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    cls = input("Type for addition to db (car/planet): ").lower()
                    instance = None
                    match cls:
                        case "planet":
                            instance = create_planet()
                        case "car":
                            instance = create_car()
                        case _:
                            print("Type not found!\nAvailable types: car, planet")

                    if(instance == None):
                        continue

                    db.add(instance)
                    print(f"added new {cls}")

                case '5':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    attr = input("Enter object attribute to search by (e.g., 'name' for planet, 'brand' for car): ")
                    val = input(f"Enter the value for '{attr}': ")

                    found = db.search(val, key=lambda x: str(getattr(x, attr, "")))
                    if found:
                        print(f"Found: {str(found)}")
                    else:
                        print("Item not found in database.")

                case '6':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    attr = input("Enter attribute of the object to edit (e.g., 'name', 'brand'): ")
                    val = input(f"Enter the value for '{attr}' to find it: ")

                    old_val = db.search(val, key=lambda x: str(getattr(x, attr, "")))
                    if old_val == None:
                        print("Item not found.")
                        continue

                    print(f"Editing: {repr(old_val)}")
                    cls = input("Type of new replacement (car/planet): ").lower()
                    instance = None
                    match cls:
                        case "planet":
                            instance = create_planet()
                        case "car":
                            instance = create_car()
                        case _:
                            print("type not found!\nAvailable types: car, planet")

                    if(instance == None):
                        continue

                    db.change(old_val, instance)
                    print("Successfully updated database field.")

                case '7':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    attr = input("Enter attribute of the object to delete (e.g., 'name', 'brand'): ")
                    val = input(f"Enter the value for '{attr}' to find it: ")

                    old_val = db.search(val, key=lambda x: str(getattr(x, attr, "")))
                    if old_val == None:
                        print("Item not found.")
                        continue

                    db.remove(old_val)
                    print(f"Successfully deleted {old_val}")

                case '8':
                    if(db == None):
                        print("Database is not initialized.")
                        continue

                    attr = input("Enter attribute to sort the entire database by (e.g., 'mileage', 'mass'): ")
                    db.sort(cmp_less=lambda a, b: getattr(a, attr, float('inf')) < getattr(b, attr, float('inf')))
                    print("Successfully sorted database.")

                case '9':
                    print_help()

                case '10':
                    print("Exiting...")
                    break

                case _:
                    print("Unknown command. Type '9' for help.")

            try:
                unsaved_changes = (4 <= int(choose) <= 9)
            except: pass
            print()

        except KeyboardInterrupt: print()
        except EOFError: break

    return 0

if(__name__ == "__main__"):
    __import__('sys').exit(main())
