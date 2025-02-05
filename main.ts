radio.onReceivedString(function (receivedString) {
    parts = receivedString.split(",")
    if (parts.length == 4) {
        setMotor(enumLeftFront, parseFloat(parts[0]))
        setMotor(enumRightFront, parseFloat(parts[1]))
        setMotor(enumLeftRear, parseFloat(parts[2]))
        setMotor(enumRightRear, parseFloat(parts[3]))
    }
})
function setMotor (motor: number, speed: number) {
    speed = Math.constrain(speed, -255, 255)
    if (motor == enumLeftFront) {
        SuperBit.MotorRun(SuperBit.enMotors.M1, speed)
    } else if (motor == enumRightFront) {
        SuperBit.MotorRun(SuperBit.enMotors.M3, speed)
    } else if (motor == enumLeftRear) {
        SuperBit.MotorRun(SuperBit.enMotors.M2, speed)
    } else if (motor == enumRightRear) {
        SuperBit.MotorRun(SuperBit.enMotors.M4, speed)
    }
}
let speed = 0
let parts: string[] = []
let enumRightRear = 0
let enumLeftRear = 0
let enumRightFront = 0
let enumLeftFront = 0
enumLeftFront = 0
basic.showIcon(IconNames.Heart)
radio.setGroup(1)
radio.setTransmitPower(7)
enumRightFront = 1
enumLeftRear = 2
enumRightRear = 3
SuperBit.MotorRun(SuperBit.enMotors.M1, 0)
SuperBit.MotorRun(SuperBit.enMotors.M2, 0)
SuperBit.MotorRun(SuperBit.enMotors.M3, 0)
SuperBit.MotorRun(SuperBit.enMotors.M4, 0)
