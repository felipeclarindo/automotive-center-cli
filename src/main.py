from modules.requests import *
from utils.validations import *
from os import system, name
from time import sleep
from tabulate import tabulate

class Main:
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:5000"

    def viewMenu(self) -> None:
        print("Centro Automotivo Porto")
        print("1 - Buscar problemas comums")
        print("2 - Buscar orçamento")
        print("3 - Mostrar carros que costumam dar mais problemas")
        print("4 - Sair")

    def clear(self) -> None:
        system('cls' if name == 'nt' else 'clear')

    def executar(self) -> None:
        while True:
            self.clear()
            try:
                self.viewMenu()
                choice = int(input("Informe a opção desejada: "))
                valid = False
                match choice:
                    case 1:
                        try:
                            while not valid:
                                self.clear()
                                brend = input("Informe a marca de carro cujo deseja buscar problemas comums: ").title().strip()
                                valid = validateStringInput(brend)
                                if not valid:
                                    input("APERTE ENTER PARA CONTINUAR")
                            self.clear()
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            problem = searchProblems(self.url, brend)
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
                                brend = input("Informe a marca para verificar orçamento: ").title().strip()
                                valid = validateStringInput(brend)
                                input("APERTE ENTER PARA CONTINUAR!")
                            self.clear()
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            dados = searchPrice(self.url, brend)
                            tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
                            print(tabela)
                        except Exception as e:
                            print(f"Erro inesperado: {e}")
                    case 3:
                        try:
                            print("Buscando...")
                            sleep(1)
                            self.clear()
                            dados = showCarsMoreProblems(self.url)
                            tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
                            print(tabela)
                        except ValueError as e:
                            print(f"Erro de valor: {e}")
                        except Exception as e: 
                            print(f"Erro inesperado: {e}")
                    case 4:
                            while not valid:
                                self.clear()
                                confirm = str(input("Deseja mesmo sair? [Sim/Nao]"))
                                valid = validateExit(confirm)
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

if __name__ == "__main__":
    main = Main()
    main.executar()