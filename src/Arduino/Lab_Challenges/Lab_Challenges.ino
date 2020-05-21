const int RED_LED = 32;
const int YELLOW_LED = 15;
const int BLUE_LED = 33;
const int BUTTON_PIN = 14;
int timer_seconds = 0;
unsigned long time_to_wait = 1000;
int accelZ = A2;
int accelY = A3;
int accelX = A4;
int accelZ_Val = 0;
int accelY_Val = 0;
int accelX_Val = 0;
const long time_tap = 3000;
unsigned long time_last_tap = 0;
int timer_state = 0;

void setup() {
// setupLED();
 setupButton();
 setupMessage();
 //Serial.begin(9600);
  // setupMotor();
  setupADC();
 
initDisplay();
//showMessage("Initializing...", 1, true);
//showMessage("Success!", 2, false);

 
}

void loop() {
 // addTimer();
// condition1();
 // condition2();
//  condition3();
 // condition4();
 // condition5();
 // condition6();
 //Lab2_C2();
   // Lab2_C4();
  // readADC();
  // printADC();
 //  Lab3();
   //sendData();
  // Lab2_C5();
  // Lab2_C7();
  Lab3_Challenge5(); 
 // Lab3_Challenge6();
  // receiveMessage();
 //  stateMachineTimer();
  //if(Serial.available() > 0){
    
//int incomingByte = Serial.read();
//Serial.print("I received: ");
//Serial.println(incomingByte, DEC);



  }


 // void Lab2_C5() {
 //  if(detectTap()) {
 //     addTimerOLED();
 //   }
 // }
//void Lab2_C7() {
 // if (detectTap()) {
 //   addTimerOLED();
 //   time_last_tap = millis();
 //   Serial.println(time_last_tap);
 // }
  // else if(time_last_tap > time_tap) {
  //  runTimerOLED();
 // }
//}

void Lab3() {
  sendData();
  receiveMessage();
}

void Lab3_Challenge5() {
  sendData();
  receiveMessage();
}

void Lab3_Challenge6() {
  receiveMessage();
  sendData();
//  refreshButton();
}
