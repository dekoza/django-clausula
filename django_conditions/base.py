#coding: utf-8

"""
.. module:: base
    :synopsis: define basic components of the package
"""

class ConditionCache(object):
    """
    This is a typical registering class.
    """
    def __init__(self):
        self._registry={}

    def register(self, condition, name=None):
        """
        This method is used to register your statement to the global
        `clauses` list registry.

        Args:
            condition: a function that will be called to resolve the condition

        Kwargs:
            name (str): a name that will be shown in the admin
        """
        self._registry.setdefault(condition.__module__, []).append(
                                 [condition.__module__ + '.' + condition.__name__,
                                  name if name else condition.__name__]
        )

    def choices(self):
        """
        This method is used to populate choices field in the admin.

        Returns:
            a nested list, so you know which clauses belong to which app
        """
        outer = []
        for key in self._registry.keys():
            inner = []
            for choice in self._registry[key]:
                inner.append(choice)
            app_name = '.'.join(key.split('.')[:-1])
            outer.append([app_name, inner])
        return outer


clauses = ConditionCache()


def autodiscover():
    """
    This is shamelessly taken from django.admin.

    This method is used to populate the global `clauses`
    object with whatever conditions devlopers put in their apps.
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
