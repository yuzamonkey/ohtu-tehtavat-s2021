class All:  # (tosi kaikille pelaajille)
    def matches(self, player):
        return True


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True

        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class Not:  # (parameetrina olevan ehdon negaatio)
    def __init__(self, cond):
        self._cond = cond

    def matches(self, player):
        return not self._cond.matches(player)


class HasFewerThan:  # (HasAtLeast-komennon negaatio eli, esim. on vähemmän kuin 10 maalia)
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
