def Ej7(): 
    ##usar modulos
    ## manejo de errores
    ## clases -> pacientes ,doctores(especialidades),agenda
    from datetime import datetime
    from Ejercicio7_1203.users import Pacientes,Doctores

    mensaje="""
        1)Registrar paciente
        2)Registrar doctores
        3)Ver horarios
        """

    print(mensaje)
    opcion=int(input("Ingrese la opción que desa realizar: "))
    if opcion==1:
        pass
    if opcion==2:
        id=0
        listaDoctores=[]
        while True:
            id=id+1
            NameDr=input("Ingrese el nombre del doctor: ")
            EspecialidadDr=input("Ingrese su especialidad: ")
            print("Ahora detalle el turno diario")
            AñoDr=int(input(("Año: ")))
            MesDr=int(input(("Mes: ")))
            DíaDr=int(input(("Día: ")))
            Hora_IDr=int(input(("Ingrese la hora de inicio: ")))
            Hora_FDr=int(input(("Ingrese la hora fin: ")))
            Turno_InicioDr=datetime(AñoDr,MesDr,DíaDr,Hora_IDr)
            Turno_FinDr=datetime(AñoDr,MesDr,DíaDr,Hora_FDr)
            try:
                T_InicioDr=datetime.strftime(Turno_InicioDr, '%d/%m %H:%M')
                T_FinDr=datetime.strftime(Turno_FinDr, '%d/%m %H:%M')
                print(f"El turno empieza el {T_InicioDr} y termina {T_FinDr}")
            except Exception as E:
                print(E)
