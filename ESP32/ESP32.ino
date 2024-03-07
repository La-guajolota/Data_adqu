int v1 = 120;
int v2 = 122;
int v3 = 123;

char buff[40];
String command;
String action;
String value;

String Getvalue(String data,char separador,int index){
  int found = 0;
  int strIndex[] = {0,1}
  int maxIndex = data.length()-1;

  for(int i=0, i<=maxIndex && found<= index; i++){
    if(data.charAt(i)==separador||i==maxIndex){
      found++;
      stdIndex[0] = strIndex[1]+1;
      strIndex[1] = (i == maxIndex) ? i+1 i;
    }
  }
  return found>index ? data.substring(strIndex[0],stdIndex[1]) : "";
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(20);
  Serial.println("ok");
}

void loop() {
  while(!Serial.available()){
    if(Serial.available()){
      command = Serial.readString();
      if(command.length()>0){
        action = getValue(command,":",0);
        switchValue = getValue(command,":",1);
        value = getValue(command,":",2);

        if(action.equals("get")){
          if(switchValue.equal("all")){
            sprintf(buff,"v1,%d:v2,%d:,v3,%d:",v1,v2,v3);
            serial.println(buff);
          }
        }
      }
    }
  }
}
