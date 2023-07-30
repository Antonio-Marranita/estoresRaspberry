from machine import Pin, ADC, PWM
import time

travao = Pin(9, Pin.OUT)
button1 = Pin(18, Pin.IN, Pin.PULL_UP)
button2 = Pin(19, Pin.IN, Pin.PULL_UP)

button4 = Pin(5, Pin.IN, Pin.PULL_UP)

#controlador motor
subir = PWM(Pin(6,mode=Pin.OUT))
descer = PWM(Pin(7,mode=Pin.OUT))
subir.freq(1000)
descer.freq(1000)
direccao1 = Pin(0, Pin.OUT) 
direccao1.value(1)

iman=1
iman2=1
tempoParado=1
tempoComando=0.1
tempoTravao=0.5
travao.value(0)

while True:
    
   
      
      
    if button1.value()==0 and iman==1:
        travao.value(1) #destrava
        print("Destrava") #avança
        time.sleep(tempoTravao)
        print("Estore Sobe") #avança
        subir.duty_u16(15000)
        time.sleep(tempoComando)
        
    elif button2.value()==0 and iman2==1:
        travao.value(1)
        print("Destrava") #avança
        time.sleep(tempoTravao)
        print("Estore Desce")
        descer.duty_u16(15000)
        time.sleep(tempoComando)
        
    else:
        print("Estore parado")
        time.sleep(tempoTravao)
        subir.duty_u16(0)
        descer.duty_u16(0)
        travao.value(0)
        print("Travão bloqueado")
        #time.sleep(tempoComando)
        #print("---Sensor iman 1 " + str(iman))
        #print("---Sensor iman 2 " + str(iman2))


