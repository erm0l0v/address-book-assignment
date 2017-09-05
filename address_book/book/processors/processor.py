class Processor(object):
    index_classes = []

    def __init__(self, book):
        self.book = book

    def collection(self):
        raise NotImplementedError('Not implemented')

    def add(self, value):
        raise NotImplementedError('Not implemented')

    def discard(self, value):
        raise NotImplementedError('Not implemented')
