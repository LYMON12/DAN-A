char recebido;

void setup() {
 Serial1.begin(9600);
Serial.begin(9600);
}

void loop() {
recebido = Serial1.read();

  if(recebido = "ola") {
    Serial.println("chegou");
    delay(800);
  }

}
