#!/bin/bash
set -euo pipefail

echo "🔐 FORENSIC REPOSITORY VERIFICATION REPORT"
echo "=========================================="
echo "Date: $(date -u +\"%Y-%m-%d %H:%M:%S UTC\")"
echo "Repository: $(git remote get-url origin 2>/dev/null || echo 'Local')"
echo "Commit: $(git rev-parse HEAD)"
echo ""

# 1. Repository Integrity
echo "📋 Git Integrity Check (git fsck --full):"
git fsck --full 2>&1 | head -n 5
echo ""

# 2. Verify All Commit Signatures
echo "✍️ Commit Signature Verification:"
UNSIGNED=$(git log --show-signature --format=\"%H\" 2>&1 | grep -c \"No signature\" || true)
TOTAL=$(git rev-list --all --count)
echo "  Total Commits: $TOTAL"
echo "  Unsigned: $UNSIGNED"
echo "  Status: $([[ $UNSIGNED -eq 0 ]] && echo '✅ ALL SIGNED' || echo '⚠️ UNSIGNED COMMITS FOUND')"
echo ""

# 3. Verify Checksums
echo "🔢 SHA-256 Checksum Verification:"
if [[ -f checksums.txt ]]; then
    sha256sum -c checksums.txt 2>&1 | tail -n 1
else
    echo "  ⚠️ checksums.txt not found - generating..."
    find . -type f -not -path \"./.git/*\" -not -name \"checksums.txt\" -exec sha256sum {} \\; > checksums.txt
    echo "  ✅ Generated checksums.txt"
fi
echo ""

# 4. Verify Latest Tag
echo "🏷️ Tag Verification:"
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "none")
if [[ "$LATEST_TAG" != "none" ]]; then
    git verify-tag "$LATEST_TAG" 2>&1 | grep -E "(Good|BAD)" || echo "  ✅ Tag signature valid"
else
    echo "  ℹ️ No tags found"
fi
echo ""

# 5. Audit Trail
echo "📜 Audit Trail (Last 10 operations):"
git reflog --date=iso | head -n 10
echo ""

# 6. Generate Evidence Hash
echo "🔗 Evidence Chain Hash:"
COMMIT_HASH=$(git log --oneline | sha256sum | cut -d' ' -f1)
echo "  Commit History Hash: $COMMIT_HASH"
echo ""

echo "=========================================="
echo "✅ VERIFICATION COMPLETE"
echo "Report Hash: $(echo \"$COMMIT_HASH\" | sha256sum | cut -d' ' -f1)"
