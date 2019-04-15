def test_la_disyunción_lógica_excluyente_entre_True_y_True_da_False(self):
  self.assertEqual(xor(True, True), False)


def test_la_disyunción_lógica_excluyente_entre_True_y_False_da_True(self):
  self.assertEqual(xor(True, False), True)


def test_la_disyunción_lógica_excluyente_entre_False_y_True_da_True(self):
  self.assertEqual(xor(False, True), True)


def test_la_disyunción_lógica_excluyente_entre_False_y_False_da_False(self):
  self.assertEqual(xor(False, False), False)

