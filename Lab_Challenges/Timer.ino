
void runTimerOLED() {
  while(timer_seconds > 0) {
    timer_seconds--;
    String stringTimer = String(timer_seconds);
    char another_timer[64];
    stringTimer.toCharArray(another_timer,4);
    showMessage(another_timer, 1, true);
  }
}

void addTimer() {
  timer_seconds += 1;
//  printTime(timer_seconds);
  delay(100);
}

void runTimer() {
  while (timer_seconds > 0) {
    timer_seconds -= 1;
    //printTime(timer_seconds);
    delay(100);
  }
}

void Lab2_C2() {
  if (digitalRead(BUTTON_PIN) == LOW) {
    addTimer();
   // int time_1 = millis();
   // delay(100);
   // Serial.println("Time: ");
   // int time_2 = millis();
  //  int yes = time_2 - time_1;
  //  Serial.println(yes);
  }
  else {
    runTimer();
  }
}

void stateMachineTimer() {
  if (timer_state == 0) {
     if(detectTap()) {
      timer_state = 1;
     }
  }
  else if (timer_state == 1) {
      addTimerOLED();
      time_last_tap = millis();
      Serial.println(time_last_tap);
        if (time_last_tap >= time_tap){
        timer_state = 2;
        }
    }
    else if (timer_state == 2) {
      runTimerOLED();
      if (timer_seconds == 0){
        timer_state = 3;
      }
    }
      else if (timer_state == 3) {
        delay(500);
        ledcWrite(pwmChannel, 255);
        if(detectTap()) {
        delay(1000);
        ledcWrite(pwmChannel, 0);
        timer_state = 0;
      }
    }
}
