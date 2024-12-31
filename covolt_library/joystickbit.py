from microbit import *
import utime 

class JoystickBitPin:  
    P12 = 12  
    P13 = 13  
    P14 = 14  
    P15 = 15  
  
class RockerType:  
    X = 1  
    Y = 2  
  
ButtonType = {  
    'down': 0, 
    'up': 1     
}  

class JOYSTICKBIT(object):
      """基本描述

      joystick游戏手柄

      """ 
      def init_joystick_bit(self):  
            pin0.write_digital(0)
            
            pin12.set_pull(pin12.PULL_UP) 
            pin13.set_pull(pin13.PULL_UP) 
            pin14.set_pull(pin14.PULL_UP)   
            pin15.set_pull(pin15.PULL_UP)  
            
            pin16.write_digital(1) 
      
      def get_button(self,button):  
          pin = 1
          if button == JoystickBitPin.P12:
              pin12.set_pull(pin12.PULL_UP)
              pin = pin12.read_digital()
          elif button == JoystickBitPin.P13:
              pin13.set_pull(pin13.PULL_UP)
              pin = pin13.read_digital()
          elif button == JoystickBitPin.P14:
              pin14.set_pull(pin14.PULL_UP)
              pin = pin14.read_digital()
          elif button == JoystickBitPin.P15:
              pin15.set_pull(pin15.PULL_UP)
              pin = pin15.read_digital()
          return not pin 
                
      def on_button_event(self,button, event_type, handler):  
            if JOYSTICKBIT.get_button(self,button) == (event_type == ButtonType['down']):  
                  handler()  
         
      def get_rocker_value(self,rocker):  
            if rocker == RockerType.X:
                  return pin1.read_analog()  
            elif rocker == RockerType.Y: 
                  return pin2.read_analog() 
            else:  
                  return 0  
       
      def vibration_motor(self,time_ms): 
              
            pin16.write_digital(0)   
            utime.sleep_ms(time_ms)   
            pin16.write_digital(1)  
            

joystickbit = JOYSTICKBIT()


if __name__ == '__main__':
     
      joystickbit.init_joystick_bit()
      # JOYSTICKBIT.get_button(JoystickBitPin.P12)
      # JOYSTICKBIT.on_button_event(JoystickBitPin.P12,ButtonType['down'],lambda: print("Button P12 pressed!"))
      # JOYSTICKBIT.get_rocker_value(RockerType.X)
      # JOYSTICKBIT.vibration_motor(100)