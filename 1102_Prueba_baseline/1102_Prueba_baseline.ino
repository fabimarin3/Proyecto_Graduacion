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

  uint16_t TVOC_base, eCO2_base;
  if (! sgp.getIAQBaseline(&eCO2_base, &TVOC_base)) {
    Serial.println("Failed to get baseline readings");
    return;
  }
  Serial.print(eCO2_base, HEX);Serial.print(","); 
  Serial.println(TVOC_base, HEX);
  delay(1000);
  }
