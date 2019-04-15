it("si la cama estaba arriba, al ejecutar jugarEnElHospital pasa a estar abajo", function() {
  jugarEnElHospital();
  assert.equal(camaArriba, false);
})

it("si la cama estaba abajo, al ejecutar jugarEnElHospital pasa a estar arriba", function() {
  camaArriba = false;
  jugarEnElHospital();
  assert.equal(camaArriba, true);
})

it("si la cama estaba arriba, al ejecutar jugarEnElHospital dos veces sigue estando arriba", function() {
  jugarEnElHospital();
  jugarEnElHospital();
  assert.equal(camaArriba, true);
})