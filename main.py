# python imports
import pygame
from sys import exit
from random import randint, choice

# local imports
from player import Player
from opponent import Opponent
from ball import Ball

# Group single
player = pygame.sprite.GroupSingle()
player.add(Player())

opponent = pygame.sprite.GroupSingle()
opponent.add(Opponent())

ball = pygame.sprite.Group()
the_ball = Ball()
# ball.add(Ball())
# ball.add(the_ball)


def collision_sprite():
    """
    If ball collides with opponent, change direction to left.
    If ball collides with player, change direction to right.
    """
    direction = ""
    if pygame.sprite.spritecollide(opponent.sprite, ball, False):
        # print("I hit opponent!")
        direction = "left"
    elif pygame.sprite.spritecollide(player.sprite, ball, False):
        # print("I hit the player!")
        direction = "right"

    return direction


def main():
    pygame.init()
    # CREATE DISPLAY SURFACE
    w = 640
    h = 480
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Pong")

    # Create the clock object for the framerate
    clock = pygame.time.Clock()

    # Timer for enemy
    # opponent_timer = pygame.USEREVENT + 1
    # pygame.time.set_timer(opponent_timer, 3000)

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

            d = collision_sprite()
            ball.draw(screen)
            ball.update(direction=d)

            if the_ball.direction == "game over":
                # print("Someone lost...")
                game_active = False
        else:
            screen.fill("black")

            # Someone may have lost...
            if update_score:
                ball_x_pos = the_ball.rect.x
                if ball_x_pos < 20:
                    # player lost
                    opponent_score += 1
                elif ball_x_pos > w - 20:
                    player_score += 1
                update_score = False

            if player_score == 0 and opponent_score == 0:
                screen.blit(game_title_surf, game_title_rect)
                screen.blit(game_start_msg, game_start_msg_rect)
            else:
                # Show instructions if score is 0, otherwise show the score
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
