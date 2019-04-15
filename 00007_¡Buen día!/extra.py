const mariaDeLosRemedios = {
  nombre: "María De Los Remedios"
};

const pedroTernera = {
  nombre: "Pedro Ternera"
};

const sofiaMontiel = {
  nombre: "Sofía Montiel"
};

const arturoDeLaPiedad = {
  nombre: "Arturo De La Piedad"
};

const pilarTernera = {
  nombre: "Pilar Ternera",
  madre: mariaDeLosRemedios,
  padre: pedroTernera
};

const ursulaIguaran = {
  nombre: "Úrsula Iguarán"
};

const joseArcadioPadre = {
  nombre: "José Arcadio"
};

const joseArcadio = {
  nombre: "José Arcadio",
  madre: ursulaIguaran,
  padre: joseArcadioPadre
};

const coronelAureliano = {
  nombre: "Coronel Aureliano",
  madre: ursulaIguaran,
  padre: joseArcadioPadre
};

const sofiaDeLaPiedad = {
  nombre: "Sofía De La Piedad",
  madre: sofiaMontiel,
  padre: arturoDeLaPiedad
};

const arcadio = {
  nombre: "Arcadio",
  madre: pilarTernera,
  padre: joseArcadio
};

const aurelianoJose = {
  nombre: "Arcadio",
  madre: pilarTernera,
  padre: coronelAureliano
};

const aurelianoSegundo = {
  nombre: "Aureliano Segundo",
  madre: sofiaDeLaPiedad,
  padre: arcadio
};

const remedios = {
  nombre: "Remedios",
  madre: sofiaDeLaPiedad,
  padre: arcadio
};

function madreDe(persona) {
  return persona.madre.nombre;
};

function padreDe(persona) {
  return persona.padre.nombre;
};