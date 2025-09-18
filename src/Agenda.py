from Reserva import Reserva
from Usuario import Usuario
from Sala import Sala
class Agenda:
    def __init__(self):
        self.listaUsuario = []
        self.listaSala = []
        self.listaReserva = []

    def criarUsuario(self, usuarioID):
        self.listaUsuario.append(Usuario(usuarioID))

    def criarSala(self, salaID):
        self.listaSala.append(Sala(salaID))
    
    def fazerReserva(self, ano, mes, dia, hora, usuarioID, salaID):
        self.listaReserva.append(Reserva(ano, mes, dia, hora, usuarioID, salaID))
    
    def removerReserva(self, reservaID):
        self.listaReserva = [reserva for reserva in self.listaReserva if reserva.reservaID != reservaID]
    
    def consultarReserva(self):
        for reserva in self.listaReserva:
            print(reserva)
