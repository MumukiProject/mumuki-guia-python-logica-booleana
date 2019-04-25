  
  def test_un_filosofo_griego_que_camina_5kms_al_día_es_un_peripatético(self):
    self.assertTrue((es_peripatetico("filosofo", "griego", 5) or es_peripatetico("filósofo", "griego", 5)))
  
  
  def test_un_filosofo_griego_que_camina_2kms_al_día_no_es_un_peripatético(self):
    self.assertFalse((es_peripatetico("filosofo", "griego", 2) or es_peripatetico("filósofo", "griego", 2)))
  
  
  def test_un_filosofo_argentino_que_camina_5kms_al_día_no_es_un_peripatético(self):
    self.assertFalse(es_peripatetico("filosofo", "argentino", 5))
  
  
  def test_un_atleta_griego_que_camina_10kms_al_día_no_es_un_peripatético(self):
    self.assertFalse(es_peripatetico("atleta", "griego", 10))
  
  
  def test_un_profesor_colombiano_que_camina_1km_al_día_no_es_un_peripatético(self):
    self.assertFalse(es_peripatetico("profesor", "colombiano", 1))
  
