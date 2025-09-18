from Agenda import Agenda

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def main():
    print("Bem vindo ao sistema de reservas!")
    agenda = Agenda()



    while True:
        print("\nComandos:")
        print("1: Criar usuario")
        print("2: Criar sala")
        print("3: Fazer Reserva")
        print("4: Consultar Reservas")
        print("5: Remover Reserva")
        print("6: Sair\n")


        comando = input()
        if comando == "1":
            print("Digite o ID do usuario: ")
            idUsuario = input()
            agenda.criarUsuario(idUsuario)
        if comando == "2":
            print("Digite o ID da sala: ")
            idSala = input()
            print("Digite o tipo de sala: ")
            tipo = input()
            agenda.criarSala(idSala, tipo)
        if comando == "3":
            ano = input_int("Digite o ano (número): ")
            if ano < 0 or ano > 9998:
                print("Erro: Ano invalido.")
                continue                
            mes = input_int("Digite o mês (número): ")
            if mes > 12 or mes < 0:
                print("Erro: Mês invalido.")
                continue
            dia = input_int("Digite o dia (número): ")
            if dia > 31 or dia < 0:
                print("Erro: Dia invalido.")
                continue
            hora = input_int("Digite a hora (0-23): ")
            if hora > 23 or hora < 00:
                print("Erro: Hora invalido.")
                continue            
            print("Digite o ID do usuario: ")
            idU = input()
            print("Digite o ID da sala: ")
            idS = input()
            agenda.fazerReserva(ano, mes, dia, hora, idU, idS)
        if comando == "4":
            agenda.consultarReserva()
        if comando == "5":
            rID = input_int("Digite o ID da reserva: ")
            agenda.removerReserva(rID)
        if comando == "6":
            break

if __name__ == "__main__":
    main()
