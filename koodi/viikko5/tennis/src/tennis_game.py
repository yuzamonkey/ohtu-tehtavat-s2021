class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.p1_score += 1
        elif player_name == self.player2:
            self.p2_score += 1
        else:
            raise Exception(f"No player {player_name} in game")

    def is_even_score(self):
        return self.p1_score == self.p2_score

    def get_even_score_text(self):
        if self.p1_score == 0:
            return "Love-All"
        elif self.p1_score == 1:
            return "Fifteen-All"
        elif self.p1_score == 2:
            return "Thirty-All"
        elif self.p1_score == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def is_set_ball(self):
        return self.p1_score >= 4 or self.p2_score >= 4

    def get_set_ball_text(self):
        difference = self.p1_score - self. p2_score
        if difference == 1:
            return f"Advantage {self.player1}"
        elif difference >= 2:
            return f"Win for {self.player1}"
        elif difference == -1:
            return f"Advantage {self.player2}"
        else:
            return f"Win for {self.player2}"

    def get_score_text(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def get_score(self):
        if self.is_even_score():
            return self.get_even_score_text()
        elif self.is_set_ball():
            return self.get_set_ball_text()
        else:
            return f"{self.get_score_text(self.p1_score)}-{self.get_score_text(self.p2_score)}"
