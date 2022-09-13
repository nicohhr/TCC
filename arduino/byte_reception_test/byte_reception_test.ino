#define DATA_BYTES 6

// Array de bytes com posição das juntas
char pyserialData[DATA_BYTES];
int positions[DATA_BYTES];
int num;

void setup() {
  
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

  Serial.println();
  delay(10);
}
