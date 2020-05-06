#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

void setupMessage() {
  SerialBT.begin("Angela_Bluetooth");
}

int sampling_rate = 50;
unsigned long sampling_delay = calcSamplingDelay(sampling_rate);
unsigned long last_sample_time = 0;
unsigned long startTime = 0;
bool sending_data = false;
int flag = 0;
char in_text[64];
int in_text_index = 0;

void sendData() {
  if(sending_data) {
  //unsigned long lastsampletime = micros();
  //  if(lastsampletime - last_sample_time > sampling_delay) {
  //   last_sample_time = micros();
      SerialBT.println("Seattle, US");
    }
  //}

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

void receiveMessage() {
  if(SerialBT.available() > 0) {
    char incomingChar = SerialBT.read();
    if (incomingChar == ',' && flag == 0) {
      String temp = String(in_text);
      showMessage(in_text, 1, true);
      delay(1000);
      checkMessage();
      in_text_index = 0;
      memset(in_text,0,20);
      flag = 1;
    }
    else if (incomingChar ==',' && flag == 1) {
      String sunrise = String(in_text);
      showMessage(in_text, 1, true);
      delay(1000);
      checkMessage();
      in_text_index = 0;
      memset(in_text,0,20);
      flag = 0;
    }
    else if (incomingChar == '\n') {
      String sunset = String(in_text);
      showMessage(in_text, 2, true);
      delay(1000);
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

void refreshButton() {
  if(digitalRead(BUTTON_PIN) == LOW) {
    sending_data = true;
  }
  else{
    sending_data = false;
  }
}
      
