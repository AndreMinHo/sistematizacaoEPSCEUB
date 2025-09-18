import unittest
from src.Agenda import Agenda
from src.Usuario import Usuario
from src.Sala import Sala

class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()

    def test_criar_usuario(self):
        self.agenda.criarUsuario("placeholder")
        self.assertEqual(len(self.agenda.listaUsuario), 1)
        self.assertIsInstance(self.agenda.listaUsuario[0], Usuario)
        self.assertEqual(self.agenda.listaUsuario[0].usuarioID, "placeholder")

    def test_criar_sala(self):
        self.agenda.criarSala("sala1", "auditorio")
        self.assertEqual(len(self.agenda.listaSala), 1)
        self.assertIsInstance(self.agenda.listaSala[0], Sala)
        self.assertEqual(self.agenda.listaSala[0].salaID, "sala1")

    def test_fazer_reserva(self):
        self.agenda.criarUsuario("placeholder")
        self.agenda.criarSala("sala1", "auditorio")
        self.agenda.fazerReserva(2025, 9, 18, 14, "placeholder", "sala1")
        self.assertEqual(len(self.agenda.listaReserva), 1)
        reserva = self.agenda.listaReserva[0]
        self.assertEqual(reserva.usuarioID, "placeholder")
        self.assertEqual(reserva.salaID, "sala1")

    def test_remover_reserva(self):
        self.agenda.criarUsuario("placeholder")
        self.agenda.criarSala("sala1", "auditorio")
        self.agenda.fazerReserva(2025, 9, 18, 14, "placeholder", "sala1")
        reserva_id = self.agenda.listaReserva[0].reservaID
        self.agenda.removerReserva(reserva_id)
        self.assertEqual(len(self.agenda.listaReserva), 0)

if __name__ == "__main__":
    unittest.main()
