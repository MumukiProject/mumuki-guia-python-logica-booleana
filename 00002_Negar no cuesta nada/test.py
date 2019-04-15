it("alguien de 20 años es mayor de edad", function() {
  assert.equal(esMayorDeEdad(20), true);
})

it("alguien de 18 años es mayor de edad", function() {
  assert.equal(esMayorDeEdad(18), true);
})

it("alguien de 17 años no es mayor de edad", function() {
  assert.equal(esMayorDeEdad(17), false);
})

it("alguien de 16 años no es mayor de edad", function() {
  assert.equal(esMayorDeEdad(16), false);
})

it("alguien de 20 años no es menor de edad", function() {
  assert.equal(esMenorDeEdad(20), false);
})

it("alguien de 18 años no es menor de edad", function() {
  assert.equal(esMenorDeEdad(18), false);
})

it("alguien de 17 años es menor de edad", function() {
  assert.equal(esMenorDeEdad(17), true);
})

it("alguien de 16 años es menor de edad", function() {
  assert.equal(esMenorDeEdad(16), true);
})