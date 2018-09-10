import pygame
import sys
from objects import *
from levels import *


class Game(object):
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pictures = Images()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.font2 = pygame.font.SysFont("Verdana", 50)
        self.font3 = pygame.font.SysFont("Verdana", 100)
        self.next_level = self.font.render("Congratulations, you reached the next level", False, (255, 255, 255))
        pygame.event.set_grab(1)
        pygame.mouse.set_visible(False)

        self.sounds = Sounds()

        self.pallet = Pallet(self.width/2, self.height-30)
        self.walls_list = pygame.sprite.Group()
        self.ball = Ball(self.width / 2 - 15, 500)

        self.a = 1
        self.b = 0

        self.level = 1
        self.lives = 10
        self.score = 0
        self.hit = 0
        self.big = False
        self.gun = False

        self.over = False
        self.win = False

        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.pallet)
        self.all_sprite_list.add(self.ball)
        self.block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        level_one(self.block_list, self.all_sprite_list, self.width)
        # level_five(self.block_list, self.all_sprite_list, self.walls_list)

        self.do = False
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.do is True:
                        self.do = False
                    elif self.do is False:
                        self.do = True
                if event.type == pygame.MOUSEMOTION:
                    self.mousePosition = event.pos[0]
                    self.pallet.rect.x = self.mousePosition - self.pallet.width/2
                if event.type == pygame.MOUSEBUTTONDOWN and self.gun is True and self.do is True:
                    bullet = Bullet((self.pallet.rect.x + self.pallet.rect.right)/2-5)
                    self.all_sprite_list.add(bullet)
                    self.bullet_list.add(bullet)
                    self.sounds.shoot_sound.play()

            if self.do is True:
                self.tick()
            if self.over is True:
                self.game_over()

            self.draw()
            pygame.display.flip()

            # clock.tick(300)

    def draw(self):
        self.screen.blit(self.pictures.background, (0, 0))
        score_text = self.font.render("Level : %i, Lives : %i, Score: %i" % (self.level, self.lives, self.score), False, (255, 255, 255))
        break_text = self.font2.render("Press space to continue", False, (255, 255, 255))
        go_text = self.font3.render("Game over !!!", False, (255, 0, 0))
        finish_text = self.font2.render("Your score: %i" % self.score, False, (255, 255, 255))
        win_text = self.font3.render("Congratulations !!!", False, (255, 128, 0))
        win2_text = self.font2.render("You've completed all of the levels!", False, (255, 255, 255))

        if self.do is False and self.over is False and self.win is False:
            self.screen.blit(break_text, (350, 500))

        if self.over is True:
            self.screen.blit(go_text, (300, 250))
            self.screen.blit(finish_text, (450, 400))

        if self.win is True:
            self.screen.blit(win_text, (150, 250))
            self.screen.blit(win2_text, (180, 400))

        self.all_sprite_list.draw(self.screen)
        self.screen.blit(score_text, (16, 16))

    def tick(self):
        # Kolizja piłki z blokami
        i = 1
        blocks_hit_list = pygame.sprite.spritecollide(self.ball, self.block_list, True)
        for block in blocks_hit_list:
            self.score += 10
            self.hit += 1
            self.sounds.explosion_sound.play()
            if i < 2:
                list = self.ball.bounce(block, self.a, self.b)
                self.a *= list[0]
                self.b *= list[1]
            i += 1

        # Kolizja piłki z paletką
        if pygame.sprite.collide_rect(self.ball, self.pallet):
            list = self.ball.pallet_bat(self.pallet, self.a, self.b)
            self.sounds.bloop_sound.play()
            self.a, self.b = list[0], list[1]
            self.hit = 0

        # Kolizja piłki z krawędziami
        if self.ball.rect.x <= -8 or self.ball.rect.right >= self.width+8:
            self.b = - self.b
            self.sounds.boop_sound.play()
        elif self.ball.rect.y <= -5:
            self.a = - self.a
            self.sounds.boop_sound.play()
        elif self.ball.rect.y >= self.height-10:
            self.ball.reset(self.width / 2 - 15, 500)
            self.draw()
            pygame.display.flip()
            pygame.time.wait(2000)
            self.lives -= 1
            self.a = 1
            self.b = 0

        # Kolizja piłki ze ścianą
        collided_walls = pygame.sprite.spritecollide(self.ball, self.walls_list, False)
        for wall in collided_walls:
            list = self.ball.bounce(wall, self.a, self.b)
            self.a *= list[0]
            self.b *= list[1]
            self.sounds.boop_sound.play()

        # Kolizja pocisku z scianami
        if pygame.sprite.groupcollide(self.walls_list, self.bullet_list, False, True):
            self.sounds.explosion_sound.play()

        # Kolizja pociku z blokami
        if pygame.sprite.groupcollide(self.bullet_list, self. block_list, False, False):
            self.sounds.explosion_sound.play()
        shot = pygame.sprite.groupcollide(self.bullet_list, self. block_list, True, True)
        for block in shot:
            self.score += 10

        # Poziomy
        if self.score == 180:
            self.level_call(2)
        elif self.score == 600:
            self.level_call(3)
        elif self.score == 1060:
            self.level_call(4)
        elif self.score == 1560:
            self.level_call(5)
        if self.score == 1960:
            self.game_win()
        if self.lives < 1:
            self.game_over()

        self.ball.rect.y += 5*self.a
        self.ball.rect.x += 5*self.b

        for bullet in self.bullet_list:
            bullet.move()

        if self.hit == 4 and self.big is False:
            self.pallet.get_bigger(self.pallet.rect.x, self.pallet.rect.y)
            self.hit = 0
            self.big = True

        if self.hit == 5 and self.gun is False:
            self.pallet.get_gun(self.pallet.rect.x, self.pallet.rect.y)
            self.hit = 0
            self.gun = True

    def level_call(self, level):
        self.level += 1
        self.score += 100
        self.a = 1
        self.b = 0
        self.draw()
        pygame.display.flip()
        self.screen.blit(self.next_level, (400, 400))
        pygame.display.update()
        pygame.time.wait(2000)
        self.ball.reset(self.width / 2 - 15, 500)
        self.pallet.reset(self.pallet.rect.x, self.pallet.rect.y)

        if level == 2:
            level_two(self.block_list, self.all_sprite_list, self.width)
        elif level == 3:
            level_tree(self.block_list, self.all_sprite_list, self.walls_list, self.width)
        elif level == 4:
            level_four(self.block_list, self.all_sprite_list, self.walls_list, self.width)
        elif level == 5:
            level_five(self.block_list, self.all_sprite_list, self.walls_list)

    def game_over(self):
        self.do = False
        self.over = True
        self.all_sprite_list.empty()

    def game_win(self):
        self.do = False
        self.win = True
        self.all_sprite_list.empty()
        self.sounds.win_sound.play()


if __name__ == "__main__":
    game = Game()
