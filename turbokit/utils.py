# -*- coding: utf-8 -*-
from .errors import NotRegistered

_document_registry = {}


def get_model(name):
    doc = _document_registry.get(name, None)
    if not doc:
        raise NotRegistered("""
            `%s` has not been registered in the document registry.
            Importing the document class automatically registers it, has it
            been imported?
        """.strip() % name)
    return doc


def import_base_model():
    """ To avoid circular imports """
    from .models import BaseModel
    return BaseModel


def get_simple_model():
    """ To avoid circular imports """
    from .models import SimpleMongoModel
    return SimpleMongoModel
