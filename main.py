from smbus2 import SMBus

# Open the BUS number 1, i2c has multiple
with SMBus(1) as BUS:
    data = BUS.read_i2c_block_data(
        # addr found in datasheet
        i2c_addr=80,
        register=0,
        length=16,
    )
    print(data)
