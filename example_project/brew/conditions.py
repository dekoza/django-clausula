from clausula import clauses

def day_of_week_clause(obj, *args, **kwargs):
    import datetime
    weekday = datetime.date.today().weekday()
    if weekday == int(obj.param):
        return True
    return False

clauses.register(day_of_week_clause, "checks day of week")

