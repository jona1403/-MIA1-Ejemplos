import os
class RmDisk:
    def __init__(self):
        self.path = ''

    def remove(self):


        if self.path:
            if self.path.startswith("\"") and self.path.endswith("\""):
                self.path = self.path[1:-1]

            try:
                if os.path.isfile(self.path):
                    if not self.path.endswith(".dk"):
                        print("\tERROR: Extensión de archivo no válida para la eliminación del Disco.") 

                    confirmation = input("Esta seguro que desea eliminar el disco? Y/N: \n")
                    
                    if  confirmation == 'Y':
                        os.remove(self.path)
                        print("\t>>>> RMDISK: Disco eliminado exitosamente <<<<") 
                    else:
                        print("\t>>>> RMDISK: Eliminación del disco cancelada correctamente <<<<") 
                else:
                    print("\tERROR: El disco no existe en la ruta indicada.") 
            except Exception as e:
                print("\tERROR: Error al intentar eliminar el disco: "+str(e)) 