#include<Servo.h>
Servo myservo;  

int pin1 = 0;
int pin2 = 0;
int flag1 = 0;
int flag2 = 0;
int count = 0;

const int del = 350;
int angle = 0;


//int led = 13;

void setup()
{
  myservo.attach(9);
  //pinMode(led, OUTPUT);
  myservo.write(0);
  Serial.begin(9600);
}

  
void loop()
{
  pin1 = analogRead(A0);
  pin2 = analogRead(A1);

  Serial.println("A0 value");
  Serial.println(pin1);
  Serial.println("A1 value");
  Serial.println(pin2);
 
  pin1 = analogRead(A0);
  pin2 = analogRead(A1);   

  if(pin1 > 280 && pin1 < 380 && pin2 > 280 &&  pin2 < 380) //1 1
  {
    angle=angle+30; 
    myservo.write(angle);
    Serial.println("condition 1");
    delay(del); 
  }
  else if(pin1 > 280 && pin1 < 380 && pin2 == 0 ) // 1 0
  {
    angle=angle+30;
    myservo.write(angle);
    Serial.println("condition 2");
         delay(del);
  }else if(pin1 == 0 && pin2 > 280 &&  pin2 < 380) // 0 1
  {
    angle=angle+30;
    myservo.write(angle);
    Serial.println("condition 3");
    delay(del);
  }
  else                                           // 0 0
  {
    //myservo.write(45);
    Serial.println("condition 4");
    delay(del);
  }
}

