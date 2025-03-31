from scenes.city import CityScene
from scenes.tavern import TavernScene
from scenes.portal import PortalScene

class Game:
    def __init__(self):
        self.running = True
        self.scenes = {
            "city": CityScene(self),
            "tavern": TavernScene(self),
            "portal": PortalScene(self),
        }
        self.current_scene = self.scenes["city"]  # Начинаем в городе

    def change_scene(self, scene_name):
        """Меняет текущую сцену"""
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def run(self):
        """Запускает игровой цикл"""
        while self.running:
            self.current_scene.display()
            user_input = input("> ")
            self.current_scene.handle_input(user_input)

if __name__ == "__main__":
    game = Game()
    game.run()
