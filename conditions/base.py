#coding: utf-8

class ConditionType(object):
    pass

# Prawdopodobnie trzeba to będzie zrobić zgodnie z podejściem adminowym

class ConditionCache(object):
    """
    Based on django.admin and brabeion.BadgeCache
    """
    def __init__(self):
        self._registry={}

    def register(self, condition):
        assert issubclass(condition, ConditionType)  # TODO: duck-type this
        self._registry.setdefault(__name__, []).append([condition.__name__,
                        condition._meta.verbose_name or condition.__name__])

    def choices(self):
        outer = []
        for key in self._registry.keys():
            inner = []
            for choice in self._registry[key]:
                inner.append(choice)
            outer.append([key, inner])
        return outer

conditions = ConditionCache()
