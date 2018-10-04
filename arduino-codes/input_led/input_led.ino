
int led1 = 11; //Red
int led2 = 12; //Yellow
int led3 = 13; //Green
int pin1;
int pin2;

void setup() {                
  pinMode(led1, OUTPUT);     
  pinMode(led2, OUTPUT);     
  pinMode(led3, OUTPUT); 
  Serial.begin(9600);

}

void loop() 
{

    pin1 = analogRead(A0); // GPIO = 337 aka 25
    delay(500);
    pin2 = analogRead(A1); // GPIO = 501 aka 31
    delay(500);


  Serial.println("A0 value");
  Serial.println(pin1);
  Serial.println("A1 value");
  Serial.println(pin2);

  if(pin1 > 300 && pin1 < 380 && pin2 > 300 &&  pin2 < 380) // 1 1 = Green
  {
    digitalWrite(led3, HIGH);   
    digitalWrite(led2, LOW);                 
    digitalWrite(led1, LOW); 
  }
  else if(pin1 > 300 && pin1 < 380 && pin2 == 0 ) // 1 0 = Yellow
  {
    digitalWrite(led1, LOW);   
    digitalWrite(led2, HIGH);                 
    digitalWrite(led3, LOW); 
  } 
  else if(pin1 == 0 && pin2 ==0) // 0 0 = Red
  {
    digitalWrite(led3, LOW);   
    digitalWrite(led2, LOW);                 
    digitalWrite(led1, HIGH); 
  } 
  else if(pin1 == 0 && pin2 > 300 && pin2 < 380) // 0 1 - Yellow Blink
  {
    digitalWrite(led1, LOW);   
    digitalWrite(led2, HIGH);                 
    digitalWrite(led3, LOW);
    delay(200);
    digitalWrite(led1, LOW);   
    digitalWrite(led2, LOW);                 
    digitalWrite(led3, LOW);
    
  }
}



