void setupButton() {
  pinMode(BUTTON_PIN, INPUT);
}

bool getButton() {
  bool button_val = BUTTON_PIN;
  return button_val;
}

