def test_arcadio_y_aureliano_jose_son_medios_hermanos_(self):
  self.assertEqual(son_medio_hermanos(arcadio, aureliano_jose), True)

def test_aureliano_segundo_y_remedios_no_son_medios_hermanos(self):
  self.assertEqual(son_medio_hermanos(aureliano_segundo, remedios), False)

def test_aureliano_segundo_y_aureliano_jose_no_son_medios_hermanos(self):
  self.assertEqual(son_medio_hermanos(aureliano_segundo, aureliano_jose), False)

def test_remedios_y_arcadio_no_son_medios_hermanos(self):
  self.assertEqual(son_medio_hermanos(remedios, arcadio), False)

