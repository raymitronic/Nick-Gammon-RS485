import serial
import rs485

# Open non-blocking port
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0, rtscts=True)
rs485 = rs485.SerialWrapper(port)

while True:
    if rs485.update():
        packet = rs485.getPacket
        print(len(packet), " bytes received\n".encode())
        print(packet)
