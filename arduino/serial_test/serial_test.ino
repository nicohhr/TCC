void setup()
{
  //An LED is Connected Pin12 
  pinMode(LED_BUILTIN, OUTPUT);   //Make Pin12 Output
  digitalWrite(LED_BUILTIN, LOW); //Make Pin12 OFF

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps 8N1

}

void loop()
{
  char RxedByte = 0;

 if (Serial.available()) 
    {
      
      RxedByte = Serial.read();    
       
      switch(RxedByte)
      {
        case 'A':  digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
                   Serial.println("R -> 'A'");
                   break;

        case 'B': //your code
                   break;
        default:
                   break;
      }//end of switch()
    }//endof if 
}