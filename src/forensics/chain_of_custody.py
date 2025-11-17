"""Forensic Chain of Custody Module - Evidence-grade integrity tracking"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class ChainOfCustody:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.evidence_log = []
        
    def generate_file_hash(self, filepath: Path) -> str:
        """Generate SHA-256 hash for file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            self.logger.error(f"Hash generation failed for {filepath}: {e}")
            return ""
    
    def log_evidence(self, filepath: Path, action: str, operator: str) -> Dict:
        """Log evidence handling with timestamp and hash"""
        evidence_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "filepath": str(filepath),
            "action": action,
            "operator": operator,
            "sha256": self.generate_file_hash(filepath),
            "file_size": filepath.stat().st_size if filepath.exists() else 0
        }
        self.evidence_log.append(evidence_entry)
        self.logger.info(f"Evidence logged: {action} on {filepath} by {operator}")
        return evidence_entry
    
    def export_custody_log(self, output_path: Path) -> bool:
        """Export chain of custody log to JSON"""
        try:
            with open(output_path, "w") as f:
                json.dump({
                    "chain_of_custody": self.evidence_log,
                    "total_entries": len(self.evidence_log),
                    "export_timestamp": datetime.utcnow().isoformat() + "Z"
                }, f, indent=2)
            self.logger.info(f"Custody log exported to {output_path}")
            return True
        except Exception as e:
            self.logger.error(f"Export failed: {e}")
            return False
    
    def verify_integrity(self, filepath: Path, expected_hash: str) -> bool:
        """Verify file integrity against expected hash"""
        current_hash = self.generate_file_hash(filepath)
        if current_hash == expected_hash:
            self.logger.info(f"Integrity verified: {filepath}")
            return True
        else:
            self.logger.error(f"Integrity violation detected: {filepath}")
            return False