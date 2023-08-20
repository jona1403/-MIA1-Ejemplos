import struct

class Particion:
    def __init__(self):
        self.part_status = '0'
        self.part_type = 'P'
        self.part_fit = 'BF'
        self.part_start = 0
        self.part_size = 0
        self.part_name = ''

    def __bytes__(self):
        return (self.part_status.encode('utf-8') +
                self.part_type.encode('utf-8') +
                self.part_fit.encode('utf-8') +
                struct.pack("<i", self.part_start) +
                struct.pack("<i", self.part_size) +
                self.part_name.ljust(16, '\0').encode('utf-8'))
    
    def __setstate__(self, data):
        self.part_status = data[:1].decode('utf-8')
        self.part_type = data[1:2].decode('utf-8')
        self.part_fit = data[2:3].decode('utf-8')
        self.part_start = struct.unpack("<i", data[3:7])[0]
        self.part_size = struct.unpack("<i", data[7:11])[0]
        self.part_name = data[11:27].decode('utf-8').rstrip('\0')

class MBR:
    def __init__(self):
        self.mbr_tamano = 0
        self.mbr_fecha_creacion = 0
        self.mbr_disk_signature = 0
        self.disk_fit = 'FF'  # Valor por defecto: First Fit
        self.mbr_Partition_1 = Particion()
        self.mbr_Partition_2 = Particion()
        self.mbr_Partition_3 = Particion()
        self.mbr_Partition_4 = Particion()

    def __bytes__(self):
        return (struct.pack("<i", self.mbr_tamano) +
                struct.pack("<i", self.mbr_fecha_creacion) +
                struct.pack("<i", self.mbr_disk_signature) +
                self.disk_fit.encode('utf-8') +
                bytes(self.mbr_Partition_1) +
                bytes(self.mbr_Partition_2) +
                bytes(self.mbr_Partition_3) +
                bytes(self.mbr_Partition_4))
    
class Transition:
    def __init__(self):
        self.partition = 0
        self.start = 0
        self.end = 0
        self.before = 0
        self.after = 0

    def __bytes__(self):
        return struct.pack("<5i", self.partition, self.start, self.end, self.before, self.after)


class EBR:
    def __init__(self):
        self.part_status = '0'
        self.part_fit = ''
        self.part_start = 0
        self.part_size = 0
        self.part_next = -1
        self.part_name = ''
    
    def __bytes__(self):
        return (self.part_status.encode('utf-8') +
                self.part_fit.encode('utf-8') +
                struct.pack("<i", self.part_start) +
                struct.pack("<i", self.part_size) +
                struct.pack("<i", self.part_next) +
                self.part_name.encode('utf-8').ljust(16, b'\x00'))

    def __setstate__(self, data):
        self.part_status = data[:1].decode('utf-8')
        self.part_fit = data[1:2].decode('utf-8')
        self.part_start = struct.unpack("<i", data[2:6])[0]
        self.part_size = struct.unpack("<i", data[6:10])[0]
        self.part_next = struct.unpack("<i", data[10:14])[0]
        self.part_name = data[14:30].decode('utf-8').rstrip('\0')
