    #----------------------------------------------------------------
    #Aqui inicia declaracion de la clase
    #---------------------------------------------------------------
from Rango_encuesta import Rango_encuesta
class Encuesta:
    rango1 = Rango_encuesta()
    rango2 = Rango_encuesta()
    rango3 = Rango_encuesta()
    #----------------------------------------------------------------
    #Aqui inicia declaracion de metodos.
    #----------------------------------------------------------------

    __method__="agregarOpinionRango1Casado " 
    __description__="Añade la opinión de una persona casada en el rango de edad 1 de la encuesta. "
    __parameter__="Opinión del encuestado."
    __return__="Ninguno"
    def agregarOpinionRango1Casado(self, calificacion):
     self.rango1.agregarOpinionCasado(calificacion)
    
    __method__="agregarOpinionRango2Soltero  " 
    __description__="Añade la opinión de una persona soltera en el rango de edad 2 de la encuesta."
    __parameter__="(1) estado civil, (2) opinión."
    __return__="Ninguno"
    def agregarOpinionRango2Soltero(self, calificacion):
     self.rango2.agregarOpinionRango2Soltero(calificacion)

    __method__="darPromedio   " 
    __description__="Retorna el promedio de la encuesta en todos los rangos de edad."
    "Para esto suma todas las opiniones y divide por el número total de encuestados."
    __parameter__="Ninguno"
    __return__="El promedio de la encuesta en todos los rangos de edad. "
    def darPromedio(self):
       rango1 = self.rango1.__totalcasados()+self.rango1.__totalsolteros()
       rango2 = self.rango2.__totalcasados()+self.rango2.__totalsolteros()
       rango3 = self.rango3.__totalcasados()+self.rango3.__totalsolteros()
       sumatotal = rango1+rango2+rango3

       rango11 = self.rango1.__numerocasados()+self.rango1.__numerosolteros()
       rango22 = self.rango2.__numerocasados()+self.rango2.__numerosolteros()
       rango33 = self.rango3.__numerocasados()+self.rango3.__numerosolteros()
       sumatotal2 = rango11+rango22+rango33
       return sumatotal/sumatotal2
    
    __method__="darPromedioCasados    " 
    __description__="Retorna el promedio de la encuesta en todos los rangos de edad."
    "Para esto suma todas las opiniones y divide por el número total de encuestados."
    __parameter__="Ninguno"
    __return__="El promedio de la encuesta en todos los rangos de edad de la clase, considerando sólo los casados."
    def darPromedioCasados(self):
      rango1_0= self.rango1.__totalcasados()+self.rango2.__totalcasados()+self.rango3.__totalcasados()
      rango2_0= self.rango1.__numerocasados()+self.rango2.__numerocasados()+self.rango3.__numerocasados()
      return  rango1_0/rango2_0