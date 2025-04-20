from os import system, name
from time import sleep
from tabulate import tabulate

from .modules.requests import search_problems, search_price, show_cars_more_problems
from .utils.validations import validate_string_input, validate_exit


class App:
    """
    Main class for the Automotive Center application.
    """

    def __init__(self) -> None:
        """
        Initializes the App class.
        """
        self.url = "http://127.0.0.1:5000"

    def view_banner(self) -> None:
        """
        Displays the banner of the application.
        """
        print("---------------------------------------")
        print("------- Centro Automotivo Porto -------")
        print("---------------------------------------")

    def view_menu(self) -> None:
        """
        Displays the main menu of the application.
        """
        self.view_banner()
        print("1 - Buscar problemas comums")
        print("2 - Buscar orçamento")
        print("3 - Mostrar carros que costumam dar mais problemas")
        print("4 - Sair")

    def clear(self) -> None:
        """
        Clears the console screen.
        """
        system("cls" if name == "nt" else "clear")

    def run(self) -> None:
        """
        Main loop of the application. It displays the menu and handles user input.
        """
        while True:
            self.clear()
            try:
                self.view_menu()
                choice = int(input("Informe a opção desejada: "))
                valid = False
                match choice:
                    case 1:
                        try:
                            while not valid:
                                self.clear()
                                brend = (
                                    input(
                                        "Informe a marca de carro cujo deseja buscar problemas comums: "
                                    )
                                    .title()
                                    .strip()
                                )
                                valid = validate_string_input(brend)
                                if not valid:
                                    input("APERTE ENTER PARA CONTINUAR")
                            self.clear()
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            problem = search_problems(self.url, brend)
                            if problem:
                                print("Problema identificado!")
                                print(f"Marca: {brend}")
                                print(f"Problema: {problem}")
                        except ValueError as e:
                            print(f"Erro de valor: {e}")
                        except Exception as e:
                            print(f"Erro inesperado: {e}")
                    case 2:
                        try:
                            while not valid:
                                self.clear()
                                brend = (
                                    input("Informe a marca para verificar orçamento: ")
                                    .title()
                                    .strip()
                                )
                                valid = validate_string_input(validate_exit)
                                input("APERTE ENTER PARA CONTINUAR!")
                            self.clear()
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            dados = search_price(self.url, brend)
                            tabela = tabulate(
                                dados, headers="firstrow", tablefmt="grid"
                            )
                            print(tabela)
                        except Exception as e:
                            print(f"Erro inesperado: {e}")
                    case 3:
                        try:
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            dados = show_cars_more_problems(self.url)
                            tabela = tabulate(
                                dados, headers="firstrow", tablefmt="grid"
                            )
                            print(tabela)
                        except ValueError as e:
                            print(f"Erro de valor: {e}")
                        except Exception as e:
                            print(f"Erro inesperado: {e}")
                    case 4:
                        while not valid:
                            self.clear()
                            confirm = str(input("Deseja mesmo sair? [Sim/Nao]"))
                            valid = validate_exit(confirm)
                            input("APERTE ENTER PARA CONTINUAR")
                        self.clear()
                        print("Programa Finalizado!")
                        break
                    case _:
                        print("Opção ínvalida.")

            except ValueError as e:
                print(f"Erro de valor: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            finally:
                input("Aperte ENTER para continuar")
                self.clear()
