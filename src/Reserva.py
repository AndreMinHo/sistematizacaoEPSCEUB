from datetime import datetime

class Reserva:

    _id_counter = 1

    def __init__(self, ano, mes, dia, hora, usuarioID, salaID):
        self.reservaID = Reserva._id_counter
        Reserva._id_counter += 1
        self.data = datetime(ano, mes, dia, hora, 0, 0)
        self.usuarioID = usuarioID
        self.salaID = salaID

    def __str__(self):
        return f"ID: {self.reservaID}, Usuario: {self.usuarioID}, Sala: {self.salaID}, Data: {self.data}"