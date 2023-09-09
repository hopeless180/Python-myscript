import ctypes
from ctypes import wintypes
from ctypes import byref
import os

# # 定义函数原型
# GetFileInformationByHandleExProto = ctypes.WINFUNCTYPE(
#     ctypes.c_bool,
#     ctypes.c_void_p,
#     ctypes.c_int,
#     ctypes.c_void_p,
#     ctypes.c_ulong
# )
# # 加载动态链接库
# kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
# # 使用库中的函数
# GetFileInformationByHandleEx = GetFileInformationByHandleExProto(("GetFileInformationByHandleEx", kernel32))

kernel32 = ctypes.WinDLL('kernel32')
GetFileInformationByHandleEx = kernel32.GetFileInformationByHandleEx
GetFileInformationByHandleEx.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
GetFileInformationByHandleEx.restype = wintypes.BOOL

class FILE_INFO(ctypes.Structure):
    _fields_ = [
        ("dwFileAttributes", ctypes.c_uint32),
        ("ftCreationTime", ctypes.c_uint64),
        ("ftLastAccessTime", ctypes.c_uint64),
        ("ftLastWriteTime", ctypes.c_uint64),
        ("nFileSizeHigh", ctypes.c_uint32),
        ("nFileSizeLow", ctypes.c_uint32),
        ("dwReserved0", ctypes.c_uint32),
        ("dwReserved1", ctypes.c_uint32),
        ("cFileName", ctypes.c_wchar * 260),
        ("cAlternateFileName", ctypes.c_wchar * 14)
    ]

# hFile = ctypes.windll.kernel32.CreateFileW(r'E:\车\同人3D\猫こねり\_そに子__ねこ缶__2.mp4', 0x80000000, 1, None, 3, 0x80, None)
hFile = os.open(r"E:\车\同人3D\猫こねり\_そに子__ねこ缶__2.mp4", os.O_RDONLY)
if hFile != -1:
    buffer_size = 1024
    lpFileInformation = ctypes.create_string_buffer(buffer_size)
    file_info = FILE_INFO()
    success = GetFileInformationByHandleEx(hFile, 0, byref(file_info), buffer_size)
    if success:
        # Handle file information
        print(file_info)
    ctypes.windll.kernel32.CloseHandle(hFile)

# # 打开文件
# file_handle = open(r"E:\车\mmd\[SexDance]连的素描特训_Chocolate Cream.mp4", "rb")

# # 获取文件唯一标识符
# file_id_info = ctypes.create_string_buffer(ctypes.sizeof(ctypes.c_ulonglong))
# if not GetFileInformationByHandleEx(ctypes.c_void_p(file_handle.fileno()), 0x40, file_id_info, ctypes.sizeof(file_id_info)):
#     error_code = ctypes.get_last_error()
#     raise ctypes.WinError(error_code)

# # 解析文件唯一标识符
# file_id = ctypes.cast(file_id_info, ctypes.POINTER(ctypes.c_ulonglong)).contents.value

# # 关闭文件
# file_handle.close()

# # 使用文件唯一标识符
# print(f"File identifier: {file_id}")