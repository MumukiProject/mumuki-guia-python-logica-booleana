def test_si_la_cama_estaba_arriba_al_ejecutar_jugar_en_el_hospital_pasa_a_estar_abajo(self):
  jugar_en_el_hospital()
  self.assertEqual(cama_arriba, False)


def test_si_la_cama_estaba_abajo_al_ejecutar_jugar_en_el_hospital_pasa_a_estar_arriba(self):
  cama_arriba = False
  jugar_en_el_hospital()
  self.assertEqual(cama_arriba, True)


def test_si_la_cama_estaba_arriba_al_ejecutar_jugar_en_el_hospital_dos_veces_sigue_estando_arriba(self):
  jugar_en_el_hospital()
  jugar_en_el_hospital()
  self.assertEqual(cama_arriba, True)

