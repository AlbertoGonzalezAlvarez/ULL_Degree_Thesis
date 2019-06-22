class PopulationUpdaters():

    type = {}

    def __init_subclass__(cls):
        PopulationUpdaters.type.update({cls.__name__: cls})