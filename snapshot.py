#!/usr/bin/python3
# Создание снапшота виртуальной машины KVM...
# Импорт нужных модулей: time(время), argparse(синтаксический анализатор парам-ов командной строки,аргументов и суб-комманд), \
# libvirt(модуль дла работы с KVM), from lxml etree (lxml - библиотек для обработки xml и html файлов, \
# где **etree** - для созданиия элементов HTML/XML и их подэлементов), from lxml.builder E (фабрика элементов для создания XML-документов) 
# 
import time
import argparse
import libvirt
from lxml import etree
from lxml.builder import E


#Функция парсинга для аргмуентов и описания (указания имени машины и пути до имени девайса(путь до диска - например **vda**))
def parse_args():
    parser = argparse.ArgumentParser(description='Create snapshot for libvirt machine')
    parser.add_argument('--name', required=True, help='Machine name')
    parser.add_argument('--device', required=True, help='Device path (like vda)')
    return parser.parse_args()
    



#Подготовительная функция для создания снапшота, получение путей и имени для snapshot-а
def create_snapshot_node(disk_node):
    device = disk_node.xpath('/domain/devices/disk/target/@dev')[0]
    disk_path = disk_node.xpath('/domain/devices/disk/source/@file')[0]

    now = int(time.time())
    snap_path = disk_path.rsplit('.', 1)[0]
    snap_path = f'{snap_path}-{now}.snap'
    snap_name = snap_path.rsplit('/', 1)[1]

    snap = E.domainsnapshot()
    snap.append(E.name(snap_name))

    disks = E.disks()
    disk = E.disk(name=device)
    disk.append(E.source(file=snap_path))
    disks.append(disk)

    snap.append(disks)
    return snap

#Функция получения дисков по имени (с передачей параметро: vm и name)
def get_disk_by_name(vm, name):
    raw_xml = vm.XMLDesc(0)
    xml = etree.XML(raw_xml)
    disks = xml.xpath(f'/domain/devices/disk/target[@dev="{name}"]/..')
    return disks[0]

#Функция main() для подключение к qemy///system и создание снапшота в XML формате 
def main():
    args = parse_args()
    session = libvirt.open('qemu:///system')
    try:
        vm = session.lookupByName(args.name)
    except libvirt.libvirtError:
        print(f'Machine with name {args.name} not found!')
        session.close()
        return
    disk = get_disk_by_name(vm, args.device)
    snapshot = create_snapshot_node(disk)
    vm.snapshotCreateXML(etree.tostring(snapshot, encoding='unicode'),
            libvirt.VIR_DOMAIN_SNAPSHOT_CREATE_DISK_ONLY | libvirt.VIR_DOMAIN_SNAPSHOT_CREATE_ATOMIC)
    session.close()

if __name__ == '__main__':
    main()
