"""Unit tests for macOS recovery module"""

import pytest
from unittest.mock import Mock, patch
from src.boot_recovery.macos_recovery import MacOSRecovery

@pytest.fixture
def recovery_instance():
    return MacOSRecovery()

def test_macos_recovery_init(recovery_instance):
    """Test MacOSRecovery initialization"""
    assert recovery_instance is not None
    assert "macOS 13" in recovery_instance.supported_versions
    assert "macOS 14" in recovery_instance.supported_versions

@patch('subprocess.run')
def test_verify_recovery_partition_found(mock_run, recovery_instance):
    """Test recovery partition detection when found"""
    mock_run.return_value = Mock(stdout="Recovery HD\nAPFS Volume", returncode=0)
    result = recovery_instance.verify_recovery_partition()
    assert result is True

@patch('subprocess.run')
def test_verify_recovery_partition_not_found(mock_run, recovery_instance):
    """Test recovery partition detection when not found"""
    mock_run.return_value = Mock(stdout="Macintosh HD\nAPFS Volume", returncode=0)
    result = recovery_instance.verify_recovery_partition()
    assert result is False

@patch('subprocess.run')
def test_rebuild_boot_cache_success(mock_run, recovery_instance):
    """Test successful boot cache rebuild"""
    mock_run.return_value = Mock(returncode=0)
    result = recovery_instance.rebuild_boot_cache()
    assert result is True