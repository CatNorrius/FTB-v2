from core.data_loader import load_csv
from scenes.base_scene import BaseScene
from rich.console import Console
from rich.table import Table

console = Console()

class CityScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.buildings = load_csv("buildings.csv")

    def display(self):
        console.print("\n[bold cyan]=== Город ===[/bold cyan]")

        table = Table(title="Здания в городе")
        table.add_column("ID", style="cyan")
        table.add_column("Название", style="magenta")
        table.add_column("Функция", style="green")

        for building in self.buildings:
            table.add_row(building["id"], building["name"], building["function"])

        console.print(table)
        console.print("[bold yellow]Выберите здание (или 0 для выхода):[/bold yellow]")

    def handle_input(self, user_input):
        if user_input == "0":
            self.game.running = False
        elif user_input == "1":
            self.game.change_scene("tavern")
        elif user_input == "3":
            self.game.change_scene("portal")
        else:
            console.print("[bold red]Некорректный ввод.[/bold red]")
