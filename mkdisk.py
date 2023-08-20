from structs import Particion, MBR
import os
import random
import time
class MkDisk:
    def __init__(self):
        self.size= 0
        self.fit = ''
        self.unit = ''
        self.path = ''

    def validateData():
        pass

    def create(self):
        disco = MBR()
        try:
            size = int(self.size)
            if size <= 0:
                print("\tERROR: El parámetro size del comando MKDISK debe ser mayor a 0")
                return

            if self.unit == "M":
                size = 1024 * 1024 * size
            elif self.unit == "K":
                size = 1024 * size

            f = self.fit[0].upper()
            disco.mbr_tamano = size
            disco.mbr_fecha_creacion = int(time.time())
            disco.disk_fit = f
            disco.mbr_disk_signature = random.randint(1, 9999)

            if os.path.exists(self.path):
                print("\tERROR: Disco ya existente en la ruta: "+self.path)
                return

            folder_path = os.path.dirname(self.path)
            os.makedirs(folder_path, exist_ok=True)

            disco.mbr_Partition_1 = Particion()
            disco.mbr_Partition_2 = Particion()
            disco.mbr_Partition_3 = Particion()
            disco.mbr_Partition_4 = Particion()

            if self.path.startswith("\""):
                self.path = self.path[1:-1]

            if not self.path.endswith(".dk"):
                print("\tERROR: Extensión de archivo no válida para la creación del Disco.")
                return

            try:
                with open(self.path, "w+b") as file:
                    file.write(b"\x00")
                    file.seek(size - 1)
                    file.write(b"\x00")
                    file.seek(0)
                    file.write(bytes(disco))
                print("\t>>>> MKDISK: Disco creado exitosamente <<<<")
            except Exception as e:
                print(e)
                print("\tERROR: Error al crear el disco en la ruta: "+self.path)
        except ValueError:
            print("\tERROR: El parámetro size del comando MKDISK debe ser un número entero")