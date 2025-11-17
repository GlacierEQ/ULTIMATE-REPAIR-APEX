"""Linux GRUB2/systemd-boot Repair - Forensic-grade Linux boot loader recovery"""

import subprocess
import logging
from pathlib import Path

class LinuxBootRepair:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.boot_loader = None
        self.detect_boot_loader()
        
    def detect_boot_loader(self):
        """Detect active boot loader (GRUB2 or systemd-boot)"""
        try:
            if Path("/boot/grub/grub.cfg").exists():
                self.boot_loader = "grub2"
                self.logger.info("GRUB2 boot loader detected")
            elif Path("/boot/efi/EFI/systemd").exists():
                self.boot_loader = "systemd-boot"
                self.logger.info("systemd-boot detected")
            else:
                self.logger.warning("No recognized boot loader found")
                self.boot_loader = None
        except Exception as e:
            self.logger.error(f"Boot loader detection failed: {e}")
    
    def repair_grub2(self, efi=True):
        """Repair GRUB2 boot loader"""
        if self.boot_loader != "grub2":
            self.logger.error("GRUB2 not detected")
            return False
        self.logger.info("Repairing GRUB2 boot loader")
        try:
            if efi:
                subprocess.run(["grub-install", "--target=x86_64-efi", "--efi-directory=/boot/efi", "--bootloader-id=GRUB"], check=True)
            else:
                subprocess.run(["grub-install", "/dev/sda"], check=True)
            subprocess.run(["update-grub"], check=True)
            self.logger.info("GRUB2 repaired successfully")
            return True
        except Exception as e:
            self.logger.error(f"GRUB2 repair failed: {e}")
            return False
    
    def repair_systemd_boot(self):
        """Repair systemd-boot"""
        if self.boot_loader != "systemd-boot":
            self.logger.error("systemd-boot not detected")
            return False
        self.logger.info("Repairing systemd-boot")
        try:
            subprocess.run(["bootctl", "install"], check=True)
            self.logger.info("systemd-boot repaired successfully")
            return True
        except Exception as e:
            self.logger.error(f"systemd-boot repair failed: {e}")
            return False