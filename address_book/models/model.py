import abc
from six import with_metaclass


class Model(with_metaclass(abc.ABCMeta)):
    @property
    @abc.abstractmethod
    def key(self):
        pass

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)
