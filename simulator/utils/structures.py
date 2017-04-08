

class HashDict(dict):
    """
    These HashDicts are expected to be frozen.
    Rude workaround to satisfy DRF.
    USE WITH EXTREME CAUTION!
    """

    def __key(self):
        return tuple((k, self[k]) for k in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()
