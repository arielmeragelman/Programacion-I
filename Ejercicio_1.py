

#if __name__ == ""__main__"":
def inicio():
    def fun_decora_1(f):
        def wrapper(*args, **kwargs):
            
            f(*args, **kwargs)    
            print("ESTE SALUDO SE EJECUTA CON UN DECORADOR LUEGO DE SALUDAR A TODAS LAS AULAS")
        return wrapper


    @fun_decora_1
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


inicio()