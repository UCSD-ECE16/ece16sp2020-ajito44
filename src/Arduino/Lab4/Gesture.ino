int threshZ = 2365;
int threshY = 1890;
int threshX = 1865;

bool detectTap() {
   accelZ_Val = analogRead(accelZ);
   accelY_Val = analogRead(accelY);
   accelX_Val = analogRead(accelX);
   bool tap_detected = false;
   if(accelZ_Val > threshZ and accelY_Val > threshY and accelX_Val > threshX){
    tap_detected = true;
   }
   return tap_detected;
}
