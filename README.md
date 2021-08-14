# Luhn Manage API

## Algoritmo de Luhn

#### ¿Que es el algoritmo de luhn?

Tambien conocido como "algoritmo de modulo 10", es una formula que se utiliza para determinar
si el número de identificación proporcionado por un usuario es valido. Esta formula es implementada
ampliamente para validar numeros de tarjetas de crédito, números IMEI, etc.

Hoy en día, el algoritmo de Luhn es un componente esencial en el sistema de pagos electrónicos y lo utilizan
todas las principales tarjetas de crédito.

#### ¿Cómo funciona?

El algoritmo de fórmula LUHN fue desarrollado por un informático alemán llamado Hans Peter Luhn en 1954 mientras trabajaba como investigador en IBM.

El algoritmo aplica una serie de cálculos al número de tarjeta de crédito dado, sumando los resultados de esos cálculos y verificando si el número resultante coincide con el resultado esperado. Si es así, el número de crédito se considera valido. De lo contrario, el algoritmo rechazará el número de la tarjeta de crédito, lo que indica que el usuario cometió un error al ingresas el número.

Ejemplo: dado un número de cuenta "**79927398713** ".

1. Cómo primer paso, comenzando desde el primer digito se duplica el valor cada segundo digito.
2. Si el resultado de la dupliación del digito da como resultado un numero de 2 digitos, estos deben ser sumando y este sera el resultado tomado. Ejemplo: (9 x 2= 18 -> 1 + 8 = 9)
3. Como tercer paso se deben sumar todos los digitos
4. Por ultimo si el modulo 10 del valor del resultado es 0, entonces el número es válido según la fórmula de Luhn; de lo contrario, no es válido.
   ![enter image description here](https://media.geeksforgeeks.org/wp-content/uploads/gfg2-2-300x101.png)
   En el ejemplo, la suma total de los digitos es 70, que es multiplo de 10, dando como resultado un número de cuenta válido

## Descripción

Esta API te proporciona un sistema de validación de números de tarjetas de credito implementando el algoritmo de luhn, adicional a esta verificación te proporciona la entidad a la que pertenece la tarjeta de credito ingresada.

#### Configuración

Estas instrucciones le proporcionarán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba.

#### Prerequisitos

Qué necesita para instalar el software y cómo instalarlo.

```
Python 3.6 o mayor.
Docker
```

### Instalación

Por favor considere usar entornos virtuales de python o ejecute el contenedor de Docker.

1.  clonar el repositorio `git clone https://github.com/danielcinome/Luhn-Algorithm.git`.
2.  ir a la carpeta Luhn-Algorithm con el comando `cd Luhn-Algorithm`.
3.  Ejecutar el entorno.

    - **Docker**

           ***Crear contenedor***

      `docker-compose build`

          ***Ejecutar el proyecto***

      `docker-compose up`

    - **Entorno virtual de Python**

            ***Crear entorno virtual***

      `virtualenv -p /usr/bin/python3 venv`

      **_Activar el entorno virtual e instalar las dependencias_**
      `source venv/bin/activate`
      `python -m pip install -r requirements.txt`

          **Ejecutar el proyecto**

      `make run`

### EndPoints y documentación

Una vez ejecute el proyecto puede ver que todos los EndPoint estan documentados en [https://0.0.0.0:5001/docs](https://0.0.0.0:5001/docs)

![enter image description here](https://i.ibb.co/gttpdyc/docs.png)

### Test

La API tambien proporciona Tests para validar el funcionamiento bajo diferentes casos y que funcione de manera correcta. Puede ver los test en el archivo [test_main ](https://github.com/danielcinome/Luhn-Algorithm/app/tests/test_main.py).

![enter image description here](https://i.ibb.co/pbxkrr0/Test.png)

### Tarjetas de Credito de Prueba

**Nota:** Los números de tarjeta de credito proporcionados son _fakes_ para pruebas.

| Entidad              | Número de Tarjeta |
| -------------------- | ----------------- |
| **VISA**             | 4916043910334916  |
| **VISA**             | 4759608675815786  |
| **MasterCard**       | 5394905750520382  |
| **MasterCard**       | 5480981995050720  |
| **American Express** | 371324254460426   |
| **American Express** | 349085228259991   |
| **Diners Club**      | 30184823193533    |
| **Diners Club**      | 30590395301496    |
| **Discover**         | 6011874716401775  |
| **Discover**         | 6011269884123600  |
| **Maestro**          | 5018680950126365  |
| **Maestro**          | 6763679934270807  |

### Caso Ejemplo de prueba

![enter image description here](https://i.ibb.co/Nr8nNK6/prueba.png)

## Autor

- Daniel Chinome - [Github](https://github.com/danielcinome) / [Twitter](https://twitter.com/DanielChinome)
