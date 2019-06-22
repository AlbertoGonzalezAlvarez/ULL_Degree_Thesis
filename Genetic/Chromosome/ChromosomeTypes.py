class ChromosomeTypes():

    types = {}

    def __init_subclass__(cls):
        ChromosomeTypes.types.update({cls.__name__: cls})