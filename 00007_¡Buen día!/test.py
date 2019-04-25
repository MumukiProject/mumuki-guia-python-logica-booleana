  
  def test_arcadio_y_aureliano_jose_son_medios_hermanos(self):
    self.assertTrue(son_medio_hermanos(arcadio, aureliano_jose))
  
  def test_aureliano_segundo_y_remedios_no_son_medios_hermanos(self):
    self.assertFalse(son_medio_hermanos(aureliano_segundo, remedios))
  
  def test_aureliano_segundo_y_aureliano_jose_no_son_medios_hermanos(self):
    self.assertFalse(son_medio_hermanos(aureliano_segundo, aureliano_jose))
  
  def test_remedios_y_arcadio_no_son_medios_hermanos(self):
    self.assertFalse(son_medio_hermanos(remedios, arcadio))

