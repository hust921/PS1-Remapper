#include <Psx.h>

Psx Psx;

void setup()
{
  Psx.setupPins(2, 4, 6, 8, 10);
  Serial.begin(9600);
}

void loop() 
{
  Serial.println(Psx.read());
  delay(100);
}
