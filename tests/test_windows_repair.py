"""Unit tests for Windows boot repair module"""

import pytest
from unittest.mock import Mock, patch
from src.boot_recovery.windows_repair import WindowsBootRepair

@pytest.fixture
def repair_instance():
    return WindowsBootRepair()

def test_windows_boot_repair_init(repair_instance):
    """Test WindowsBootRepair initialization"""
    assert repair_instance is not None
    assert "Windows 10" in repair_instance.supported_versions
    assert "Windows 11" in repair_instance.supported_versions

@patch('subprocess.run')
def test_verify_windows_installation(mock_run, repair_instance):
    """Test Windows installation verification"""
    mock_run.return_value = Mock(stdout="Windows Boot Manager", returncode=0)
    result = repair_instance.verify_windows_installation()
    assert result is True
    mock_run.assert_called_once()

@patch('subprocess.run')
def test_repair_mbr_success(mock_run, repair_instance):
    """Test successful MBR repair"""
    mock_run.return_value = Mock(returncode=0)
    result = repair_instance.repair_mbr(drive="C:")
    assert result is True
    assert mock_run.call_count == 4

@patch('subprocess.run')
def test_repair_uefi_success(mock_run, repair_instance):
    """Test successful UEFI repair"""
    with patch('pathlib.Path.exists', return_value=True):
        mock_run.return_value = Mock(returncode=0)
        result = repair_instance.repair_uefi(efi_partition="Z:")
        assert result is True