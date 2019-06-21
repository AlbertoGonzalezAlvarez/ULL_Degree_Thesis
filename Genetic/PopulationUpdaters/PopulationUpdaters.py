class PopulationUpdaters():
    method = {}

    def __init_subclass__(cls):
        if 'update' not in dir(cls):
            raise ValueError(cls.__name__ + ' has no update() method')

        PopulationUpdaters.method.update({cls.__name__: cls})