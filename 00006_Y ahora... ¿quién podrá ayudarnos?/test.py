def test_un_lunes_feriado_a_las_14hs_el_banco_está_cerrado(self):
  self.assertEqual(esta_cerrado(True, "lunes", 14), True)


def test_un_miércoles_feriado_a_las_20hs_el_banco_está_cerrado(self):
  self.assertEqual(esta_cerrado(True, "miercoles", 20), True)


def test_un_jueves_corriente_a_las_13hs_el_banco_no_estácerrado"(self):
  self.assertEqual(esta_cerrado(False, "jueves", 13), False)


def test_un_sábado_corriente_a_las_11hs_el_banco_está_cerrado(self):
  self.assertEqual(esta_cerrado(False, "sabado", 11), True)


def test_un_domingo_corriente_a_las_19hs_el_banco_está_cerrado(self):
  self.assertEqual(esta_cerrado(False, "domingo", 19), True)


def test_un_martes_corriente_a_las_16hs_el_banco_está_cerrado(self):
  self.assertEqual(esta_cerrado(False, "martes", 16), True)

