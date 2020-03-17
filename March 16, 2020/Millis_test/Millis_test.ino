unsigned long time;

void setup() {
  Serial.begin(9600);
}

int counter
void loop() {
  counter ++
  if (counter == 30){
    counter == 0;
    Serial.print("Time: ");
    time = millis();

    Serial.println(time); //prints time since program started
    delay(1000);          // wait a second so as not to send massive amounts of data
  }
}
