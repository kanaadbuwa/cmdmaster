#  CmdMaster - A Personal Linux CLI Assistant 

**CmdMaster** is a command-line productivity tool designed to help users navigate the Linux terminal more efficiently by providing a collection of frequently used shell commands at their fingertips.

---

## 🛠️ Why CmdMaster?

Let’s face it — remembering every Linux command and their endless options can be a pain. Especially if you:
- Constantly Google the same commands
- Forget complex syntax
- Waste time typing long command chains

**CmdMaster** solves that by being your always-ready CLI cheat-sheet with built-in execution, search, and discovery capabilities.

---

## 👤 Who Is This Tool For?

CmdMaster is perfect for:
- 🧑‍💻 **Beginners** just starting out in Linux and struggling with memorizing commands.
- ⚙️ **System administrators** and power users who need quick access to routine commands.
- 📚 **Students**, learners, and hobbyists working in terminal environments.
- 🐧 Anyone who lives in the Linux shell and wants a **productivity boost**.

---

## 🚀 Features

- 🔍 **Search** commands by keyword
- 📜 **List** all available commands
- ⚡ **Execute** commands directly from the terminal
- 🧠 **Descriptions** help you understand each command
- 🔌 Easy to extend: add more commands in `commands_map.yaml`

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/kanaadbuwa/cmdmaster.git
cd cmdmaster
```

---

## 🧪 Usage

Run the tool using Python 3:

```bash
python3 main.py <command-key>
```

### Available Options

| Command | Description |
|--------|-------------|
| `list` | Show all available command keys |
| `search <keyword>` | Search for commands matching a keyword |
| `help` | Show usage help |
| `<command-key>` | Run the associated shell command |

### Examples

```bash
python3 main.py list
python3 main.py search ip
python3 main.py show-ip
```

---

## 🧩 Customizing Your Commands

All commands are defined in `commands_map.yaml`:

```yaml
show-ip:
  command: "ip a | grep inet"
  description: "Display your system's IP addresses"
```

To add your own:
1. Open `commands_map.yaml`
2. Add a new entry with a key, `command`, and `description`

---

## 💡 Tips to Get the Best Out of CmdMaster

- Create your own custom commands (aliases, automation snippets)
- Use it as a centralized place to store long or tricky terminal commands
- Continuously build your own *Linux brain* into `commands_map.yaml`
- Extend support for other shells like ZSH, Fish, or even Windows (Coming Soon)

---

## 🪟 Windows Support?

Windows support (CMD, PowerShell) is on the roadmap! For now, Linux and WSL are fully supported.

---

## 📌 Future Plans

- ✅ CLI for Linux (Current)
- ⏳ Support for PowerShell & CMD
- ⏳ Import/export command libraries
- ⏳ GUI wrapper with Tkinter or web frontend

---

## 👨‍💻 Author

Made by [kanaadbuwa](https://github.com/kanaadbuwa)  
Just a curious mind tired of typing the same damn commands.

---

##  Terminal > GUI

> "Master the terminal, and you'll master the system."  
> — CmdMaster Philosophy
