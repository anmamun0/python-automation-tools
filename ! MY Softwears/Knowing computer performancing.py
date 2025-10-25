import platform
import psutil

print("Operating System:", platform.system())
print("Platform:", platform.platform())
print("Processor:", platform.processor())
print("RAM:", round(psutil.virtual_memory().total / (1024.0 ** 3), 2), "GB")
print("Number of CPU Cores:", psutil.cpu_count())
print("CPU Frequency:", psutil.cpu_freq())


print('Here down all drive capacitys ')


import psutil
for partition in psutil.disk_partitions():
    if 'cdrom' in partition.opts or partition.fstype == '':
        # skip cd-rom drives with no disk in it; they may raise
        # ENOENT, pop-up a Windows GUI error for a non-ready
        # partition or just hang.
        continue
    print(f"Drive: {partition.device}")
    print(f"  Type: {partition.fstype}")
    print(f"  Mountpoint: {partition.mountpoint}")
    usage = psutil.disk_usage(partition.mountpoint)
    print(f"  Total: {usage.total / (1024.0 ** 3):.2f} GB")
    print(f"  Used: {usage.used / (1024.0 ** 3):.2f} GB")
    print(f"  Free: {usage.free / (1024.0 ** 3):.2f} GB")




# More
# import psutil
# import os
# import glob

# def count_files(extension):
#     return len(glob.glob1(partition.mountpoint, f"*.{extension}"))

# for partition in psutil.disk_partitions():
#     if 'cdrom' in partition.opts or partition.fstype == '':
#         continue
#     print(f"Drive: {partition.device}")
#     print(f"  Type: {partition.fstype}")
#     print(f"  Mountpoint: {partition.mountpoint}")
#     usage = psutil.disk_usage(partition.mountpoint)
#     print(f"  Total: {usage.total / (1024.0 ** 3):.2f} GB")
#     print(f"  Used: {usage.used / (1024.0 ** 3):.2f} GB")
#     print(f"  Free: {usage.free / (1024.0 ** 3):.2f} GB")
#     print(f"  Number of Videos: {count_files('mp4') + count_files('mkv') + count_files('avi')}")
#     print(f"  Number of Images: {count_files('jpg') + count_files('jpeg') + count_files('png')}")
#     print(f"  Number of Documents: {count_files('doc') + count_files('docx') + count_files('pdf')}")

