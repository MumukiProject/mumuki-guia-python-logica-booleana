it("un filosofo griego que camina 5kms al día es un peripatético", function() {
  assert.equal((esPeripatetico("filosofo", "griego", 5) || esPeripatetico("filósofo", "griego", 5)), true);
})

it("un filosofo griego que camina 2kms al día no es un peripatético", function() {
  assert.equal((esPeripatetico("filosofo", "griego", 2) || esPeripatetico("filósofo", "griego", 2)), false);
})

it("un filosofo argentino que camina 5kms al día no es un peripatético", function() {
  assert.equal(esPeripatetico("filosofo", "argentino", 5), false);
})

it("un atleta griego que camina 10kms al día no es un peripatético", function() {
  assert.equal(esPeripatetico("atleta", "griego", 10), false);
})

it("un profesor colombiano que camina 1km al día no es un peripatético", function() {
  assert.equal(esPeripatetico("profesor", "colombiano", 1), false);
})