#include "U8x8lib.h"

#define OLED_RESET 4
U8X8_SSD1306_128X32_UNIVISION_HW_I2C u8x8(OLED_RESET);

void initDisplay() {
  u8x8.begin();
  u8x8.setPowerSave(0);
  u8x8.setFont(u8x8_font_amstrad_cpc_extended_r);
  u8x8.setCursor(0, 0);
}

void showMessage(const char * message, int row, bool clearDisplay) {
  if(clearDisplay){
    u8x8.clearDisplay();
  }
  u8x8.setCursor(0, row);
  u8x8.print(message);
}

void addTimerOLED() {
  timer_seconds += 1;
  String stringTime = String(timer_seconds);
  char message_buffer[64];
  stringTime.toCharArray(message_buffer,4);
  showMessage(message_buffer, 1, true);
}
