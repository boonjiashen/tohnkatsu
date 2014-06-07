// Controls the motors of the Ardupi

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
  motorA.setup();
  motorB.setup();
  Serial.begin(9600);
}

void loop(){
  
  /*
//  if (Serial.available()){
//    byte c = Serial.read();
  if (1){
//    char c = 256;
//    char c = 0;
    float delta = (c - 128.) / 128.;
    float center_speed = 0.85;
    motorA.set_speed(center_speed + delta*(1-center_speed));
    motorB.set_speed(center_speed - delta*(1-center_speed));
  }
  */

  motorA.set_speed(1.0);
  motorB.set_speed(1.0);
  delay(3000);
  motorA.set_speed(-1.0);
  motorB.set_speed(-1.0);
  delay(2000);
}

