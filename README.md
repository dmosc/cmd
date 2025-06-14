# Command — Your AI-Powered Console Expert

> Want to just install it? Follow the [installation guide](#installation-guide).

**Command** is an AI-driven CLI assistant designed to help you accomplish virtually any task you can imagine — right from your terminal.

This tool is an expert in all existing command-line interfaces (CLIs) — from Git and Docker to system utilities and package managers. But Command goes further: it understands your entire operating system context, allowing it to plan and execute complex, multi-step operations safely and intelligently.

Whether you're trying to debug a system issue, automate a repetitive task, or explore unfamiliar tools, Command is your always-available shell companion — fluent in terminal speak, but powered by natural language.

## Key features

### 📚 CLI Expertise That Stays Fresh

Command stays up to date with the ever-evolving command-line ecosystem. We periodically re-index documentation for all major CLI tools — from `git` and `docker` to `kubectl`, `ffmpeg`, and beyond. Using Retrieval-Augmented Generation (RAG) techniques, Command continuously taps into the latest docs to generate accurate instructions every time.

### 🧠 Contextual Awareness

Command doesn't just guess — it understands. By analyzing your current working directory, environment variables, installed libraries, and shell history, it generates commands that are tailored to your specific system state and task.

### 🛡️ Safe Execution with Ephemeral VMs

Worried about breaking things? Command uses lightweight virtual machines that temporarily clone your file system and simulate the command's effects. This lets you preview the impact of any operation — even multi-step ones — in a sandboxed environment before deciding to run it for real.

### 📖 Built to Teach, Not Just Execute

Command isn't a black box. For every suggested command, it breaks down what each part does — the command, the flags, the arguments — so you can understand and learn from it. Over time, you don't just get things done faster — you become a CLI master yourself.

## Installation guide

Run the following command from your terminal:

```bash
curl -s https://raw.githubusercontent.com/dmosc/cmd/main/scripts/install.sh | sh
```

The installer will:
1. Download the latest release binary for your operating system
2. Install it to `$HOME/local/bin/cmd`
3. Make the binary executable
4. Add `$HOME/local/bin` to your PATH by modifying your shell configuration files:
   - `~/.bashrc` (if you use Bash)
   - `~/.zshrc` (if you use Zsh)
   - `~/.profile` (as a fallback)

After installation, you may need to restart your terminal or run `source ~/.bashrc` (or equivalent) to update your PATH. You can verify the installation by running:

```bash
which cmd
```

This should output: `$HOME/local/bin/cmd`.