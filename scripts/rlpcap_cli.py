#!/usr/bin/env python3
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

from rlpcap.utils import is_npcap_installed, open_npcap_install_page, get_active_network_interface
from rlpcap.sniffer import sniff_for_server

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    last_server = "N/A"
    while True:
        clear()
        print(Fore.MAGENTA + Style.BRIGHT + "🚀 Rocket League Server Sniffer\n")
        print(f"Last Server: {Fore.YELLOW}{last_server}{Style.RESET_ALL}\n")
        print("[1] Scan for server")
        print("[2] Install/check Npcap")
        print("[3] Exit\n")

        choice = input("Select an option: ").strip()
        if choice == "1":
            # run sniff — silent except for updating the single line afterwards
            try:
                result = sniff_for_server()
            except Exception as e:
                # preserve silent UX: set last_server to N/A but don't spam details
                result = None

            if result:
                last_server = result
            # loop will redraw menu (keeps UI stable; only Last Server changes)
            continue

        elif choice == "2":
            # quick check and open installer if not present
            if is_npcap_installed():
                print("Npcap appears to be installed.")
            else:
                print("Npcap not found — opening download page in your browser...")
                open_npcap_install_page()
            time.sleep(1.2)
            continue

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
