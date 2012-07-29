#coding: utf-8

class ConditionType(object):
    # dodać mechanikę Meta
    pass

# Prawdopodobnie trzeba to będzie zrobić zgodnie z podejściem adminowym

class ConditionCache(object):
    """
    Based on django.admin and brabeion.BadgeCache
    """
    def __init__(self):
        self._registry={}

    def register(self, condition):
#        assert issubclass(condition, ConditionType)  # TODO: duck-type this
        self._registry.setdefault(condition.__module__, []).append(
                                 [condition.__module__ + condition.__name__,
                                 getattr(condition, 'verbose_name', condition.__name__)]
        )

    def choices(self):
        outer = []
        for key in self._registry.keys():
            inner = []
            for choice in self._registry[key]:
                inner.append(choice)
            outer.append([key, inner])
        return outer


clauses = ConditionCache()


def autodiscover():
    """
    Stolen from django.admin
    """

    import copy
    from django.conf import settings
    from django.utils.importlib import import_module
    from django.utils.module_loading import module_has_submodule

    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        # Attempt to import the app's admin module.
        before_import_registry = copy.copy(clauses._registry)
        try:
            import_module('%s.conditions' % app)
        except:
            # Reset the model registry to the state before the last import as
            # this import will have to reoccur on the next request and this
            # could raise NotRegistered and AlreadyRegistered exceptions
            # (see #8245).
            clauses._registry = before_import_registry

            # Decide whether to bubble up this error. If the app just
            # doesn't have an admin module, we can ignore the error
            # attempting to import it, otherwise we want it to bubble up.
            if module_has_submodule(mod, 'conditions'):
                raise
