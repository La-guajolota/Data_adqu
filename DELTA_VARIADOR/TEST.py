from pymodbus.client import ModbusTcpClient

# Dirección IP del dispositivo Modbus TCP
SERVER_IP = '192.168.1.100'
# Puerto del dispositivo Modbus TCP (generalmente es 502)
SERVER_PORT = 502

# Dirección del registro desde el cual leeremos datos
REGISTER_ADDRESS = 0
# Cantidad de registros a leer
NUM_REGISTERS = 10

# Crear un cliente Modbus TCP
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

try:
    # Conectar al dispositivo
    client.connect()

    # Leer datos de los registros
    result = client.read_holding_registers(REGISTER_ADDRESS, NUM_REGISTERS, unit=1)
    
    # Verificar si la lectura fue exitosa
    if result.isError():
        print("Error al leer los registros:", result)
    else:
        # Imprimir los valores leídos
        print("Valores leídos:", result.registers)

finally:
    # Cerrar la conexión
    client.close()
