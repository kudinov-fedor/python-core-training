import Game_Session as game

a = 10
b = 10
c = 10
cor = game.GameSession(a, b, c)

assert len(cor.mines) == c