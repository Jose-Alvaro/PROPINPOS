# PROPINPOS

PoyectoPinguinosPostgress viene del todopoderoso sueño de organizar a todos los pinüinos del planeta.
![alt text](https://github.com/Jose-Alvaro/PROPINPOS/blob/main/img/intro.png)

#Recursos usados




Para ello utilizaremos un CSV que contiene parte de esta información:
![alt text](https://github.com/Jose-Alvaro/PROPINPOS/blob/main/img/csvpin.png)

Primero debemos limpiar datos que no nos son necesarios o que no queremos que se muestren, por ejemplo:
    "Region" : Es un campo que no aporta información por que es siempre el mismo valor.
    "Comments" : Un valor eliminable por lo objetivo de este que no añade nada a la clasificación.

Además tambien hayproblemas con los valores nulos, los cuales no queremos que molesten en nuestra base de datos:
![alt text](https://github.com/Jose-Alvaro/PROPINPOS/blob/main/img/NaNPin.png)

Estos valores deben desaparecer:
![alt text](https://github.com/Jose-Alvaro/PROPINPOS/blob/main/img/balancedpin.png)

Listo!, "Ar sielo (base de datos) con ellos":
![alt text](https://github.com/Jose-Alvaro/PROPINPOS/blob/main/img/sielopin.png)

