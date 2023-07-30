from machine import Pin, ADC, PWM
import time

#direccao1
direccao1 = Pin(0, Pin.OUT) 
pwm1 = PWM(Pin(6,mode=Pin.OUT))

pwm1.freq(1000)
direccao1.value(1)

pwm1.duty_u16(15000)
time.sleep(2)
pwm1.duty_u16(0)


direccao2 = Pin(1, Pin.OUT) 
pwm2 = PWM(Pin(7,mode=Pin.OUT))

pwm2.freq(1000)
direccao2.value(1)

pwm2.duty_u16(15000)
time.sleep(2)
pwm2.duty_u16(0)