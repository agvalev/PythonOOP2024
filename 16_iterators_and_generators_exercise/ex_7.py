from typing import Iterable


def read_next(*collections: Iterable):
    for collection in collections:
        #  for el in collection:
        #    yield el
        yield from collection
