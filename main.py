def stopCar():
    global carSpeed
    carSpeed = 0
    carMove(carSpeed, carSpeed, carSpeed, carSpeed)
def carMove(m1Speed: number, m2Speed: number, m3Speed: number, m4Speed: number):
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, m1Speed, SuperBit.enMotors.M2, m2Speed)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, m3Speed, SuperBit.enMotors.M4, m4Speed)
def showLed(ledNo: number, _brightness: number):
    SuperBit.RGB_Program().set_pixel_color(ledNo, neopixel.colors(NeoPixelColors.RED))
    SuperBit.RGB_Program().set_brightness(_brightness)
    SuperBit.RGB_Program().show()
# 判断是否前进
def isAdvance(joystickValue: number):
    return joystickValue > max_joystick_travel

def on_received_value(name, value):
    global realMotorSpeed, m1Speed2, m2Speed2, m3Speed2, m4Speed2
    realMotorSpeed = getSpeed(value)
    if realMotorSpeed != 0:
        if name == "left_y":
            showLed(0, realMotorSpeed)
            if not (isAdvance(value)):
                realMotorSpeed = 0 - realMotorSpeed
            m1Speed2 = realMotorSpeed
            m2Speed2 = realMotorSpeed
            m3Speed2 = realMotorSpeed
            m4Speed2 = realMotorSpeed
        carMove(m1Speed2, m2Speed2, m3Speed2, m4Speed2)
    else:
        basic.show_icon(IconNames.SQUARE)
        SuperBit.RGB_Program().clear()
        stopCar()
radio.on_received_value(on_received_value)

def getSpeed(joystickValue2: number):
    global max_motor_speed, mSpeed
    max_motor_speed = 255
    if joystickValue2 > 130:
        mSpeed = (joystickValue2 - max_joystick_travel) / max_joystick_travel * max_motor_speed
    elif joystickValue2 < 126:
        mSpeed = (max_joystick_travel - joystickValue2) / max_joystick_travel * max_motor_speed
    else:
        mSpeed = 0
    return mSpeed
mSpeed = 0
max_motor_speed = 0
m4Speed2 = 0
m3Speed2 = 0
m2Speed2 = 0
realMotorSpeed = 0
carSpeed = 0
m1Speed2 = 0
max_joystick_travel = 0
max_joystick_travel = 128
m1Speed2 = 0
radio.set_group(10)
radio.set_transmit_power(7)
basic.show_icon(IconNames.HEART)

def on_in_background():
    control.raise_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
        EventBusValue.MICROBIT_EVT_ANY)
control.in_background(on_in_background)
