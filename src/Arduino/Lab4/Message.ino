/*
char in_text[64];
int in_text_index = 0;

void receiveMessage() {
  if(Serial.available() > 0) {
    char incomingChar = Serial.read();
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
void setupMessage() {
  Serial.begin(115200);
}

//void printTime(int integer_to_print) {
//  Serial.println(integer_to_print);
//}

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
      readHR();
      Serial.print(last_sample_time);
      Serial.print(",");
      Serial.print(accelX_Val);
      Serial.print(",");
      Serial.print(accelY_Val);
      Serial.print(",");
      Serial.print(accelZ_Val);
      Serial.print(",");
      Serial.println(HR_Data);
 
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
*/
