#define stepPin1 2
#define dirPin1 3
#define stepPin2 4
#define dirPin2 5
#define stepPin3 6
#define dirPin3 7
#define stepPin4 8
#define dirPin4 9
#define stepPin5 10
#define dirPin5 11

void Fturn(int turns) {
  digitalWrite(dirPin1,HIGH);
  for(int x = 0; x < 50*turns; x++) {
    digitalWrite(stepPin1,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin1,LOW);
    delayMicroseconds(1000);
  }
}

void Lturn(int turns) {
  digitalWrite(dirPin2,HIGH);

  for(int x = 0; x < 50*turns; x++) {
    digitalWrite(stepPin2,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin2,LOW);
    delayMicroseconds(1000);
  }
}

void Rturn(int turns) {
  digitalWrite(dirPin3,HIGH);

  for(int x = 0; x < 50*turns; x++) {
    digitalWrite(stepPin3,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin3,LOW);
    delayMicroseconds(1000);
  }
}

void Bturn(int turns) {
  digitalWrite(dirPin4,HIGH);

  for(int x = 0; x < 50*turns; x++) {
    digitalWrite(stepPin4,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin4,LOW);
    delayMicroseconds(1000);
  }
}

void Dturn(int turns) {
  digitalWrite(dirPin5,HIGH);

  for(int x = 0; x < 50*turns; x++) {
    digitalWrite(stepPin5,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin5,LOW);
    delayMicroseconds(1000);
  }
}

void setup() {
  Serial.begin(9600);

  pinMode(stepPin1,OUTPUT);   
  pinMode(dirPin1,OUTPUT);
  pinMode(stepPin2,OUTPUT);   
  pinMode(dirPin2,OUTPUT);
  pinMode(stepPin3,OUTPUT);   
  pinMode(dirPin3,OUTPUT);
  pinMode(stepPin4,OUTPUT);   
  pinMode(dirPin4,OUTPUT);
  pinMode(stepPin5,OUTPUT);   
  pinMode(dirPin5,OUTPUT);
}

done = False;
void loop() {
  if (Serial.available()) {
    if (done == False) {
      String data = Serial.readStringUntil('\n'); // Read until newline character
      Serial.println("Received: " + data); // Print the received data

      String result[30]; 
      int index = 0;

      int startIndex = 0;
      int endIndex = data.indexOf(' ');

      while (endIndex != -1) {
        result[index++] = data.substring(startIndex, endIndex);
        startIndex = endIndex + 1;
        endIndex = data.indexOf(' ', startIndex);
      }
      result[index] = data.substring(startIndex);

      for (int i = 0; i <= index-1; i++) {
        char motor = result[i][0];
        char turn = result[i][1];
        int turns = (int)turn;

        Serial.println(motor);

        if (motor == 'U') {
          Serial.println('poop');
        }
        else if (motor == 'F') {
          Fturn(turns);
        }
        else if (motor == 'R') {
          Rturn(turns);
        }
        else if (motor == 'L') {
          Lturn(turns);
        }
        else if (motor == 'D') {
          Dturn(turns);
        }
        else if (motor == 'B') {
          Bturn(turns);
        }
      }    
      done = True;
    }
  }
}