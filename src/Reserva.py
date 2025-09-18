from datetime import datetime

class Reserva:
    def __init__(self, ano, mes, dia, hora, usuarioID, salaID):
        self.data = datetime(ano, mes, dia, hora, 0, 0)
        self.usuarioID = usuarioID
        self.salaID = salaID
    