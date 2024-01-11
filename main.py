# python imports
import pygame
from sys import exit
from random import randint, choice

# local imports
from player import Player
from opponent import Opponent
from ball import Ball

w = 640
h = 480

# Group single
player = pygame.sprite.GroupSingle()
player.add(Player())

opponent = pygame.sprite.GroupSingle()
opponent.add(Opponent())

ball = pygame.sprite.Group()
the_ball = Ball()


def collision_sprite():
    """
    If ball collides with opponent, change direction to left.
    If ball collides with player, change direction to right.

    If opp or player is going down, ball goes down.
    If opp or player is going up, ball goes up.
    """
    vert_dir = ""
    direction = ""
    if pygame.sprite.spritecollide(opponent.sprite, ball, False):
        vert_dir = opponent.sprite.direction  # up or down
        direction = "left"
    elif pygame.sprite.spritecollide(player.sprite, ball, False):
        vert_dir = player.sprite.direction  # up or down
        direction = "right"

    return direction, vert_dir


def main():
    pygame.init()
    # CREATE DISPLAY SURFACE
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Pong")

    # Create the clock object for the framerate
    clock = pygame.time.Clock()

    # Player & opponent score
    player_score = 0
    opponent_score = 0
    test_font = pygame.font.Font("freesansbold.ttf", 50)

    # Start screen title
    game_title_surf = test_font.render("Pong", False, "Yellow")
    game_title_rect = game_title_surf.get_rect(center=(w / 2, h / 2 - 100))
    # Start screen score
    game_start_msg = test_font.render("Press Enter to start", False, "White")
    game_start_msg_rect = game_start_msg.get_rect(center=(w / 2, h / 2))
    game_cont_msg = test_font.render("Press Enter to continue", False, "White")
    game_cont_msg_rect = game_start_msg.get_rect(center=(w / 2 - 50, 330))

    game_active = False
    update_score = False

    # While loop
    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                pass
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    ball.empty()
                    game_active = True
                    update_score = True
                    the_ball = Ball()
                    ball.add(the_ball)
                    player.update(game_restart=True)

        if game_active:
            screen.fill("black")

            player.draw(screen)
            player.update()

            opponent.draw(screen)
            opponent.update()

            d, vd = collision_sprite()
            ball.draw(screen)
            ball.update(direction=d, vert_dir=vd)

            if the_ball.direction == "game over":
                # Ball is out of bounds on left or right side
                game_active = False
        else:
            # Start screen or Game over screen
            screen.fill("black")
            if update_score:
                ball_x_pos = the_ball.rect.x
                if ball_x_pos < 20:
                    # opponent won
                    opponent_score += 1
                elif ball_x_pos > w - 20:
                    # player won
                    player_score += 1
                update_score = False

            if player_score == 0 and opponent_score == 0:
                # Show start screen
                screen.blit(game_title_surf, game_title_rect)
                screen.blit(game_start_msg, game_start_msg_rect)
            else:
                # Show score screen
                your_score = f"Your score: {player_score}"
                opp_score = f"Opponent's score: {opponent_score}"
                score_msg_1 = test_font.render(
                    your_score,
                    False,
                    "White",
                )
                score_msg_2 = test_font.render(
                    opp_score,
                    False,
                    "Red",
                )
                score_msg_rect_1 = score_msg_1.get_rect(center=(w / 2, h / 2 - 100))
                score_msg_rect_2 = score_msg_1.get_rect(center=(w / 2 - 100, 230))

                screen.blit(score_msg_1, score_msg_rect_1)
                screen.blit(score_msg_2, score_msg_rect_2)
                screen.blit(game_cont_msg, game_cont_msg_rect)

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
