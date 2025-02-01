float duration, distance;  
int length = 2;
int modules[2][3] = {
  {2, 4, 5},
  {3, 6, 7},
};

int already_sent = -1;

void setup() {
  Serial.begin(9600);
  
  for(int i = 0; i < length; i++) {
    pinMode(modules[i][0], INPUT);
    pinMode(modules[i][1], OUTPUT);
    pinMode(modules[i][2], OUTPUT);
  }
}

void loop() {
  for(int i = 0; i < length; i++) {
    for(int k = 1; k < 3; k++) {
      //Serial.println(modules[i][k]);
      digitalWrite(modules[i][k], LOW);  
      delayMicroseconds(2);  
      digitalWrite(modules[i][k], HIGH);  
      delayMicroseconds(10);  
      digitalWrite(modules[i][k], LOW);  

      duration = pulseIn(modules[i][0], HIGH);
      distance = (duration*.0343)/2;  

      //Serial.println(distance);
      //Serial.println();

      int note = i + k;
      /*Serial.print("Note: ");
      Serial.print(note);
      Serial.print(" Distance: ");
      Serial.print(distance);
      Serial.println();*/

      if(distance < 50 && note != already_sent) {
        already_sent = note;
        Serial.print("play_note ");
        Serial.print(note);
        Serial.println();
      }

      delay(10);
    }
  }
}

