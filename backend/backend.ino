float duration, distance;  
int length = 2;
int modules[2][3] = {
  {2, 3, 4},
  {5, 6, 7},
};

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

      if(distance < 50) {
        int note = i + k;
        Serial.println("    play_note " + i + k);
      }

      delay(100);
    }
  }
}
