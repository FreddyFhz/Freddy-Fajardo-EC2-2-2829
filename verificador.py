import sys
import filecmp

def verificar_archivos(origen_file, descomprimido_file):
    if filecmp.cmp(origen_file, descomprimido_file):
        return "ok"
    else:
        return "nok"

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Uso: python verificador.py archivo_original.txt archivo_descomprimido.txt")
    else:
        archivo_original = sys.argv[1]
        archivo_descomprimido = sys.argv[2]
        resultado = verificar_archivos(archivo_original, archivo_descomprimido)
        print(resultado)