Empecemos por algo sencillo, ¿te acordás del operador `not` ? Se lo denomina negación o complemento lógico y sirve para negar un valor booleano.

Si tengo el booleano representado por `tiene_hambre`, el complemento será `not tiene_hambre`.

¿Y esto para qué sirve? :thought_balloon: Por ejemplo, para modelar casos de alternancia.

```python
lampara_prendida = True

def apretar_interruptor():
  global lampara_prendida
  lampara_prendida = not lampara_prendida
```

> Definí el procedimiento `jugar_en_el_hospital` para que los pacientes impacientes puedan divertirse subiendo y bajando su cama.
