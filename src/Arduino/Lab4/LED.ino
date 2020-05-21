void setupLED() {
  int RED_LED = 32;
  int YELLOW_LED = 15;
  int BLUE_LED = 33;
  }

  void condition1() {
   pinMode(LED_BUILTIN, OUTPUT);
     digitalWrite(LED_BUILTIN, HIGH);
     delay(1000);
     digitalWrite(LED_BUILTIN, LOW);
     delay(1000);
  }

  void condition2() {
    pinMode(LED_BUILTIN, OUTPUT);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      digitalWrite(LED_BUILTIN, LOW);
      delay(100);
    }
  

   void condition3() {
    pinMode(LED_BUILTIN, OUTPUT);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(200);
      digitalWrite(LED_BUILTIN, LOW);
      delay(200);
    }
   

   void condition4() {
    pinMode(RED_LED, OUTPUT);
      digitalWrite(RED_LED, HIGH);
      delay(1000);
      digitalWrite(RED_LED, LOW);
      delay(100);
    }
   
  
   void condition5() {
    pinMode(YELLOW_LED, OUTPUT);
      digitalWrite(YELLOW_LED, HIGH);
      delay(200);
      digitalWrite(YELLOW_LED, LOW);
      delay(50);
    }
   
  
   void condition6() {
    pinMode(BLUE_LED, OUTPUT);
      digitalWrite(BLUE_LED, HIGH);
      delay(20);
      digitalWrite(BLUE_LED, LOW);
      delay(10);
    }
    
