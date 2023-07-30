from machine import Pin, ADC, PWM
import time

travao = Pin(22, Pin.OUT)
joystick1 = Pin(18, Pin.IN, Pin.PULL_UP)
joystick2 = Pin(19, Pin.IN, Pin.PULL_UP)
sensor1 = Pin(9, Pin.IN, Pin.PULL_UP)
sensor2 = Pin(14, Pin.IN, Pin.PULL_UP)

#controlador motor
subir = PWM(Pin(6,mode=Pin.OUT))
descer = PWM(Pin(7,mode=Pin.OUT))
subir.freq(1000)
descer.freq(1000)
direccao1 = Pin(0, Pin.OUT) 
direccao1.value(1)

sensorIman1=1
sensorIman2=1
tempoParado=2
tempoComando=1
tempoTravao=0.5
travao.value(0)

#lê estados dos sensores antes de iniciar, se existirem e
try:
    with open('sensorIman1.json', 'r') as f:
        data = json.load(f)
        print (data["sensorIman1"])
        sensorIman1=data["sensorIman1"]
except:
    print("sem dados no ficheiro")
    
try:
    with open('sensorIman2.json', 'r') as f:
        data = json.load(f)
        print (data["status"])
        sensorIman2=data["sensorIman2"]
except:
    print("sem dados no ficheiro")
    
    
    
while True:
    
    if sensor1.value()==0:
        if sensorIman1==1:
            sensorIman1=0
            gravaEstadoSensor(SensorIman1, 0)
            print("---Sensor iman 1 Parou" + str(sensorIman1))
            time.sleep(tempoParado)
        else:
            sensorIman1=1
            gravaEstadoSensor(sensorIman1, 1)
            print("---Sensor iman 1 Continua" + str(sensorIman1))
            time.sleep(tempoParado)
    
    if sensor2.value()==0:
        if sensorIman2==1:
            sensorIman2=0
            gravaEstadoSensor(sensorIman2, 0)
            print("---Sensor iman 2 Parou" + str(sensorIman2))
            time.sleep(tempoParado)
        else:
            sensorIman2=1
            gravaEstadoSensor(sensorIman2, 1)
            print("---Sensor iman 2 Continua" + str(sensorIman2))
            time.sleep(tempoParado)
      
      
    if joystick1.value()==0 and sensorIman1==1:
        travao.value(1) #destrava
        print("Destrava") #avança
        time.sleep(tempoTravao)
        print("Estore Sobe") #avança
        subir.duty_u16(25000)
        time.sleep(tempoComando)
        
    elif joystick2.value()==0 and sensorIman2==1:
        travao.value(1)
        print("Destrava") #avança
        time.sleep(tempoTravao)
        print("Estore Desce")
        descer.duty_u16(18000)
        time.sleep(tempoComando)
        
    else:
        print("Estore parado")
        subir.duty_u16(0)
        descer.duty_u16(0)
        time.sleep(tempoTravao)
        travao.value(0)
        print("Travão bloqueado")
        time.sleep(tempoComando)
        #print("---Sensor iman 1 " + str(iman))
        #print("---Sensor iman 2 " + str(sensorIman2))



def gravaEstadoSensor(sensor, estado)
    ledState={sensor : estado}
    with open(sensor + '.json', 'w') as f:
        json.dump(ledState, f)