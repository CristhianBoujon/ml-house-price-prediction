# ml-house-price-prediction
Predict house price using regression

# Intro
Con el objetivo de afianzar los conocimientos sobre machine learning, seleccioné el dataset desde https://www.kaggle.com/harlfoxem/housesalesprediction, en donde el objetivo es predecir el precio de casas.

# Dataset
El dataset utilizado es el que se encuentra en el archivo kc_house_data.csv.

Features:
<ul>
  <li> bedrooms: Catidad de Habitaciones</li>
  <li> bathrooms: Cantidad de baños. 
        <br />
        <b>Aclaración:</b> En el dataset podrán observar que algunos ejemplos son decimales y no enteros (Ver segundo ejemplo, donde      bathrooms = 2.25). 
        Según Wikipedia: <blockquote cite="https://en.wikipedia.org/wiki/Bathroom#Terminology_in_the_United_States">In the United States, bathrooms are generally categorized as master bathroom, containing a varied shower [2] and a tub that is adjoining to a master bedroom, a "full bathroom" (or "full bath"), containing four plumbing fixtures: bathtub/shower, or (separate shower), toilet, and sink; "half (1/2) bath" (or "powder room") containing just a toilet and sink; and "3/4 bath" containing toilet, sink, and shower...</blockquote>
  
  </li>
  <li> sqft_living: Tamaño del living en pie cuadrado</li>
  <li> sqft_lot: Tamaño del terreno en pie cuadrado </li>
  <li> floors: Cantidad de pisos </li>
  <li> waterfront: si la casa tiene vista al río. 0 = No / 1 = Si </li>
  <li> view </li>
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
  <li> grade: Representa la calidad de la construcción </li>
  <li> sqft_above </li>
  <li> sqft_basement: Tamaño del sótano en pie cuadrado </li>
  <li> yr_built: Año de la consutrucción de la casa. </li>
  <li> yr_renovated: Año en que se hicieron mejoras significativas en la casa. </li>
  <li> zipcode: Código Postal </li>
  <li> lat: Coordenadas - Latitud </li>
  <li> long Coordenadas - Longitud </li>
  <li> sqft_living15: Tamaño promedio del living de las 15 casas más cerca en pie cuadrado. </li>
  <li> sqft_lot15: Tamaño promedio del terreno de las 15 casas más cerca en pie cuadrado. </li>
  <li> price: Precio en dólares </li> 
</ul>
<b>Nota: </b> El archivo kc_house_data_orginal.csv es el dataset original, el cual contiene las columnas "id" que es un identificador único de cada registro y la columna "date" que es la fecha en la que se realizó el registro. Éstas columnas fueron quitadas ya que no aportan ningún valor al modelo.

# Proceso
<h2>1-linear_regression.py </h2>
Realicé un proceso de tres pasos para determinar el modelo.
Siempre es recomendable comenzar por lo más sencillo y si no da resultado, ir aumentando la complejidad, es por ésto que comencé con el  script "1-linear_regression.py", en el cual hice una primera prueba para determinar que tan bien se ajusta el dataset a un modelo lineal. Ésto nos dará una pauta de cuales son los pasos a seguir.
