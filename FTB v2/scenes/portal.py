from scenes.base_scene import BaseScene

class PortalScene(BaseScene):
    def display(self):
        print("\n=== Портал ===")
        print("1. Вернуться в город")
        print("0. Выйти из игры")

    def handle_input(self, user_input):
        if user_input == "1":
            self.game.change_scene("city")
        elif user_input == "0":
            self.game.running = False
        else:
            print("Некорректный ввод.")
