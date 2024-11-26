#define stepPin1 2
#define dirPin1 3

void setup() {
  pinMode(stepPin1,OUTPUT);   
  pinMode(dirPin1,OUTPUT);
}

void loop() {
    for(int x = 0; x < 50*turns; x++) {
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(1000);
        digitalWrite(stepPin1,LOW);
        delayMicroseconds(1000);
  }
}