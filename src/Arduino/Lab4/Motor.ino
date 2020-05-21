const int pwmFrequency = 5000;
const int pwmChannel = 3;
const int pwmBitResolution = 8;
int motorPin = 13;

void setupMotor() {
  ledcSetup(pwmChannel, pwmFrequency, pwmBitResolution);
  ledcAttachPin(motorPin, pwmChannel);
}

void Lab2_C4() {
  delay(1000);
  ledcWrite(pwmChannel, 255);
  delay(1000);
  ledcWrite(pwmChannel, 127);
  delay(1000);
  ledcWrite(pwmChannel, 0);
  }
