import os
import platform
import psutil
from colorama import Fore, Style, init

# Windows 환경에서 색상 지원 초기화
init()

WINDOWS_11_ASCII = f"""
{Fore.BLUE}
################    ################
################    ################
################    ################
################    ################
################    ################
################    ################
################    ################

################    ################
################    ################
################    ################
################    ################
################    ################
################    ################
################    ################
{Style.RESET_ALL}
"""

LINUX_ASCII = f"""
{Fore.YELLOW}      .--.
     |o_o |
     |:_/ |
    //   \ \\
   (|     | )
  /'\\_   _/`\\
  \\___)=(___/{Style.RESET_ALL}
"""

def get_system_info():
    return {
        "OS": platform.system() + " " + platform.release(),
        "Host": platform.node(),
        "Kernel": platform.version(),
        "Uptime": f"{round(psutil.boot_time() / 3600, 2)} hours",
        "Shell": os.getenv('SHELL', 'cmd.exe' if os.name == 'nt' else 'bash'),
        "Resolution": "1920x1080",  # 실제 해상도 가져오는 방법 추가 가능
        "WM": "DWM.exe" if platform.system() == "Windows" else "Xorg",
        "Terminal": "Windows Terminal" if platform.system() == "Windows" else os.getenv('TERM', 'Unknown'),
        "CPU": platform.processor(),
        "GPU": "Intel(R) HD Graphics" if platform.system() == "Windows" else "NVIDIA",  # GPU 감지 기능 추가 가능
        "Memory": f"{round(psutil.virtual_memory().used / (1024 ** 2))}MiB / {round(psutil.virtual_memory().total / (1024 ** 2))}MiB"
    }

def display_info():
    info = get_system_info()
    os_ascii = WINDOWS_11_ASCII if "Windows" in info["OS"] else LINUX_ASCII
    
    # 운영체제 로고 출력
    print(os_ascii, end="")
    
    # 정보 출력 (좌측에 운영체제 로고와 나란히 표시되도록 조정)
    print(Fore.CYAN + "  " + os.getlogin() + "@" + info["Host"] + Style.RESET_ALL)
    print(Fore.YELLOW + "  " + "-" * 30 + Style.RESET_ALL)
    
    for key, value in info.items():
        print(Fore.GREEN + f"  {key:<12}: " + Style.RESET_ALL + str(value))
    
    print(Fore.YELLOW + "  " + "-" * 30 + Style.RESET_ALL)
    
    # 색상 블록 표시
    print("\n  " + "  ".join([ 
        Fore.BLACK + "██" + Fore.RED + "██" + Fore.GREEN + "██" + Fore.YELLOW + "██" +
        Fore.BLUE + "██" + Fore.MAGENTA + "██" + Fore.CYAN + "██" + Fore.WHITE + "██" + Style.RESET_ALL
    ]))

if __name__ == "__main__":
    display_info()
