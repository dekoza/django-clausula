.. django-conditions documentation master file, created by
   sphinx-quickstart on Sun Jul 29 22:04:41 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-clausula's documentation!
===========================================

`Clausula` means `condition` in Latin.

The purpose of this app is to allow adding dynamic conditions to relations
between objects.


How is this useful?
-------------------

Let's say you develop an application that will present content to user based
on various conditions. Gamification comes to mind. Let's say you want to set
the conditions on a per-user or per-group basis. For example girls get happy
hours on Saturday and boys get them on Thursdays. Hardcoding that would be a
bit tricky if you tend to change your mind frequently.


Usage
-----

After installing the package and adding 'clausula' to INSTALLED_APPS
you should define some abstract conditions you'd like to use.

Do this by creating a file `conditions.py` in your app. Then you need to
import `clauses` registry, define your conditions and register them.

Each condition is simply a function that fullows these rules:

* it takes one argument: an `object` (a :class:`Condition` instance)
* it returns a boolean value

The `object` is guaranteed to have a `param` attribute which holds a string
which can be used to compute returned boolean value. There can also be some
relations available as :class:`Condition` subclasses :class:`django.db.models.Model`.
Feel free to experiment and find some hackish uses for this package.

Full example
------------

`conditions.py`::

    from clausula import clauses

    def day_of_week_clause(obj):
        import datetime
        weekday = datetime.date.today().weekday()
        if weekday == int(obj.param):
            return True
        return False

    clauses.register(day_of_week_clause, "checks day of week")

Then you should run ``manage.py runserver``, go to the admin page and add
a Condition. You'll see "checks day of week" in `Clause` list. Fill the name
and give a day number. Let's say we want to check if this is Sunday:

.. figure:: _static/addcondition.png
   :align:  center


TO BE CONTINUED


Contents:

.. toctree::
   :maxdepth: 2

   autodoc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

