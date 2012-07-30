#coding: utf-8
from clausula.base import clauses

def resolve(obj):
    "always Fail"
    return False

clauses.register(resolve, "always False")
