float Sensibilidad = 0.066; /* Según las especificaciones de este modelo */
float offset = 0.100; // Buscamos que sea un valor aproximado a la amplitud del ruido
float voltajeRed = 127.0; // Común en México pero es necesario un ajuste

void setup() {
  Serial.begin(9600);
}

void loop() {
    // Obtiene la corriente de cada uno de los tres sensores
  float corrienteSensor1 = get_corriente(A0);
 // float corrienteSensor2 = get_corriente(A1);
 // float corrienteSensor3 = get_corriente(A2);
  
  Serial.print("Irms Sensor 1: ");
  Serial.print(corrienteSensor1, 3);
  Serial.println(" A");

  Serial.print("Irms Sensor 2: ");
  Serial.print(corrienteSensor2, 3);
  Serial.println(" A");

  Serial.print("Irms Sensor 3: ");
  Serial.print(corrienteSensor3, 3);
  Serial.println(" A");
 // Espera un poco antes de la próxima iteración
}


float get_corriente(int pin) {
  float voltajeSensor;
  float corriente = 0;
  long tiempo = millis();
  float Imax = 0;
  float Imin = 0;
  float V0 = 2.460; // voltaje en OUT cuando la corriente a medir es 0A (varia de dispositivo a dispositivo)
  while (millis() - tiempo < 500) { // realizamos mediciones durante 0.5 segundos
    voltajeSensor = analogRead(pin) * (5.0 / 1023.0); // lectura del sensor
    /* para disminuir un poco el ruido aplicamos un filtro pasa bajos, que es similar a realizar un promedio de 10 muestras*/
    corriente = 0.9 * corriente + 0.1 * ((voltajeSensor - V0) / Sensibilidad); // Ecuación para obtener la corriente
    if (corriente > Imax) Imax = corriente;
    if (corriente < Imin) Imin = corriente;
  }
  return (((Imax - Imin) / 2) - offset);
}