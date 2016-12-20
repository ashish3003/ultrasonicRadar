/************************************************************************************************************
* @filename : ultrasonicRadar                                                                                 
* @author   : Ashish Sharma
* @brief    : Program for Ultrasonic Sensing Radar.
*             Components required: Arduino Microcontroller (Nano used here), HC-SR04 Ultrasonic Transceiver,
*                                  SG90 Servo Motor, Mounting arrangement.
*             Connect "Trig" pin of HC-SR04 to pin D7
*             Connect "Echo" pin of HC-SR04 to pin D8
*             Connect servo motor signal pin to pin D9
************************************************************************************************************/

#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 

const int loopPeriod = 20;
unsigned long loopdelay = 0;
const int trig = 7; // ARDUINO OUTPUT PIN FOR SENSOR
const int echo = 8;
long ultraDuration, ultraDistance;
//char incomingData;

void setup()
{
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(115200);
}

void loop()
{
    if (Serial.available() > 0) {
    char incomingData = (char)Serial.read();
    if ('1' == incomingData)
    {  
      for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees 
      {
        // in steps of 1 degree 
        Serial.print(pos);
        Serial.print(",");
        myservo.write(pos);              // tell servo to go to position in variable 'pos' 
        delay(50);
        readUltrasonicSensors();
        //delay(50);           // waits 15ms for the servo to reach the position 
      } 
      delay(50);
      for(pos = 180; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees 
      {   
        Serial.print(pos);
        Serial.print(",");
        myservo.write(pos);              // tell servo to go to position in variable 'pos' 
        delay(50);
        readUltrasonicSensors();    
        //delay(50);                       // waits 15ms for the servo to reach the position 
      } 
    }
    //  loopdelay = millis();
  }
}

void readUltrasonicSensors()
{
  pinMode(trig , OUTPUT);
  digitalWrite(trig , LOW);
  delayMicroseconds(2);
  digitalWrite(trig , HIGH);
  delayMicroseconds(5);
  digitalWrite(trig , LOW);
  
  pinMode(echo , INPUT);
  ultraDuration = pulseIn(echo , HIGH);
  ultraDistance = microsecondsToCentimeters(ultraDuration);
  /*if (ultraDistance>200)
  {
    ultraDistance = 200;
  }*/
  Serial.println(ultraDistance);
  delay(100);
  //Serial.println();
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}
