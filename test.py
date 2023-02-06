from pyModbusTCP.client import ModbusClient
import struct

def to_float(response):
    a = response[0]
    b = response[1]
    return struct.unpack('>f', bytes.fromhex(f"{a:0>4x}" + f"{b:0>4x}"))[0]

c = ModbusClient(host="ew11.local", auto_open=True, auto_close=True, unit_id=1)                                                                                                                                                             1)

regs = c.read_input_registers(0x0,2)

if regs:
    print(to_float(regs))

regs = c.read_input_registers(0x6,2)

if regs:
    print(to_float(regs))

regs = c.read_input_registers(0xC,2)

if regs:
    print(to_float(regs))
