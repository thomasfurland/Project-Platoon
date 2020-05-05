class MapFactory:
    _instances = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        MapFactory._instances[cls._unique_key] = cls()

    def __call__(cls, unique_key):
        if unique_key in MapFactory._instances:
            return MapFactory._instances[unique_key]
        else:
            print(len(MapFactory._instances))
            raise KeyError("Instance not found in MapFactory. Check unique_key.")

#class MetaFactory(type):
#    def __new__(cls, *args, **kwargs):
        


