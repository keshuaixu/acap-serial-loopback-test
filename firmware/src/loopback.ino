void setup(){
  Serial.begin(115200);
}

void loop(){
  for (;;){
    if (Serial.available()){
      char c = Serial.read();
      Serial.write(c);
    }
  }
}
