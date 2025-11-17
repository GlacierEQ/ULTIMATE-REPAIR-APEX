"""macOS Recovery Mode Automation - Forensic-grade macOS boot recovery"""

import subprocess
import logging
from pathlib import Path

class MacOSRecovery:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.supported_versions = ["macOS 13", "macOS 14"]
        
    def verify_recovery_partition(self):
        """Verify macOS Recovery partition exists"""
        try:
            result = subprocess.run(["diskutil", "list"], capture_output=True, text=True, check=True)
            if "Recovery" in result.stdout:
                self.logger.info("Recovery partition found")
                return True
            else:
                self.logger.warning("No Recovery partition detected")
                return False
        except Exception as e:
            self.logger.error(f"Recovery verification failed: {e}")
            return False
    
    def rebuild_boot_cache(self):
        """Rebuild macOS boot cache"""
        self.logger.info("Rebuilding macOS boot cache")
        try:
            subprocess.run(["kextcache", "-i", "/"], check=True, capture_output=True)
            self.logger.info("Boot cache rebuilt successfully")
            return True
        except Exception as e:
            self.logger.error(f"Boot cache rebuild failed: {e}")
            return False
    
    def reset_nvram(self):
        """Reset NVRAM/PRAM (requires reboot)"""
        self.logger.warning("NVRAM reset requires system reboot")
        try:
            nvram_script = Path("/tmp/reset_nvram.sh")
            nvram_script.write_text("#!/bin/bash\nnvram -c\nshutdown -r now\n")
            nvram_script.chmod(0o755)
            self.logger.info("NVRAM reset script prepared")
            return True
        except Exception as e:
            self.logger.error(f"NVRAM reset preparation failed: {e}")
            return False