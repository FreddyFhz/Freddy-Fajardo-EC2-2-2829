import sys
import os
import numpy as np
from typing import List

def decompress_lzw(input_file: str) -> List[str]:
    output_extension = ".txt"
    output_file = "descomprimido" + output_extension

    # Leer el contenido del archivo comprimido
    compressed_data = np.load(input_file)

    # Inicializar el diccionario con caracteres individuales
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256

    decompressed_data = []
    code = compressed_data[0]
    decompressed_data.append(dictionary[code])

    # Algoritmo LZW de descompresión
    current_string = dictionary[code]
    for code in compressed_data[1:]:
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

    return decompressed_data


def verify_compression(original_file: str, decompressed_data: List[str]) -> str:
    with open(original_file, 'r') as file:
        original_text = file.read()

    if original_text == ''.join(decompressed_data):
        return "ok"
    else:
        return "nok"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python descompresor.py archivo_comprimido.ELMEJORPROFESOR")
    else:
        input_file = sys.argv[1]
        decompressed_data = decompress_lzw(input_file)
        verification_result = verify_compression(input_file[:-9], decompressed_data)
        print(f"Verificación: {verification_result}")
