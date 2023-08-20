from mkdisk import MkDisk
from rmdisk import RmDisk
from rep import reporte
from fdisk import FDisk
def main():
    disk = MkDisk()
    disk.fit= 'FF'
    disk.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    disk.size = 10
    disk.unit = 'M'
    disk.create()

    rm = RmDisk()
    rm.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    rm.remove()

    repo = reporte()
    repo.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    repo.rep()

    partition = FDisk()
    partition.size = 2
    partition.type = 'p'
    partition.unit = 'M'
    partition.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    partition.name = 'particion1'
    partition.fit = 'ff'
    partition.fdisk()

    repo = reporte()
    repo.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    repo.rep()
    pass

if __name__ == '__main__':
    main()