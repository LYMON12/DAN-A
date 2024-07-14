void leitura_faixa(){
  valor_esq_dentro = analogRead(pino_esq_dentro);
  valor_esq_fora = analogRead(pino_esq_fora);
  valor_dir_dentro = analogRead(pino_dir_dentro);
  valor_dir_fora = analogRead(pino_dir_fora);
  valor_meio = analogRead(pino_meio);
Serial.print("  valor_dir_fora:  ");
Serial.print(valor_dir_fora);
Serial.print("  valor_dir_dentro:  ");
Serial.print(valor_dir_dentro);
Serial.print("  valor_meio:  ");
Serial.print(valor_meio);
Serial.print("  valor_esq_dentro:  ");
Serial.print(valor_esq_dentro);
Serial.print("  valor_esq_fora:  ");
Serial.println(valor_esq_fora);
delay(1000);

}