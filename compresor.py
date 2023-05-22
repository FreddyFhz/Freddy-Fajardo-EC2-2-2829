import sys
import os

def compress_lzw(input_file):
    output_extension = ".ELMEJORPROFESOR"
    output_file = "archivo_comprimido" + output_extension

    # Leer el contenido del archivo de entrada
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Inicializar el diccionario con caracteres individuales
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256

    compressed_data = []
    current_string = input_text[0]

    # Algoritmo LZW de compresión
    for char in input_text[1:]:
        current_string_plus_char = current_string + char
        if current_string_plus_char in dictionary:
            current_string = current_string_plus_char
        else:
            compressed_data.append(dictionary[current_string])
            dictionary[current_string_plus_char] = next_code
            next_code += 1
            current_string = char

    compressed_data.append(dictionary[current_string])

    # Escribir los datos comprimidos en el archivo de salida
    with open(output_file, 'wb') as file:
        for code in compressed_data:
            file.write(code.to_bytes(2, 'big'))

    # Calcular la tasa de compresión
    input_size = os.path.getsize(input_file)
    output_size = os.path.getsize(output_file)
    compression_ratio = (output_size / input_size) * 100

    print("Compresión completada.")
    print(f"Tasa de compresión: {compression_ratio:.2f}%")
    print(f"Archivo comprimido: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compresor.py noto.txt")
    else:
        input_file = sys.argv[1]
        compress_lzw(input_file)
