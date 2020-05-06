/*#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

void setupMessage() {
  
  SerialBT.begin("Angela_Bluetooth");
}

char in_text[64];
int in_text_index = 0;

void receiveMessage() {
  if(SerialBT.available() > 0) {
    char incomingChar = SerialBT.read();
    if (incomingChar == 10) {
      showMessage(in_text, 1, true);
      checkMessage();
      in_text_index = 0;
      memset(in_text,0,20);
    }
    else{
      in_text[in_text_index] = incomingChar;
      in_text_index += 1;
    }
  } 
}


void printTime(int integer_to_print) {
  SerialBT.println(integer_to_print);
}

int sampling_rate = 50;
unsigned long sampling_delay = calcSamplingDelay(sampling_rate);
unsigned long last_sample_time = 0;
unsigned long startTime = 0;
bool sending_data = false;

void sendData() {
  if(sending_data) {
  unsigned long lastsampletime = micros();
    if(lastsampletime - last_sample_time > sampling_delay) {
      last_sample_time = micros();
      readADC();
      SerialBT.print(last_sample_time);
      SerialBT.print(",");
      SerialBT.print(accelX_Val);
      SerialBT.print(",");
      SerialBT.print(accelY_Val);
      SerialBT.print(",");
      SerialBT.println(accelZ_Val);
 
    }
  }
}

long calcSamplingDelay(long sampling_rate) {
  return 1000000/sampling_rate;
}

void checkMessage() {
  String message = String(in_text);
    if (message == "stop data" ) {
      sending_data = false;
    }
    if(message == "start data") {
      sending_data = true;
      delay(1000);
    }
  
}


//void printTime(int seconds) {
 // SerialBT.println(seconds);
//}
*/
