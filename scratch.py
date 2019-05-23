import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
G = -0.5
WALL_KD = 100


class Bird:
    def __init__(self):
        self.x = 200
        self.y = 750
        self.speed = 3
        self.color = arcade.color.YELLOW_ORANGE
        self.size = 20

    def draw(self):
        arcade.draw_point(self.x,self.y,self.color,self.size)

    def move(self):
        self.speed += G
        self.y += self.speed

    def jump(self):
        self.speed = 15

    def check_wall_crush(self, wall):
        check_x = wall.x < self.x < wall.x + wall.w
        check_y = wall.h < self.y < wall.h + wall.space
        return check_x and not check_y

class Wall:
    def __init__(self):
        self.x = SCREEN_WIDTH + 10
        self.w = 20
        self.h = random.randint(100, SCREEN_HEIGHT - 200)
        self.space = random.randint(100, SCREEN_HEIGHT - self.h - 50)
        self.speed = 5
        self.color = [150, 200, 200]

    def draw(self):
        arcade.draw_xywh_rectangle_filled(self.x, 0, self.w, self.h, self.color)
        arcade.draw_xywh_rectangle_filled(self.x, self.h + self.space, self.w, SCREEN_WIDTH - (self.h + self.space), self.color)

    def move(self):
        self.x -= self.speed

    def is_out(self):
        return self.x < -self.w

    # def go:


class MyGame(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.BLACK)
        self.score = 0
        self.wall_kd = WALL_KD
        self.wall_list = []
        self.state = 'run'

    def setup(self):
        self.bird = Bird()
        pass

    def on_draw (self):
        arcade.start_render()
        if self.state == 'run':
            self.bird.draw()
            for wall in self.wall_list:
                wall.draw()
        elif self.state == 'game over':
            arcade.draw_text("GAME OVER",
                             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED, 100, width=SCREEN_WIDTH,
                             align="center", anchor_x="center", anchor_y="center")

    def update(self, delta_time):
        if self.state == 'run':
            self.bird. move()
            self.wall_kd -= 1

            for wall in self.wall_list:
                if self.bird.check_wall_crush(wall):
                    self.state = 'game over'
                wall.move()
                if wall.is_out():
                    self.wall_list.remove(wall)

            if random.randint(0, 1000) < 1000 and self.wall_kd <= 0:
                self.wall_list.append(Wall())
                self.wall_kd = WALL_KD

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.bird.jump()


def main ():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == '__main__':
    main()
