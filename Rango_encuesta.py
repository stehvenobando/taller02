__author___="Stehven Alexander Obando Cordoba"
__license__="GPL"
__version__="1.0.0"
__email__="stehvenobando@gmail.com"
#----------------------------------------------------------------
#Aqui inicia declaracion de la clase
#---------------------------------------------------------------
class Rango_encuesta:
    __totalcasados = 0
    __totalsolteros= 0
    __numerocasados= 0
    __numerosolteros= 0
    
    __method__="darNumeroCasados" 
    __description__="Retorna el número de personas casadas que respondieron la encuesta, en el rango de edad de la clase."
    __parameter__="Ninguno."
    __return__="El número de personas casadas que respondieron la encuesta, en el rango de edad de la clase."
    def darNumeroCasados(self):
        return self.__numerocasados
    
    
    __method__="darPromedio"
    __description__="Retorna el promedio de la encuesta en el rango de edad de la clase." 
    "Para esto suma todas las opiniones y divide por el número total de encuestados."
    __parameter__="Ninguno"
    __return__="El promedio de la encuesta en el rango de edad de la clase considerando sólo los casados."  
    def darPromedio(self):
        totalEncuestados= self.__numerosolteros + self.__numerocasados
        totalOpiniones= self.__totalcasados + self.__totalsolteros
        return totalOpiniones/totalEncuestados
    
    __method__="agregarOpinionCasado "
    __description__="Opinión del encuestado. "
    __parameter__="Opinión del encuestado."
    __return__="Ninguno." 
    def agregarOpinionCasado(self,calificacion):
        self.__numerocasados  += 1
        self.__totalcasados += calificacion 
        
    __method__="darPromedioCasados"
    __description__="Retorna el promedio de la encuesta en el rango de edad de la clase."
    "Para esto suma todas las opiniones de los casados y divide por el número total de ellos."
    __parameter__="Ninguno."
    __return__="El promedio de la encuesta en el rango de edad de la clase considerando sólo los casados."  
    def darPromedioCasados(self):
         return self.__numerocasados/self.__totalcasados
    
    __method__="darTotalOpinionCasados"
    __description__="Retorna la suma de todas las opiniones de los encuestados casados en el rango de edad de la clase."
    __parameter__="Ninguno."
    __return__="La suma de todas las opiniones de los encuestados casados en el rango de edad de la clase."  
    def darTotalOpinionCasados(self):
         return self.__totalcasados
    #solteros
    __method__="agregarOpinionSoltero "
    __description__="Opinión del encuestado. "
    __parameter__="Opinión del encuestado."
    __return__="Ninguno." 
    def agregarOpinionSoltero(self,calificacion):
        self.__numerosolteros  += 1
        self.__totalsolteros += calificacion 
    
    
           
 #----------------------------------------------------------------
#Aqui inicia declaracion de metodos.
#---------------------------------------------------------------