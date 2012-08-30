Welcome to django-clausula
==========================

The purpose of this app is to allow adding dynamic conditions to relations
between objects.


How is this useful?
-------------------

Let's say you develop an application that will present content to user based
on various conditions. Gamification comes to mind. Let's say you want to set
the conditions on a per-user or per-group basis. For example girls get happy
hours on Saturday and boys get them on Thursdays. Hardcoding that would be a
bit harsh if you tend to change your mind frequently.

Requirements
------------

Django >= 1.4

Usage
-----

After installing the package and adding 'clausula' to INSTALLED_APPS
you should define some abstract conditions you'd like to use.

Do this by creating a file `conditions.py` in your app. Then you need to
import `clauses` registry, define your conditions and register them.
Example `conditions.py`::

    def day_of_week_clause(obj, *args, **kwargs):
        import datetime
        weekday = datetime.date.today().weekday()
        if weekday == int(obj.param):
            return True
        return False

    clauses.register(day_of_week_clause, "checks day of week")

Each condition is a function that fullows these rules:

* it takes one mandatory argument: an `object` (a :class:`Condition` instance)
* it silently accepts any number of optional arguments (*args, **kwargs)
* it returns a boolean value

`clauses.register` accepts two arguments: a callable and a string representation
that will be displayed in Admin.

The `object` is guaranteed to have a `param` attribute which holds a string
which can be used to compute returned boolean value. There can also be some
relations available as :class:`Condition` is a subclass of :class:`django.db.models.Model`.
Feel free to experiment and find some hackish uses for this package.
