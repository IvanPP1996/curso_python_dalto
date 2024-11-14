ingreso_mensual = 90000
gasto_mensual = 88000

if ingreso_mensual >= 10000:
    if ingreso_mensual -gasto_mensual > 7000:
        print("Ahora estas bien")
    else:
        print("Estas gastando mucho dinero")
elif ingreso_mensual >= 1000:
    print("Estas bien en latinoamerica")
else:
    print("No tienes buenos ingresos")