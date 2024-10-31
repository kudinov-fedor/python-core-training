from logging import getLogger
import logging


class Player:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, player: 'Player'):
        player.lose_health(self.attack)

    def lose_health(self, damage: int):
        self.health = max(0, self.health - damage)


class Warrior(Player):
    pass


class Knight(Player):
    attack = 7


def fight(player1: Player, player2: Player) -> bool:
    round = 1
    logger = getLogger(Player.__name__)
    logger.info((f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}'))

    while player1.is_alive:
        player1.hit(player2)
        round += 1

        logger.info((f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}'))

        if not player2.is_alive:
            break

        player2.hit(player1)
        round += 1
        logger.info((f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}'))

    return player1.is_alive


logging.basicConfig(filename='warrior.log', encoding='utf-8', level=logging.INFO)

if __name__ == '__main__':
    player1 = Warrior()
    player2 = Knight()

    fight(player1, player2)
