it("una persona que mide 1.5m, no está acompañada por un adulto y no tiene afecciones cardíacas puede subirse a la atracción", function() {
  assert.equal(puedeSubirse(1.5, false, false), true);
})

it("una persona que mide 1.7m, no está acompañada por un adulto y tiene afecciones cardíacas no puede subirse a la atracción", function() {
  assert.equal(puedeSubirse(1.7, false, true), false);
})

it("una persona que mide 1.2m, está acompañada por un adulto y no tiene afecciones cardíacas puede subirse a la atracción", function() {
  assert.equal(puedeSubirse(1.2, true, false), true);
})

it("una persona que mide 1.2m, no está acompañada por un adulto y no tiene afecciones cardíacas no puede subirse a la atracción", function() {
  assert.equal(puedeSubirse(1.2, false, false), false);
})

it("una persona que mide 1.1m, está acompañada por un adulto y no tiene afecciones cardíacas no puede subirse a la atracción", function() {
  assert.equal(puedeSubirse(1.1, true, false), false);
})