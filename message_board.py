import serial

def enum(**enums):
    return type('Enum', (), enums)

MessageTypes = enum(Text = 1, Color = 2, MessageTimeMS = 3)

class MessageBoard:
  def start(self, port = '/dev/ttyACM0', baud = 9600):
    self.serialPort = serial.Serial(port, baud)

  def sendMessage(self, type, message):
    self.serialPort.write(str(type) + ',' + str(message) + ';')

  def setColor(self, r, g, b):
    self.sendMessage(MessageTypes.Color, str(r) + ',' + str(g) + ',' + str(b))

  def setText(self, text):
    self.sendMessage(MessageTypes.Text, text) 

  def setMessageTime(self, timems):
    self.sendMessage(MessageTypes.MessageTimeMS, timems)
