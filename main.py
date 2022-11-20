from smbus2 import SMBus

# Open the BUS number 1, i2c has multiple
with SMBus(1) as BUS:
    data = BUS.read_byte_data(
        # addr found in datasheet
        0x0,
        0,
    )
    print(data)
