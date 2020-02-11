#include <Wire.h>
#include "Adafruit_SGP30.h"

Adafruit_SGP30 sgp;

void setup() {
  Serial.begin(9600);
//  Serial.println("SGP30 test");


  if (! sgp.begin()){
    Serial.println("Sensor not found :(");
    while (1);
  }
}

int counter = 0;

void loop() {

  if (! sgp.IAQmeasure()) {
    Serial.println("Measurement failed");
    return;
  }
  Serial.print(sgp.TVOC); Serial.print(",");  
  Serial.println(sgp.eCO2);

delay(1000);
}

//A este código le falta establecer los valores de baseline
//Y también el cálculo de la humedad absoluta, para esto ocupo la temperatura y humedad relativa. 
