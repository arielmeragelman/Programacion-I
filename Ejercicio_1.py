

if __name__ == ""__main__"":
        
    def saludo_aula(aulas):
        for aula in aulas:
            print("Hola Aula "+str(aula))


    def ingreso_aulas():
        aula = []
        seguir= "1"
        while seguir == "1":
            entrada=str(input("INGRESE NUMERO DE AULA, 0 PARA SALIR:"))
            if entrada != "0":
                aula.append(entrada)
            else:
                seguir = "0"
        return aula


    aula=ingreso_aulas()
    saludo_aula(aula)