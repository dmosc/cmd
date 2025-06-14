#!/bin/bash

# Exit on error
set -e

# Detect OS and architecture
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
case $OS in
    "darwin")
        OS_NAME="macos"
        ;;
    "linux")
        OS_NAME="linux"
        ;;
    "windows")
        OS_NAME="windows"
        ;;
    *)
        echo "Unsupported OS: $OS"
        exit 1
        ;;
esac

# Create bin directory if it doesn't exist
BIN_DIR="$HOME/local/bin"
mkdir -p "$BIN_DIR"

# Download the appropriate artifact
ARTIFACT_NAME="${OS_NAME}-main"
if [ "$OS" = "windows" ]; then
    ARTIFACT_NAME="${ARTIFACT_NAME}.exe"
fi

echo "Downloading latest release for $ARTIFACT_NAME..."

# Download the artifact
curl -L "https://github.com/dmosc/cmd/releases/latest/download/${ARTIFACT_NAME}" -o "$BIN_DIR/cmd"

# Make it executable
chmod +x "$BIN_DIR/cmd"

# Add to PATH if not already present
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Adding $BIN_DIR to PATH..."
    if [ -f "$HOME/.bashrc" ]; then
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$HOME/.bashrc"
    fi
    if [ -f "$HOME/.zshrc" ]; then
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$HOME/.zshrc"
    fi
    if [ -f "$HOME/.profile" ]; then
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$HOME/.profile"
    fi
fi

echo "Installation complete! The 'cmd' command is now available."
echo "You may need to restart your terminal or run 'source ~/.bashrc' (or equivalent) to update your PATH."
