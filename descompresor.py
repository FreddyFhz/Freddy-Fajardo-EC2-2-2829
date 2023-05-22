import sys
import os

def decompress_lzw(input_file):
    output_extension = ".txt"
    output_file = "descomprimido" + output_extension

    # Leer el contenido del archivo comprimido
    with open(input_file, 'rb') as file:
        compressed_data = file.read()

    # Inicializar el diccionario con caracteres individuales
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256

    decompressed_data = []
    code = int.from_bytes(compressed_data[:2], 'big')
    compressed_data = compressed_data[2:]
    decompressed_data.append(dictionary[code])

    # Algoritmo LZW de descompresión
    current_string = dictionary[code]
    while len(compressed_data) > 0:
        code = int.from_bytes(compressed_data[:2], 'big')
        compressed_data = compressed_data[2:]

        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_string + current_string[0]
        else:
            raise ValueError("Error de descompresión: código inválido")

        decompressed_data.append(entry)
        dictionary[next_code] = current_string + entry[0]
        next_code += 1
        current_string = entry

    # Escribir los datos descomprimidos en el archivo de salida
    with open(output_file, 'w') as file:
        for entry in decompressed_data:
            file.write(entry)

    print("Descompresión completada.")
    print(f"Archivo descomprimido: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python descompresor.py archivo_comprimido.ELMEJORPROFESOR")
    else:
        input_file = sys.argv[1]
        decompress_lzw(input_file)
