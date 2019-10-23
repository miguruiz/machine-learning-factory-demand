 

**IDEA NUEVA 3:**

 

**NLP:**

 

Tratamiento de textos: una herramienta que "lea" libros y documentos enteros, saque las distintas palabras principales por frecuencia.

 

Problemas:

 

Eliminación de palabras sin aporte de contenido ("en", "de", "el", "la")

Eliminación de palabras genéricas frecuentes ("coche", "casa")

 

Buscar qué palabras específicas de unos documentos (es decir, palabras sobrerrepresentadas en unos documentos frente a lo normal) marcan el carácter de un documento

 

Fuente: Guttenberg project (pendiente de comprobar si existiese una fuente similar en español)

 

Yo tengo un archivo con 12gb de libros.

 

Aplicaciones:

 

- Un superfiltro: crear una herramienta que no sólo te lleve palabra a palabra a donde quieras en un documento, sino que, introduciendo una palabra o una lista, extraiga los      distintos párrafos

donde se encuentran y te los presente.



No sólo eso, sino que con el superfiltro se pueden extraer las palabras más sobrerrepresentadas y comprobar cuál es el carácter y el tema del documento.



- Un juego: una vez leídos miles de libros, se puede plantear un juego en el que al usuario se le vayan presentando las palabras más frecuentes y tenga que adivinar la      obra, ganando más puntos cuanto antes la acierte y quedando eliminado      cuando se equivoque.

 

 

Temas tratados:

 

Webscrapping

Herramientas NLP

 

Adicionalmente podríamos subirlo a la nube (¿de Google o de Amazon?) y comparar las herramientas NLP de Python con las de Google

 

 

**IDEA NUEVA 4:**

 

Estudio de los precios de compra frente a alquiler en España. 

 

Problema inicial:

 

https://www-eleconomista-es.cdn.ampproject.org/c/s/www.eleconomista.es/vivienda/amp/10105933/Fomento-desmonta-los-precios-del-alquiler-que-ofrecen-idealista-y-Fotocasa-son-hasta-un-56-mas-caros-respecto-a-la-renta-final

 

https://www.eleconomista.es/vivienda/noticias/10023424/08/19/El-Banco-de-Espana-explica-el-calenton-de-precios-en-el-alquiler-de-Madrid-y-Barcelona-efecto-Airbnb-con-entrada-en-tromba-de-inversores.html?_gl=1*ydsf4n*_ga*WjVrN19MMFcydThFaG53ZmpoeFp5a1FXZEh5U3B4VmJJSkx4djlCTDZYQi1CNVVSQTRzcnNsZGd1bVNFY0RjZg

 

Responder a la pregunta: ¿qué es más rentable, comprar o alquilar?

 

Crear un modelo que de un precio para una vivienda media (precio/m2 ó precio medio de una vivienda de 100m2), tanto de compra como para alquiler.

 

Webscrapping de Idealista y Fotocasa.

 

Problema fundamental a resolver:

 

Los precios que se presentan en estas webs son los de la oferta, no los de las transacciones reales, por lo que los estudios basados en ellos tomando directamente el precio pedido no son reales.

 

Evidentemente, además, los pisos más sobrepreciados son los que más inflan los precios de de esos supuestos estudios. Dos motivos:

 

Cuando más desvirtuado es el valor pedido sobre el medio, más poder tiene para desplazar la media hacia arriba

 

Los pisos con valores de mercado o por debajo del de mercado se venden y/o alquilan más rápidamente, por lo tanto permanecen en la web menos tiempo. Por contra, los pisos más sobrepreciados permanecen en las webs más tiempo, por lo que se puede concluir que las webs del mercado inmobiliario están llenas de pisos sobrepreciados que no se venden.

 

Corrección:

 

Trazar, tomando datos, la curva precios medios - tiempo de anuncio (adimensionalizando primero los precios)

Por otro lado, trazar la distribución nº de pisos - tiempo de anuncio y establecer cuál es el tiempo medio que permanece el anuncio de un piso en la web

 

Ello nos permite:

 

Calcular el valor de mercado para todos los pisos

Calcular el valor medio de los mercados de alquiler y compra

Responder a las preguntas iniciales: cuáles son los precios reales del alquiler en España?

Reponder: es mejor opción comprar o alquilar?

 

Temas tratados:

 

Webscrapping

Algoritmos de Data Science

Representación de datos

Tiene una base matemática y económica

 

 

**IDEA NUEVA 3:**

 

 

Arbitraje en el mundo digital:

 

https://www.webretailer.com/lean-commerce/amazon-to-ebay-arbitrage/

 

https://arbitrageinfo.com/5-best-amazon-to-ebay-arbitrage-software-2019/

 

https://www.profitscraper.com/

 

 

La base del proyecto sería sobre todo webscrapping. Todo lo que podríamos hacer es enfocarlo más bien a la detección de arbitraje, es decir: buscar diferencias de precios en un producto entre un lugar y otro, analizar al vendedor y observar si ese vendedor también vende otros productos con estrategias similares. Ahí es donde podríamos introducir Data Science.

 

 

**IDEA NUEVA 4:**

 

Análisis de perfiles de usuarios en Twitter:

 

Idea:

 

Parte 1:

 

Webscrapping de los mensajes de Twitter. Limpieza, obtención de palabras con técnicas NLP. Guardar palabras por cada tweet y por cada usuario.

 

Clasificación luego de los usuarios con métodos de clustering (no supervisado).

 

Ver con cross-validation cuál es el número óptimo de clusters, aplicar ese número de clusters, y leer las palabras clave representativas para cada uno de los clusters formados.

 

Con esto tenemos cuáles son las principales "tribus" que habitan Twitter y qué palabras los definen.

 

Parte 2:

 

A partir de las palabras que los definen, crear una identidad para cada uno de los diferentes grupos creados. Estudio de qué productos pueden ofrecerse a cada uno de estos grupos.

 

Temas tratados:

 

Webscrapping

Algoritmos de Data Science

NLP

Representación

 

 

**IDEAS SEMEJANTES CON UNA BASE PARECIDA:**

 

Se puede crear una lista con una serie de palabras inicial para filtrar tweets que nos permitan encontrar a la gente con las características que buscamos, por ejemplo:

 

Detección de gente infeliz en Twitter.

Detección de terrorismo en Twitter.

 

A partir de ahí, con técnicas de NLP podemos ir añadiendo (comparando sus tweets con los de una "masa neutra" como grupo de control, y viendo qué palabras están sobrerrepresentadas en sus tweets) palabras a nuestros diccionarios, lo que nos permitirá ir afinando más la búsqueda de nuestros sujetos.

 

Como pregunta final, podríamos intentar comprobar, contrastando con nuestro grupo de control, si los individuos de diferentes grupos (terroristas, gente infeliz, etc…) tienden a estar más conectados a otra gente como ellos, o no.

 

 

**IDEA NUEVA 5:**

 

Rey-Hombre+Mujer = Reina

 

https://kawine.github.io/blog/nlp/2019/06/21/word-analogies.html

 

Coger un conjunto suficientemente grande de textos, limpiar, aplicar NLP y representar las distintas palabras como vectores con sus atributos.

 

Comprobar entonces qué relaciones existen entre los diferentes vectores existen.
