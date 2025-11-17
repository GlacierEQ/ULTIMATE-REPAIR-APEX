"""Unit tests for forensic chain of custody module"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch
from src.forensics.chain_of_custody import ChainOfCustody

@pytest.fixture
def custody_instance():
    return ChainOfCustody()

def test_chain_of_custody_init(custody_instance):
    """Test ChainOfCustody initialization"""
    assert custody_instance is not None
    assert custody_instance.evidence_log == []

def test_generate_file_hash(custody_instance, tmp_path):
    """Test SHA-256 hash generation"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("forensic test data")
    
    hash_result = custody_instance.generate_file_hash(test_file)
    assert len(hash_result) == 64
    assert hash_result.isalnum()

def test_log_evidence(custody_instance, tmp_path):
    """Test evidence logging"""
    test_file = tmp_path / "evidence.txt"
    test_file.write_text("evidence data")
    
    entry = custody_instance.log_evidence(test_file, "CREATE", "Casey Barton")
    assert entry["action"] == "CREATE"
    assert entry["operator"] == "Casey Barton"
    assert len(entry["sha256"]) == 64
    assert len(custody_instance.evidence_log) == 1

def test_verify_integrity(custody_instance, tmp_path):
    """Test file integrity verification"""
    test_file = tmp_path / "verify.txt"
    test_file.write_text("test data")
    
    expected_hash = custody_instance.generate_file_hash(test_file)
    result = custody_instance.verify_integrity(test_file, expected_hash)
    assert result is True
    
    wrong_hash = "a" * 64
    result = custody_instance.verify_integrity(test_file, wrong_hash)
    assert result is False