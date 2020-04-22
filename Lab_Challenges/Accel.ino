void setupADC() {
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);
  Serial.begin(9600);
}

void readADC() {
   accelZ_Val = analogRead(accelZ);
   accelY_Val = analogRead(accelY);
   accelX_Val = analogRead(accelX);
}

void printADC(){ 
 Serial.print("Z:");
 Serial.println(accelZ_Val);
 delay(100);
 Serial.print(",");
 Serial.print("Y:");
 Serial.println(accelY_Val);
 delay(100);
 Serial.print(",");
 Serial.print("X:");
 Serial.println(accelX_Val);
 delay(100);
}

