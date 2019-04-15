def test_una_mujer_de_62_años_con_40_años_de_aportes_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(62, 'F', 40), True)


def test_una_mujer_de_63_años_con_25_años_de_aportes_no_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(63, 'F', 25), False)


def test_una_mujer_de_58_años_con_35_años_de_aportes_no_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(58, 'F', 35), False)


def test_una_mujer_de_69_años_con_40_años_de_aportes_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(69, 'F', 40), True)


def test_un_hombre_de_66_años_con_40_años_de_aportes_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(66, 'M', 40), True)


def test_un_hombre_de_63_años_con_35_años_de_aportes_no_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(63, 'M', 35), False)


def test_un_hombre_de_68_años_con_26_años_de_aportes_no_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(68, 'M', 26), False)


def test_un_hombre_de_58_años_con_35_años_de_aportes_no_puede_jubilarse(self):
  self.assertEqual(puede_jubilarse(58, 'M', 35), False)

