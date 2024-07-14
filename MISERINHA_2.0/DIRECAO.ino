void frente() {
   esq_frente.write(170, 100);
  esq_tras.write(170, 100);
  dir_frente.write(15, 100);
  dir_tras.write(15, 100);
}

void re() {
  esq_frente.write(25, 70);
  esq_tras.write(25, 70);
  dir_frente.write(151, 70);
  dir_tras.write(151, 70);
}

void direita(){
  dir_frente.write(150, 150);
  dir_tras.write(150, 150);
  esq_frente.write(150, 150);
  esq_tras.write(150, 150);
}

void esquerda(){
  esq_frente.write(20, 150);
  esq_tras.write(20, 150);
  dir_frente.write(20, 150);
  dir_tras.write(20, 150);
}

void para() {
  esq_frente.write(90, 0);
  esq_tras.write(90, 0);
  dir_frente.write(90, 0);
  dir_tras.write(90, 0);
}