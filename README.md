# Intro
Con el objetivo de afianzar los conocimientos sobre machine learning, seleccioné el dataset desde https://www.kaggle.com/harlfoxem/housesalesprediction, en donde el objetivo es predecir el precio de casas.

# Dataset
El dataset utilizado es el que se encuentra en el archivo kc_house_data.csv.

Features:
<ul>
  <li> bedrooms: Catidad de Habitaciones. </li>
  <li> bathrooms: Cantidad de baños. 
        <br />
        <b>Aclaración:</b> En el dataset podrán observar que algunos ejemplos son decimales y no enteros (Ver segundo ejemplo, donde      bathrooms = 2.25). 
        Según Wikipedia: <blockquote cite="https://en.wikipedia.org/wiki/Bathroom#Terminology_in_the_United_States">In the United States, bathrooms are generally categorized as master bathroom, containing a varied shower [2] and a tub that is adjoining to a master bedroom, a "full bathroom" (or "full bath"), containing four plumbing fixtures: bathtub/shower, or (separate shower), toilet, and sink; "half (1/2) bath" (or "powder room") containing just a toilet and sink; and "3/4 bath" containing toilet, sink, and shower...</blockquote>
  
  </li>
  <li> sqft_living: Tamaño del living en pie cuadrado. </li>
  <li> sqft_lot: Tamaño del terreno en pie cuadrado. </li>
  <li> floors: Cantidad de pisos. </li>
  <li> waterfront: si la casa tiene vista al río. 0 = No / 1 = Si. </li>
  <li> view: Puntaje entre 0 - 4 de la vista de la casa. </li>
  <li> 
      condition: Puntaje 1-5 que indica en qué condición/estado se encuentra la casa.
      <ul>
        <li>1 = Mala</li>
        <li>2 = Baja</li>
        <li>3 = Media</li>
        <li>4 = Buena</li>
        <li>5 = Muy Buena</li>
      </ul>
  </li>
  <li> 
    grade: Representa la calidad de la construcción. 
    <ul>
      <li>1 = Por debajo de los estándares mínimos de construcción.</li>
      <li>2 = Por debajo de los estándares mínimos de construcción.</li>
      <li>3 = Por debajo de los estándares mínimos de construcción.</li>
      <li>4 = Construcción vieja y de baja calidad.</li>
      <li>5 = Bajos costes de construcción y mano de obra. Diseño pequeño y sencillo.</li>
      <li>6 = Cumple con los estándares mínimos de construcción. Baja calidad de materiales.</li>
      <li>7 = Promedio calidad de construcción y diseño.</li>
      <li>8 = Por encima del promedio en construcción y diseño. Buenos materiales tanto en el interior como en el exterior.</li>
      <li>9 = Mejor diseño arquitectónico, tanto interior como exterior.</li>
      <li>10 = Por debajo de los estándares mínimos de construcción. Casas espaciosas</li>
      <li>11 = Diseño personalizado y acabado de calidad superior con complementos de madera, accesorios de baño y opciones más lujosas.</li>
      <li>12 = Diseño personalizado y excelentes constructores. Todos los materiales son de la más alta calidad y todas las comodidades están presentes.</li>
      <li>13 = Por lo general diseñado y construido a medida. Nivel de mansión. Acabado de madera, mármol, formas de entrada, etc</li>
    </ul>
  </li>
  <li> sqft_above: Espacio interior de la vivienda que está sobre el nivel del suelo en pie cuadrado. </li>
  <li> sqft_basement: Tamaño del sótano en pie cuadrado. </li>
  <li> yr_built: Año de la consutrucción de la casa. </li>
  <li> yr_renovated: Año en que se hicieron mejoras significativas en la casa. </li>
  <li> zipcode: Código Postal </li>
  <li> lat: Coordenadas - Latitud. </li>
  <li> long Coordenadas - Longitud. </li>
  <li> sqft_living15: Tamaño promedio del living de las 15 casas más cerca en pie cuadrado. </li>
  <li> sqft_lot15: Tamaño promedio del terreno de las 15 casas más cerca en pie cuadrado. </li>
  <li> price: Precio en dólares </li> 
</ul>
<b>Nota: </b> El archivo kc_house_data_orginal.csv es el dataset original, el cual contiene las columnas "id" que es un identificador único de cada registro y la columna "date" que es la fecha en la que se realizó el registro. Éstas columnas fueron quitadas ya que no aportan ningún valor al modelo.

# Proceso
<h2>Un poco de conceptos </h2>
Realicé un proceso de tres pasos para determinar el modelo. Básicamente lo que intento es determinar si el modelo sufre de <b>overfitting</b> o <b>underfitting</b> o si está bien equilibrado.


<img src="https://s15.postimg.org/bbt6a5m97/t0zit.png"></img>
<br />
Imagen extraída del curso dictado por Andrew Ng en <a href="https://www.coursera.org/learn/machine-learning">Coursera</a>

<h3>¿Cómo identificar Overfitting?</h3>
Overfitting (Sobreajuste) significa que nuestro modelo se ajusta demasiado a los datos de entrenamiento, tanto así, que pierde la capacidad de generalización y por lo tanto, no funcionará correctamente cuando el modelo se ponga a prueba con datos de test. Por lo tanto, si la performance de nuestro modelo es alta en los datos de entrenamiento y la performance es baja en los datos de test, entonces estamos en presencia de overfitting.

<h3>¿Cómo identificar Underfitting?</h3>
Underfitting quiere decir que el modelo elegido no se ajusta suficientemente bien a los datos. Dicho de otra manera, el modelo planteado es demasiado simple. Por ejemplo, un modelo lineal, como una recta, pero los datos se comportan de manera logarítmica. Por lo tanto, si la performance de nuestro modelo es baja en los datos de entrenamiento y la performance es baja en los datos de test, entonces estamos en presencia de underfitting

<h2>1-linear_regression.py </h2>
Siempre es recomendable comenzar por lo más sencillo y si no da resultado, ir aumentando la complejidad, es por ésto que comencé con el  script "1-linear_regression.py", en el cual hice una primera prueba para determinar que tan bien se ajusta el dataset a un modelo lineal. Ésto nos dará una pauta de cuales son los pasos a seguir.
Como resultado obtenemos:
<pre>
python 1-linear_regression.py
</pre>
<pre>
0.699828185572 0.00254130401921
0.697014788003 0.0205903110921
</pre>

Dado que la performance de las predicciones sobre los mismos datos que se utilizaron para el entrenamiento (0.699828185572) es casi igual a la performance de las predicciones de datos nuevos para el modelo (datos que no se utilizaron para el entrenamiento) (0.697014788003) y es un valor relativamente bajo, podemos suponer que el modelo aún no se ajusta lo suficientemente bien a nuestros datos, por lo que estamos en un escenario de <b>underfitting</b>.

<h2>2-polynomical_d2.py </h2>
Una manera de de probar si podemos mejorar la performance, es probar con un modelo polinómico de mayor grado, es decir, en éste caso, elevando todas nuestras variables al cuadrado.
<pre>
  python 2-polynomical_d2.py 
</pre>
<pre>
  0.830028882046 0.00291291406115
  0.812813894177 0.0244860601912
</pre>
Podemos ver que la performance aumentó significativamente, tanto en para los datos de entrenamiento como los de test, por lo que, en principo, es una buena idea adoptar éste modelo polinómico.

<h2>3-polynomical_d3.py</h2>
Para ver si podemos mejorar aún más al performance, aumentaremos un grado más aún, es decir que elevaremos al cubo cada variable.
<pre>
  python 3-polynomical_d3.py 
</pre>
<pre>
  0.902972786233 0.00198889028091
  -46748368.4718 88719438.1422
</pre>
Se puede observar que la performance del modelo sobre los datos de entrenamiento ha sido aún mejor (0.902972786233) con respecto al paso anterior, pero definitivamente ha sido muy mala la performance sobre los datos nuevos para el modelo (-46748368.4718). Éste es el caso en donde nos encontramos en un escenario de <b>overfitting</b>.

# Conclusión
Pasamos un modelo con underfitting, lo mejoramos cambiandolo por un modelo polinómico de grado 2 y finalmente evaluamos un modelo polinómico de grado 3, en el cual vimos que caemos en overfitting, por lo tanto, de los tres modelos planteados, el ganador es el segundo. Se puede seguir probando como mejorar el mismo, pero sabemos que aumentar los grados del polinomio no es una opción.
