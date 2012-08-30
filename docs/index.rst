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

.. `Clausula` is meant to be a glue between models (which are concrete) and
    condition statements. It allows you to concretize your abstract clauses and
    save them as objects to database. Such objects can be then injected in
    relations between other objects.

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

You run a virutal pub and want to have lower prices on one day.

`conditions.py`::

    from clausula import clauses

    def day_of_week_clause(obj):
        import datetime
        weekday = datetime.date.today().weekday()
        if weekday == int(obj.param):
            return True
        return False

    clauses.register(day_of_week_clause, "checks day of week")

Now let's see our `models.py`::

    from django.db import models
    from clausula.models import Condition

    class Bewerage(models.Model):
        name = models.CharField(max_length=30)
        normal_price = models.DecimalField(max_digits=7, decimal=2)


    class Redeem(models.Model):
        value = models.DecimalField(max_digits=7, decimal=2)
        beverage = models.ForeignKey(Beverage)
        condition = models.ForeignKey(Condition)

A bit of sugar in `admin.py`::

    from django.contrib import admin
    from .models import (Bewerage, Redeem)

    class RedeemInline(admin.TabularInline):
        model = Redeem


    class BewerageAdmin(admin.ModelAdmin):
        inlines = [Redeem]


    admin.site.register(Bewerage, BewerageAdmin)

Then you should run ``./manage.py syncdb && ./manage.py runserver``, go to the admin page and add
a Condition. You'll see "checks day of week" in `Clause` list. Fill the name
and give a day number. Let's say we want to add a `Condition` that triggers on Sunday:

.. figure:: _static/addcondition.png
   :align:  center

You should also add a Beverage with redeem triggered by your "On Sunday" condition.

Now you can show the price like this::

    {% load clausula_tags %}
    {% for brew in beverages %}
        {% if brew.redeems %}
            {% for redeem in brew.redeems %}
                {% check redeem.condition as result %}
                {% if result %}
                    {{redeem.value}} (with redeem)
                {% else %}
                    {{brew.price}} (normal price)
                {% endif %}
            {% endfor %}
        {% else %}
            {{brew.price}} (normal price)
        {% endif %}
    {% endfor %}


.. TODO: Add inclusion template tag as this case may be common.

Now play with `param` and check if it works properly. Try writing another function
and swap it with the one you used in example. Does it trigger properly? Experiment.

Feedback
========

If you have any ideas how to extend functionality of this little package,
`fork it on github <https://github.com/dekoza/django-clausula>`_ and make
a pull request or simply `file a feature request <https://github.com/dekoza/django-clausula/issues>`_.



Contents:

.. toctree::
   :maxdepth: 2

   autodoc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

