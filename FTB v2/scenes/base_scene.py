class BaseScene:
    def __init__(self, game):
        """Принимает ссылку на основной объект игры"""
        self.game = game

    def display(self):
        """Метод для отображения сцены (переопределяется в наследниках)"""
        pass

    def handle_input(self, user_input):
        """Метод обработки ввода (переопределяется в наследниках)"""
        pass
