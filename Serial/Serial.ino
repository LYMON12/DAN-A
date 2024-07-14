char s;

void setup() {
  Serial.begin(9600);

}

void loop() {
  s = Serial.read();

if(s == 'a') {
  Serial.println("ABERTO");
} else if(s == 'f') {
  Serial.println("FECHADO");
}
else {
  Serial.println("NENHUMA TECLA FOI DISCADA");
}

}
