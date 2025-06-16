#!/bin/bash

# Exit on error
set -e

# Detect OS and architecture & map OS to GitHub artifact name
case $(uname -s | tr '[:upper:]' '[:lower:]') in
    "darwin")
        OS="macos"
        ;;
    "linux")
        OS="linux"
        ;;
    "windows")
        OS="windows"
        ;;
    *)
        echo "Unsupported OS: $OS"
        exit 1
        ;;
esac

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Ollama based on OS
install_ollama() {
    case $OS in
        "macos")
            echo "Installing Ollama for macOS..."
            # Download and extract the zip file
            ZIP_PATH="/tmp/ollama.zip"
            echo "Downloading Ollama..."
            curl -sL "https://ollama.com/download/Ollama-darwin.zip" -o "$ZIP_PATH"
            echo "Extracting..."
            unzip -q "$ZIP_PATH" -d "/tmp/"
            APP_FILE="/tmp/Ollama.app"
            if [ -z "$APP_FILE" ]; then
                echo "Error: Could not find the Ollama app."
                rm -rf "$ZIP_PATH"
                exit 1
            fi
            # Copy to Applications
            mv -f "$APP_FILE" /Applications/
            rm -rf "$ZIP_PATH"
            echo "Ollama has been installed to /Applications. Please open it to complete the installation."
            ;;
        "linux")
            echo "Installing Ollama for Linux..."
            curl -fsSL https://ollama.com/install.sh | sh
            ;;
        "windows")
            echo "For Windows, please download and install Ollama from:"
            echo "https://ollama.com/download/windows"
            echo "After downloading, run the installer and follow the on-screen instructions."
            exit 1
            ;;
        *)
            echo "Unsupported OS: $OS"
            exit 1
            ;;
    esac
}

main() {
    # Check if Ollama is installed
    if ! command_exists ollama; then
        echo "Ollama is not installed. This is required for Command to work."
        read -p "Would you like to install Ollama now? [y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_ollama
        else
            echo "Please install Ollama manually from https://ollama.com/download"
            exit 1
        fi
    fi

    # Create bin directory if it doesn't exist
    BIN_DIR="$HOME/local/bin"
    mkdir -p "$BIN_DIR"

    # Download the appropriate artifact
    ARTIFACT_NAME="${OS}-main"
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
}

main