from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All


class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasAtLeast(self, val, attr):
        return QueryBuilder(And(self._query, HasAtLeast(val, attr)))

    def hasFewerThan(self, val, attr):
        return QueryBuilder(And(self._query, HasFewerThan(val, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._query
