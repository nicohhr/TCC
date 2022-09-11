// Incluindo bibliotecas
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Definicao de conectores
#define RELE 8
#define SERVOMIN  125 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  530 // This is the 'maximum' pulse length count (out of 4096)

// Instanciando Objeto PWM Servo Driver
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(); 

// Funções
int angle2Bytes(long angle){
  return map(angle, 0, 180, SERVOMIN, SERVOMAX);
}

void setup() {
  
  // Definindo pinos de entrada/saida
  pinMode(RELE, OUTPUT);

  // Alimentando servo motores 
  digitalWrite(RELE, HIGH);
  delay(300);

  // Iniciando Servos
  pwm.begin();
  pwm.setPWMFreq(50);
  delay(300);

  Serial.begin(9600);

}

void loop() {

  pwm.setPWM(0, 0, angle2Bytes(0));
  pwm.setPWM(1, 0, angle2Bytes(0));
  delay(1000);
  pwm.setPWM(0, 0, angle2Bytes(90));
  pwm.setPWM(1, 0, angle2Bytes(90));
  delay(1000);
  pwm.setPWM(0, 0, angle2Bytes(180));
  pwm.setPWM(1, 0, angle2Bytes(180));
  delay(1000);
  pwm.setPWM(0, 0, angle2Bytes(135));
  pwm.setPWM(1, 0, angle2Bytes(135));
  delay(1000);

}
