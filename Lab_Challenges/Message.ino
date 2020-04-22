char in_text[64];
int in_text_index = 0;

void receiveMessage() {
  if(Serial.available() > 0) {
    char incomingChar = Serial.read();
    if (incomingChar == 10) {
      showMessage(in_text, 1, true);
      in_text[in_text_index] = 0;
      memset(in_text,0,20);
    }
    else{
      in_text[in_text_index] = incomingChar;
      in_text_index += 1;
    }
  } 
}
void setupMessage() {
  Serial.begin(9600);
}

void printTime(int integer_to_print) {
  Serial.println(integer_to_print);
}

