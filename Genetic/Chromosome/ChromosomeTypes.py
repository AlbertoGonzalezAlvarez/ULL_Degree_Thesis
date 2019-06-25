class ChromosomeTypes():

    type = {}

    def __init_subclass__(cls):
        ChromosomeTypes.type.update({cls.__name__: cls})