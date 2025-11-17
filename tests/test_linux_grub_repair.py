"""Unit tests for Linux boot repair module"""

import pytest
from unittest.mock import Mock, patch
from src.boot_recovery.linux_grub_repair import LinuxBootRepair

@pytest.fixture
def repair_instance():
    with patch('pathlib.Path.exists', return_value=False):
        return LinuxBootRepair()

def test_linux_boot_repair_init(repair_instance):
    """Test LinuxBootRepair initialization"""
    assert repair_instance is not None
    assert repair_instance.boot_loader is None

@patch('pathlib.Path.exists')
def test_detect_grub2(mock_exists):
    """Test GRUB2 detection"""
    mock_exists.return_value = True
    repair = LinuxBootRepair()
    assert repair.boot_loader == "grub2"

@patch('subprocess.run')
def test_repair_grub2_efi_success(mock_run):
    """Test successful GRUB2 EFI repair"""
    with patch('pathlib.Path.exists', return_value=True):
        repair = LinuxBootRepair()
        repair.boot_loader = "grub2"
        mock_run.return_value = Mock(returncode=0)
        result = repair.repair_grub2(efi=True)
        assert result is True
        assert mock_run.call_count == 2

@patch('subprocess.run')
def test_repair_systemd_boot_success(mock_run):
    """Test successful systemd-boot repair"""
    with patch('pathlib.Path.exists', return_value=True):
        repair = LinuxBootRepair()
        repair.boot_loader = "systemd-boot"
        mock_run.return_value = Mock(returncode=0)
        result = repair.repair_systemd_boot()
        assert result is True