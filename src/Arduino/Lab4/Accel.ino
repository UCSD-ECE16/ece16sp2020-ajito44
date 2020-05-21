void setupADC() {
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);
}

void readADC() {
   accelZ_Val = analogRead(accelZ);
   accelY_Val = analogRead(accelY);
   accelX_Val = analogRead(accelX);
}

void printADC(){ 
// Serial.print("Z:");
 Serial.print(accelZ_Val);
 delay(100);
 Serial.print(",");
// Serial.print("Y:");
 Serial.print(accelY_Val);
 
 delay(100);
 Serial.print(",");
 //Serial.print("X:");
 Serial.print(accelX_Val);

 delay(100);
}
