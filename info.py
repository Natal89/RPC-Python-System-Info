import psutil
import platform
from datetime import datetime
# import cpuinfo
import socket
import uuid
import re


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_information():
    results = ""

    print("="*40, "System Information", "="*40)
    results = results+ "="*40 + "System Information"+ "="*40 + "\n"
    uname = platform.uname()
    print(f"System: {uname.system}")
    results = results+ f"System: {uname.system}"+"\n"
    print(f"Node Name: {uname.node}")
    results = results+ f"Node Name: {uname.node}"+ "\n"
    print(f"Release: {uname.release}")
    results = results+ f"Release: {uname.release}"+ "\n"
    print(f"Version: {uname.version}")
    results = results+ f"Version: {uname.version}"+ "\n"
    print(f"Machine: {uname.machine}")
    results = results+ f"Machine: {uname.machine}"+ "\n"
    print(f"Processor: {uname.processor}")
    results = results+ f"Processor: {uname.processor}"+ "\n"
    # print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")
    results = results+ f"Ip-Address: {socket.gethostbyname(socket.gethostname())}"+ "\n"
    print(f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")
    results = results+ f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}"+ "\n"


    # Boot Time
    print("="*40, "Boot Time", "="*40)
    results = results + "="*40+ "Boot Time"+ "="*40+ "\n"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    results = results+ f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"+ "\n"


    # print CPU information
    print("="*40, "CPU Info", "="*40)
    results = results+ "="*40+ "CPU Info"+ "="*40+ "\n"
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    results = results+ "Physical cores:"+ str(psutil.cpu_count(logical=False))+ "\n"
    print("Total cores:", psutil.cpu_count(logical=True))
    results = results+ "Total cores:"+ str(psutil.cpu_count(logical=True))+ "\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    results = results+ f"Max Frequency: {cpufreq.max:.2f}Mhz"+ "\n"
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    results = results+ "="*40+ f"Min Frequency: {cpufreq.min:.2f}Mhz"+ "\n"
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    results = results+ "="*40+ f"Current Frequency: {cpufreq.current:.2f}Mhz"+ "\n"
    # CPU usage
    print("CPU Usage Per Core:")
    results = results+ "CPU Usage Per Core:"+ "\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
        results = results+ f"Core {i}: {percentage}%"+ "\n"
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    results = results+ f"Total CPU Usage: {psutil.cpu_percent()}%"+ "\n"


    # Memory Information
    print("="*40, "Memory Information", "="*40)
    results = results+ "="*40+ "Memory Information"+ "="*40+ "\n"
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    results = results+ f"Total: {get_size(svmem.total)}"+ "\n"
    print(f"Available: {get_size(svmem.available)}")
    results = results+ f"Available: {get_size(svmem.available)}"+ "\n"
    print(f"Used: {get_size(svmem.used)}")
    results = results+ f"Used: {get_size(svmem.used)}"+ "\n"
    print(f"Percentage: {svmem.percent}%")
    results = results+ f"Percentage: {svmem.percent}%"+ "\n"



    print("="*20, "SWAP", "="*20)
    results = results+ "="*20+ "SWAP"+ "="*20+ "\n"
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    results = results+ f"Total: {get_size(swap.total)}"+ "\n"
    print(f"Free: {get_size(swap.free)}")
    results = results+ f"Free: {get_size(swap.free)}"+ "\n"
    print(f"Used: {get_size(swap.used)}")
    results = results+ f"Used: {get_size(swap.used)}"+ "\n"
    print(f"Percentage: {swap.percent}%")
    results = results+ f"Percentage: {swap.percent}%"+ "\n"



    # Disk Information
    print("="*40+ "Disk Information"+ "="*40)
    results = results+ "="*40+ "Disk Information"+ "="*40+ "\n"
    print("Partitions and Usage:")
    results = results+ "Partitions and Usage:"+ "\n"
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        results = results+ f"=== Device: {partition.device} ==="+ "\n"
        print(f"  Mountpoint: {partition.mountpoint}")
        results = results+f"  Mountpoint: {partition.mountpoint}"+ "\n"
        print(f"  File system type: {partition.fstype}")
        results = results+ f"  File system type: {partition.fstype}"+ "\n"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        results = results+ f"  Total Size: {get_size(partition_usage.total)}" "\n"
        print(f"  Used: {get_size(partition_usage.used)}")
        results = results+ f"  Used: {get_size(partition_usage.used)}"+ "\n"
        print(f"  Free: {get_size(partition_usage.free)}")
        results = results+ f"  Free: {get_size(partition_usage.free)}"+ "\n"
        print(f"  Percentage: {partition_usage.percent}%")
        results = results+ f"  Percentage: {partition_usage.percent}%"+ "\n"
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    results = results+ f"Total read: {get_size(disk_io.read_bytes)}"+ "\n"
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    results = results+f"Total write: {get_size(disk_io.write_bytes)}"+ "\n"

    ## Network information
    print("="*40, "Network Information", "="*40)
    results = results+"="*40+ "Network Information"+ "="*40+ "\n"
    ## get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            results = results+ f"=== Interface: {interface_name} ==="+ "\n"
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                results = results+f"  IP Address: {address.address}"+ "\n"
                print(f"  Netmask: {address.netmask}")
                results = results+ f"  Netmask: {address.netmask}"+ "\n"
                print(f"  Broadcast IP: {address.broadcast}")
                results = results+ f"  Broadcast IP: {address.broadcast}"+ "\n"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                results = results+ f"  MAC Address: {address.address}"+ "\n"
                print(f"  Netmask: {address.netmask}")
                results = results+ f"  Netmask: {address.netmask}"+ "\n"
                print(f"  Broadcast MAC: {address.broadcast}")
                results = results+ f"  Broadcast MAC: {address.broadcast}"+ "\n"
    ##get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    results = results+ f"Total Bytes Sent: {get_size(net_io.bytes_sent)}"+ "\n"
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    results = results+ f"Total Bytes Received: {get_size(net_io.bytes_recv)}"+ "\n"
   
    return results


