class Vozel:
    """
    Osnovni sestavni del verige vozlov.
    """

    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        if self.naslednji is not None:
            return '{} -> {}'.format(self.podatek, self.naslednji)
        else:
            return '{} -> X'.format(self.podatek)