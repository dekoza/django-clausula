#coding: utf-8
from conditions.base import clauses

def resolve(obj):
    "always Fail"
    return False

clauses.register(resolve, "always False")
