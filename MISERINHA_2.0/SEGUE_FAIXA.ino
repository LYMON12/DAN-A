void segue_faixa() {
  valor_esq_dentro = analogRead(pino_esq_dentro);
  valor_esq_fora = analogRead(pino_esq_fora);
  valor_dir_dentro = analogRead(pino_dir_dentro);
  valor_dir_fora = analogRead(pino_dir_fora);
  valor_meio = analogRead(pino_meio);

if(valor_esq_fora < faixa && valor_dir_fora < faixa) {
  frente();
}
  if(valor_esq_dentro > faixa){
    para();
    delay(10);
    esquerda(); 
    delay(50);
    }

  if(valor_dir_dentro > 400){
    para();
    delay(10);
    direita();
    delay(50);
  }

//------FALSO_ESQ-------------------------------------------
if(valor_esq_dentro > faixa && valor_esq_fora > faixa && valor_dir_fora < faixa) {
para();
delay(50);
frente();
delay(270);
valor_meio = analogRead(pino_meio);
while(valor_meio < faixa)  {
valor_meio = analogRead(pino_meio);
esquerda();
if(valor_meio > faixa) {
  para();
  delay(200);
}
}
}
//--------------
if(valor_dir_dentro > faixa && valor_dir_fora > faixa && valor_esq_fora < faixa) {
para();
delay(50);
frente();
delay(270);
valor_meio = analogRead(pino_meio);
while(valor_meio < faixa)  {
valor_meio = analogRead(pino_meio);
direita();
if(valor_meio > faixa) {
  para();
  delay(200);
}
}
}


}