def test_un_lunes_feriado_a_las_14hs_el_banco_esta_cerrado(self):
  self.assertTrue(esta_cerrado(True, "lunes", 14))


def test_un_miércoles_feriado_a_las_20hs_el_banco_esta_cerrado(self):
  self.assertTrue(esta_cerrado(True, "miercoles", 20))


def test_un_jueves_corriente_a_las_13hs_el_banco_no_estacerrado"(self):
  self.assertTrue(not esta_cerrado(False, "jueves", 13))


def test_un_sabado_corriente_a_las_11hs_el_banco_esta_cerrado(self):
  self.assertTrue(esta_cerrado(False, "sabado", 11))


def test_un_domingo_corriente_a_las_19hs_el_banco_esta_cerrado(self):
  self.assertTrue(esta_cerrado(False, "domingo", 19))


def test_un_martes_corriente_a_las_16hs_el_banco_esta_cerrado(self):
  self.assertTrue(esta_cerrado(False, "martes", 16))

