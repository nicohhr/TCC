// Incluindo bibliotecas
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define DATA_BYTES 6
#define RELE 8
#define SERVOMIN  125 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  530 // This is the 'maximum' pulse length count (out of 4096)

// Array de bytes com posição das juntas
char pyserialData[DATA_BYTES];
int positions[DATA_BYTES];
int num;

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
  
  if(Serial.available()){
    
    Serial.readBytes(pyserialData, DATA_BYTES);

    for (int i = 0; i < DATA_BYTES; i++) {
      num = (uint8_t)(pyserialData[i]);
      positions[i] = num; 
    }
  }

  for (int i = 0; i < DATA_BYTES; i++) {
    Serial.print(" "); 
    Serial.print(positions[i]); 
  }

  // Escrita nos motores
  pwm.setPWM(0, 0, angle2Bytes(positions[0]));

  Serial.println();
  delay(10);
}
