import pickle
import sort

class DataBaseManager:
    def __init__(self, always_sorted: bool = False, cmp_less = None, single: bool = False, single_object = None):
        self.__single = single
        if(not single):
            self.__db = []
        else:
            self.__db = single_object

        self.always_sorted = always_sorted
        self.__sorted = True
        self.cmp_less = None

    @property
    def db(self):
        return self.__db[:] if not self.__single else self.__db

    @property
    def sorted(self):
        return self.__sorted

    @property
    def single(self):
        return self.__single

    def add(self, object):
        if(self.__single):
            raise ValueError("Can't add to single object.")

        self.__db.append(object)
        self.__sorted = False
        if(self.always_sorted):
            self.sort()

    def remove(self, object):
        if(self.__single):
            raise ValueError("Can't remove single object.")

        self.__db.remove(object)

    def change(self, old_value, new_value):
        if(self.__single and self.__db != old_value):
            raise ValueError(f"{old_value.__repr__()} is not in list")

        if(self.__single):
            self.__db = new_value
        else:
            self.__db[self.__db.index(old_value)] = new_value
            self.__sorted = False
            if(self.always_sorted):
                self.sort()

    def sort(self, cmp_less=None):
        self.__sorted = True
        if(self.__single):
            return

        if(self.cmp_less != None and cmp_less == None):
            cmp_less = self.cmp_less

        if(self.always_sorted):
            sort.bubble(self.__db, cmp_less)
        else:
            sort.merge(self.__db, cmp_less)

    def search(self, target, binary_search: bool = False, key=None):
        if(key == None):
            key = lambda a : a

        if(binary_search):
            if(not self.__sorted):
                print("\x1b[33mWARNING: \x1b[0using binary search on unsorted list")
            try:
                low = 0
                high = len(self.__db) - 1
                while low <= high:
                    mid = (low + high) // 2
                    guess = self.__db[mid]

                    if key(guess) == target:
                        return guess

                    if key(guess) > target:
                        high = mid - 1
                    else:
                        low = mid + 1

                return None
            except:
                pass # fall back to dumb search

        index = None
        keyed = tuple(map(key, self.__db))
        try:
            index = keyed.index(target)
        except ValueError:
            pass

        return self.__db[index] if index != None else None

    def save(self, filename: str):
        with open(filename, 'wb') as output:
            pickle.dump(self.__db, output)

    def load(self, filename: str):
        with open(filename, 'rb') as input:
            db = pickle.load(input)
            if(type(db) != list and not self.__single):
                raise ValueError("Deserialized data is invalid.")

            self.__db = db
            self.__sorted = self.__single
            if(self.always_sorted):
                self.sort()
