#define LED_BUILTIN 2
void setup() {
  pinMode(12,INPUT);  // pin for data_in. 
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

// infinite loop that checks for sensor data.
void loop() {
  bool pirsensor = digitalRead(12);
  if (pirsensor){
    digitalWrite(LED_BUILTIN, HIGH);   
    Serial.println("1");
    delay(250);}
  else{
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("0"); 
    delay(500);}   
}
