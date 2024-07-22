#include "Adafruit_APDS9960.h"
Adafruit_APDS9960 apds;

void setup() {
  Serial.begin(115200);
  
  if(!apds.begin()){
    Serial.println("failed to initialize device! Please check your wiring.");
  }
  else Serial.println("Device initialized!");

  apds.enableProximity(true);
  apds.enableGesture(true);
}

void loop() {

uint8_t gesture = apds.readGesture();

  //if(gesture == APDS9960_DOWN) Serial.println("v");
  //if(gesture == APDS9960_UP) Serial.println("^");
  //if(gesture == APDS9960_LEFT) Serial.println("<");
  //if(gesture == APDS9960_RIGHT) Serial.println(">");

if(gesture > 0) {
  Serial.println("HOUVE UM GESTO");
}
 
}