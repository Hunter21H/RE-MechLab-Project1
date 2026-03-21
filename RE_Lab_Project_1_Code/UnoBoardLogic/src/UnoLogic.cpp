
#include <Arduino.h>
//Set cathode interface
int a = 6;
int b = 7;
int c = 8;
int d = 9;
int e = 10;
int f = 11;
int g = 12;
int dp = 13;
//Set anode interface
int d4 = 5;
int d3 = 2;
int d2 = 3;
int d1 = 4;
// time set up
unsigned long previousMillis = 0;
const long interval = 1000;
unsigned long t = 0;




int Dp1 = 0;
int Dp2 = 0;
int Dp3 = 0;
int Dp4 = 0;

void setup()
{
    Serial.begin(9600);
    pinMode(d1, OUTPUT);
    pinMode(d2, OUTPUT);
    pinMode(d3, OUTPUT);
    pinMode(d4, OUTPUT);
    pinMode(a, OUTPUT);
    pinMode(b, OUTPUT);
    pinMode(c, OUTPUT);
    pinMode(d, OUTPUT);
    pinMode(e, OUTPUT);
    pinMode(f, OUTPUT);
    pinMode(g, OUTPUT);
    pinMode(dp, OUTPUT);
    Serial.begin(9600);
    randomSeed(analogRead(0));
}

void loop()
{

  
    piListener();

    Display(1, Dp1);
    Display(2, Dp2);
    Display(3, Dp3);
    Display(4, Dp4);

}


void piListener()
{
    if(Serial.available()>0)
    {
        char data = Serial.read();
        //rolling numbers
        if(data == 'r')
        {
            DisplayRollAni();
            //Sends randomized numbers back to Pi
            Serial.println(String(Dp1)+","+String(Dp2)+","+String(Dp3)+","+String(Dp4)+"/n");
        }
    
    
    }
}



void DisplayRollAni()
{

     
    //time loop for 10 seconds
    while (t < 10000)
    {
        Dp1 = random(0, 9);
        Dp2 = random(0, 9);
        Dp3 = random(0, 9);
        Dp4 = random(0, 9);
        for (int i = 0; i<20; ) {
          Display(1, Dp1);
          Display(2, Dp2);
          Display(3, Dp3);
          Display(4, Dp4);
          i++;
        }
        //ten second timer
        unsigned long currentMillis = millis();
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          }
      t = currentMillis;

            }


}

void DigitSel(unsigned char n)//
{
    switch (n)
    {
    case 1:
        digitalWrite(d1, HIGH);
        digitalWrite(d2, LOW);
        digitalWrite(d3, LOW);
        digitalWrite(d4, LOW);
        break;
    case 2:
        digitalWrite(d1, LOW);
        digitalWrite(d2, HIGH);
        digitalWrite(d3, LOW);
        digitalWrite(d4, LOW);
        break;
    case 3:
        digitalWrite(d1, LOW);
        digitalWrite(d2, LOW);
        digitalWrite(d3, HIGH);
        digitalWrite(d4, LOW);
        break;
    case 4:
        digitalWrite(d1, LOW);
        digitalWrite(d2, LOW);
        digitalWrite(d3, LOW);
        digitalWrite(d4, HIGH);
        break;
    default:
        digitalWrite(d1, LOW);
        digitalWrite(d2, LOW);
        digitalWrite(d3, LOW);
        digitalWrite(d4, LOW);
        break;
    }
}
void Num_0()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, LOW);
    digitalWrite(g, HIGH);
    digitalWrite(dp, HIGH);
}
void Num_1()
{
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, HIGH);
    digitalWrite(g, HIGH);
    digitalWrite(dp, HIGH);
}
void Num_2()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, HIGH);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, HIGH);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_3()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, HIGH);
    digitalWrite(f, HIGH);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_4()
{
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_5()
{
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, HIGH);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_6()
{
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_7()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, HIGH);
    digitalWrite(g, HIGH);
    digitalWrite(dp, HIGH);
}
void Num_8()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, LOW);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Num_9()
{
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
    digitalWrite(c, LOW);
    digitalWrite(d, LOW);
    digitalWrite(e, HIGH);
    digitalWrite(f, LOW);
    digitalWrite(g, LOW);
    digitalWrite(dp, HIGH);
}
void Clear()  // Clear the screen
{
    digitalWrite(a, HIGH);
    digitalWrite(b, HIGH);
    digitalWrite(c, HIGH);
    digitalWrite(d, HIGH);
    digitalWrite(e, HIGH);
    digitalWrite(f, HIGH);
    digitalWrite(g, HIGH);
    digitalWrite(dp, HIGH);
}
void pickNumber(unsigned char n)//Choose the number of
{
    switch (n)
    {
    case 0:Num_0();
        break;
    case 1:Num_1();
        break;
    case 2:Num_2();
        break;
    case 3:Num_3();
        break;
    case 4:Num_4();
        break;
    case 5:Num_5();
        break;
    case 6:Num_6();
        break;
    case 7:Num_7();
        break;
    case 8:Num_8();
        break;
    case 9:Num_9();
        break;
    default:Clear();
        break;
    }
}
void Display(unsigned char x, unsigned char Number)//Show that x is the coordinate, Number is the number
{
    DigitSel(x);
    pickNumber(Number);
    delay(1);
    Clear(); //Vanishing
}