class IndividualTypes():

    type = {}

    def __init_subclass__(cls):
        IndividualTypes.type.update({cls.__name__: cls})