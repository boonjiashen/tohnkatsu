// Controls the motors of TOHKATSU over i2c

#include <Wire.h>
#define SLAVE_ADDRESS 0x04

const int pwmA = 3;
const int brakeA = 9;
const int dirA = 12;
const int pwmB = 11;
const int brakeB = 8;
const int dirB = 13;

// http://arduino.cc/en/Hacking/LibraryTutorial
class DC_motor{
  
  int _pwm_pin;
  int _brake_pin;
  int _dir_pin;
  
  public:
    DC_motor(int brake_pin, int dir_pin, int pwm_pin){
      _brake_pin = brake_pin;
      _dir_pin = dir_pin;
      _pwm_pin = pwm_pin;
    }
    
    void setup(){
      pinMode(_dir_pin, OUTPUT);
      pinMode(_brake_pin, OUTPUT);
    }
      
    // speed_ is between -1 and 1 inclusive
    void set_speed(float speed_){
      int speed_9bit = int(speed_ * 255);
      digitalWrite(_brake_pin, speed_9bit==0 ? HIGH : LOW);
      digitalWrite(_dir_pin, speed_9bit > 0 ? HIGH : LOW);
      analogWrite(_pwm_pin, abs(speed_9bit));
    }
};

DC_motor motorA(brakeA, dirA, pwmA);
DC_motor motorB(brakeB, dirB, pwmB);
  
void setup() {

  Serial.begin(9600);
  motorA.setup();
  motorB.setup();

    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);

    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
}

void loop(){

  motorA.set_speed(1.0);
  motorB.set_speed(1.0);
  delay(3000);
  motorA.set_speed(-1.0);
  motorB.set_speed(-1.0);
  delay(2000);
}

/*
Callback for received data
-----------------------------
number read is expected to be in interval [0, 8]
The more significant digit is for the left motor
The less significant digit is for the right motor
0: reverse
1: stop
2: forward
e.g. 20 base 3 (or 6 in base 10) means reverse left motor and
forward right motor
    */
void receiveData(int byteCount){

    while(Wire.available()) {

        // Get digits (in interval [0, 3]) for left and right motor
        int number = Wire.read();
        int left_digit = number / 3;
        int right_digit = number % 3;

        // Set motor speeds
        motorA.set_speed(left_digit - 1);
        motorB.set_speed(right_digit - 1);
        Serial.print("data received: ");
        Serial.println(number);
    }
}
