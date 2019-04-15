Empecemos por algo sencillo, ¿te acordás del operador `!` ? Se lo denomina negación, not o complemento lógico y sirve para negar un valor booleano.

Si tengo el booleano representado por `tieneHambre`, el complemento será `!tieneHambre`.

¿Y esto para qué sirve? :thought_balloon: Por ejemplo, para modelar casos de alternancia.

```python
let lamparaPrendida = true;

function apretarInterruptor() {
  lamparaPrendida = !lamparaPrendida;
}
```

> Definí el procedimiento `jugarEnElHospital` para que los pacientes impacientes puedan divertirse subiendo y bajando su cama.
