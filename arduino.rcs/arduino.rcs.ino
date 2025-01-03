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

void setup() {
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

void loop() {
  // put your main code here, to run repeatedly:

}


// void Fturn(char direction, int turns) {
//   if (direction == 'C') {
//     digitalWrite(dirPin1,HIGH);
//   }
//   else {
//     digitalWrite(dirPin1,LOW);
//   }

//   for(int x = 0; x < 48*turns; x++) {
//     digitalWrite(stepPin1,HIGH);
//     delayMicroseconds(1000);
//     digitalWrite(stepPin1,LOW);
//     delayMicroseconds(1000);
//   }
// }

// // void Lturn(direction, turns) {
// //   if direction == 'C' {
// //     digitalWrite(dirPin2,HIGH);
// //   }
// //   else {
// //     digitalWrite(dirPin2,LOW);
// //   }

// //   for(int x = 0; x < 50*turns; x++) {
// //     digitalWrite(stepPin2,HIGH);
// //     delayMicroseconds(1000);
// //     digitalWrite(stepPin2,LOW);
// //     delayMicroseconds(1000);
// //   }
// // }

// // void Rturn(direction, turns) {
// //   if direction == 'C' {
// //     digitalWrite(dirPin3,HIGH);
// //   }
// //   else {
// //     digitalWrite(dirPin3,LOW);
// //   }

// //   for(int x = 0; x < 50*turns; x++) {
// //     digitalWrite(stepPin3,HIGH);
// //     delayMicroseconds(1000);
// //     digitalWrite(stepPin3,LOW);
// //     delayMicroseconds(1000);
// //   }
// // }

// // void Bturn(direction, turns) {
// //   if direction == 'C' {
// //     digitalWrite(dirPin4,HIGH);
// //   }
// //   else {
// //     digitalWrite(dirPin4,LOW);
// //   }

// //   for(int x = 0; x < 50*turns; x++) {
// //     digitalWrite(stepPin4,HIGH);
// //     delayMicroseconds(1000);
// //     digitalWrite(stepPin4,LOW);
// //     delayMicroseconds(1000);
// //   }
// // }

// // void Dturn(direction, turns) {
// //   if (direction == 'C') {
// //     digitalWrite(dirPin5,HIGH);
// //   }
// //   else {
// //     digitalWrite(dirPin5,LOW);
// //   }

// //   for(int x = 0; x < 50*turns; x++) {
// //     digitalWrite(stepPin5,HIGH);
// //     delayMicroseconds(1000);
// //     digitalWrite(stepPin5,LOW);
// //     delayMicroseconds(1000);
// //   }
// // }

// void loop() {
//   Fturn('C', 1);
//   delay(1000);
// }