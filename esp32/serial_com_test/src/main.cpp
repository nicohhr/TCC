#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define MOTOR_CNT 6
#define RELE 5
#define SERVOMIN  125 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  530 // This is the 'maximum' pulse length count (out of 4096)

// Array de bytes com posição das juntas
uint8_t motorPositions[MOTOR_CNT];

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

  // Iniciando comunicação Serial
  Serial.begin(115200);
}

void loop() {
    // Conferindo se há dados seriais recebidos
  if (Serial.available()) {
    
    // Checando por bytes do header -> "OP"
    if (Serial.read() == 'O' && Serial.read() == 'P') {

      // Lendo próximos 6 bytes com valores de posição de cada junta (servomotor)
      Serial.readBytes(motorPositions, MOTOR_CNT);

      // Talvez conferir que cada valor esteja entre 0 e 180

      // Conferindo finalização do pacote -> "ED"
      if (Serial.read() == 'E' && Serial.read() == 'D') {
        
        // Atualizando posição dos motores. 
        // Valores apenas serão escritos se o apcote for válido
        for (int m = 0; m < MOTOR_CNT; m++) {
          pwm.setPWM(m, 0, angle2Bytes(motorPositions[m]));
        }
      }
    }
  }

  // Retornando valores recebidos
  for (int i = 0; i < MOTOR_CNT; i++) {
    Serial.print(" "); 
    Serial.print(motorPositions[i]); 
  }

  Serial.println();
  delay(5);
}