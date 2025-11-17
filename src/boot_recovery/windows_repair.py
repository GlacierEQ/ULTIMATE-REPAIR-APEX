"""Windows Boot Recovery Module - Forensic-grade boot repair for Windows MBR/GPT/UEFI systems"""

import os
import subprocess
import logging
from pathlib import Path

class WindowsBootRepair:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.supported_versions = ["Windows 10", "Windows 11"]
        
    def verify_windows_installation(self):
        """Verify Windows installation integrity"""
        try:
            result = subprocess.run(["bcdedit", "/enum"], capture_output=True, text=True, check=True)
            self.logger.info("Windows BCD store accessible")
            return True
        except subprocess.CalledProcessError:
            self.logger.error("Cannot access Windows BCD store")
            return False
    
    def repair_mbr(self, drive="C:"):
        """Repair Master Boot Record (Legacy BIOS)"""
        self.logger.info(f"Repairing MBR on drive {drive}")
        try:
            commands = [["bootrec", "/fixmbr"], ["bootrec", "/fixboot"], ["bootrec", "/scanos"], ["bootrec", "/rebuildbcd"]]
            for cmd in commands:
                subprocess.run(cmd, check=True, capture_output=True)
                self.logger.info(f"Executed: {' '.join(cmd)}")
            return True
        except Exception as e:
            self.logger.error(f"MBR repair failed: {e}")
            return False
    
    def repair_uefi(self, efi_partition="Z:"):
        """Repair UEFI boot entries"""
        self.logger.info(f"Repairing UEFI boot on partition {efi_partition}")
        try:
            subprocess.run(["mountvol", efi_partition, "/S"], check=True)
            bcdboot_path = Path("C:\\Windows\\System32\\bcdboot.exe")
            if bcdboot_path.exists():
                subprocess.run([str(bcdboot_path), "C:\\Windows", "/s", efi_partition, "/f", "ALL"], check=True)
                self.logger.info("UEFI boot files repaired")
                return True
            else:
                self.logger.error("bcdboot.exe not found")
                return False
        except Exception as e:
            self.logger.error(f"UEFI repair failed: {e}")
            return False