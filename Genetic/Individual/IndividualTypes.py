class IndividualTypes():

    types = {}

    def __init_subclass__(cls):
        IndividualTypes.types.update({cls.__name__: cls})