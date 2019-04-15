def cuotas(tarjeta:
  switch(tarjeta:
    case "visa":
      return 6
    case "mastercard":
      return 2
    default:
      return 1



def paga_con_tarjeta(seCobraInteres, tarjeta, efectivoDisponible:
  return !seCobraInteres and cuotas(tarjeta) >= 3 or efectivoDisponible < 100

