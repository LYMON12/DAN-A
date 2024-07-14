#include <Ultrasonic.h>
#include <VarSpeedServo.h>
Ultrasonic ultra(22,23);
int distancia;

VarSpeedServo dir_frente;
VarSpeedServo esq_frente;
VarSpeedServo dir_tras;
VarSpeedServo esq_tras;
int faixa = 200;

int pino_dir_fora = A0;
int valor_dir_fora;

int pino_dir_dentro = A1;
int valor_dir_dentro;

int pino_esq_fora = A4;
int valor_esq_fora;

int pino_esq_dentro = A3;
int valor_esq_dentro;

int pino_meio = A2;
int valor_meio;

int bt = 27;
int estado_bt;

void setup() {
  Serial.begin(9600);
pinMode(pino_esq_dentro, INPUT);
pinMode(pino_esq_fora, INPUT);
pinMode(pino_dir_dentro, INPUT);
pinMode(pino_dir_fora, INPUT);
pinMode(pino_meio, INPUT);

esq_frente.attach(4);
dir_frente.attach(7);
esq_tras.attach(5);
dir_tras.attach(6);

}

void loop() {
distancia = ultra.read();
estado_bt = digitalRead(bt);
valor_esq_dentro = analogRead(pino_esq_dentro);
valor_esq_fora = analogRead(pino_esq_fora);
valor_dir_dentro = analogRead(pino_dir_dentro);
valor_dir_fora = analogRead(pino_dir_fora);
valor_meio = analogRead(pino_meio);

while(estado_bt == 1) {
para();
delay(100);
}

segue_faixa();
//Serial.println(distancia);

}
