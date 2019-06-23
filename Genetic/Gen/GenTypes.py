class GenTypes:

    type = {}

    def __init_subclass__(cls):
        GenTypes.type.update({cls.__name__: cls})