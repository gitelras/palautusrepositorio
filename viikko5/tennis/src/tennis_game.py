class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.convert = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_late_game_score()
        else:
            return self.convert[self.m_score1] + '-' + self.convert[self.m_score2]

    def _get_late_game_score(self):
        winning_player = self._get_winning_player()
        score_difference = abs(self.m_score1 - self. m_score2)
        if score_difference == 1:
            return "Advantage " + winning_player
        else:
            return "Win for " + winning_player

    def _get_equal_score(self):
        if self.m_score1 < 3:
            return self.convert[self.m_score1] + '-All'
        return 'Deuce'

    def _get_winning_player(self):
        return self.player1_name if self.m_score1 > self.m_score2 else self.player2_name