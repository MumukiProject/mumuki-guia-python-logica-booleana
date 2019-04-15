it("una mujer de 62 años con 40 años de aportes puede jubilarse", function() {
  assert.equal(puedeJubilarse(62, 'F', 40), true);
})

it("una mujer de 63 años con 25 años de aportes no puede jubilarse", function() {
  assert.equal(puedeJubilarse(63, 'F', 25), false);
})

it("una mujer de 58 años con 35 años de aportes no puede jubilarse", function() {
  assert.equal(puedeJubilarse(58, 'F', 35), false);
})

it("una mujer de 69 años con 40 años de aportes puede jubilarse", function() {
  assert.equal(puedeJubilarse(69, 'F', 40), true);
})

it("un hombre de 66 años con 40 años de aportes puede jubilarse", function() {
  assert.equal(puedeJubilarse(66, 'M', 40), true);
})

it("un hombre de 63 años con 35 años de aportes no puede jubilarse", function() {
  assert.equal(puedeJubilarse(63, 'M', 35), false);
})

it("un hombre de 68 años con 26 años de aportes no puede jubilarse", function() {
  assert.equal(puedeJubilarse(68, 'M', 26), false);
})

it("un hombre de 58 años con 35 años de aportes no puede jubilarse", function() {
  assert.equal(puedeJubilarse(58, 'M', 35), false);
})