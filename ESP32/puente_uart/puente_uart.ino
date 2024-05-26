#include <DMXSerial.h>

#define DMX_TX_PIN 3
#define DMX_ENABLE_PIN 2

void setup() {
  pinMode(DMX_ENABLE_PIN, OUTPUT);
  digitalWrite(DMX_ENABLE_PIN, HIGH);  // Habilitar el transceptor para transmisión
  DMXSerial.init(DMXController);
}

void loop() {
  DMXSerial.write(1, 255);  // Enviar valor máximo al canal 1
  delay(1000);
  DMXSerial.write(1, 0);    // Enviar valor mínimo al canal 1
  delay(1000);
}