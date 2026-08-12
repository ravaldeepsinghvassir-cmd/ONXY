# ⚙️ ONXY

### The Autonomous Personal AI Operating System

**By Ravaldeep Singh Vassir**

> **Hear. See. Think. Act. Remember.**

ONXY is a cross-platform personal AI assistant designed to become a persistent digital companion and computer-control layer.

It combines real-time voice interaction, visual awareness, persistent memory, computer control, web research, autonomous task execution, proactive intelligence, system monitoring, browser automation, file processing, and remote access into a unified AI system.

The vision is simple:

> **An AI that doesn't just answer you — it understands your environment, remembers your context, uses your tools, and helps execute real-world tasks.**

---

## ✨ What Is ONXY?

ONXY is an experimental autonomous AI assistant that connects an AI reasoning layer with your operating system and digital environment.

Instead of functioning like a traditional chatbot, ONXY is designed to:

- 🎙️ Hear you through real-time voice interaction
- 🧠 Understand natural language and context
- 👁️ See and analyze your screen
- 📷 Process camera input
- 💻 Control applications and system functions
- 🌐 Search and research the web
- 📂 Read and process local files
- 🤖 Execute multi-step tasks
- 🧠 Remember important context across sessions
- 📊 Monitor system hardware
- 🔔 Provide proactive notifications
- ⏰ Create reminders
- 🌐 Control browsers
- 🎬 Control YouTube
- 📋 Understand clipboard content
- 📱 Provide remote dashboard access
- 🛠️ Assist with coding and development

The long-term objective is to evolve ONXY from a personal assistant into a **general-purpose autonomous AI employee for the user's digital environment.**

---

# 🚀 Core Capabilities

## 🎙️ Real-Time Voice Intelligence

ONXY supports real-time voice interaction using the Gemini Live API.

Designed for:

- Natural conversations
- Low-latency interaction
- Multilingual communication
- Voice commands
- Continuous conversational context
- Hands-free computer interaction

ONXY can adapt its communication language based on the user's interaction.

---

## 🧠 Persistent Memory

ONXY maintains persistent context across sessions.

Memory can contain:

- User identity
- Preferences
- Active projects
- Previous sessions
- Important conversation context
- Monitored topics
- Assistant configuration

The goal is to make ONXY feel continuous instead of starting from zero every time it launches.

### Session Memory

At the end of a session, ONXY can generate a short summary of what was discussed.

The next session can use that context naturally.

Example:

> "Good morning. Yesterday you were working on the ONXY dashboard. Would you like to continue from where you stopped?"

Session summaries are designed to avoid unnecessary long-term memory growth.

---

# 👁️ Visual Intelligence

ONXY can process visual information from the computer environment.

Supported capabilities include:

- Screen capture
- Webcam input
- Visual analysis
- Screenshot interpretation
- UI understanding
- Visual troubleshooting

Example:

> "ONXY, look at my screen and tell me why this Python application is showing an error."

The assistant can capture the relevant visual context and use AI vision capabilities to analyze it.

---

# 💻 Computer Control

ONXY can interact with the operating system through dedicated action modules.

Examples include:

- Open applications
- Close applications
- Keyboard shortcuts
- Mouse control
- Window management
- Taskbar interaction
- Volume control
- Brightness control
- Wi-Fi control
- Power operations
- Desktop operations

OS-specific functionality is isolated where possible to keep the core architecture portable.

---

# 🤖 Autonomous Task Execution

ONXY supports multi-step task execution through an agent-oriented architecture.

Instead of requiring every individual action to be specified, a high-level objective can be provided.

Example:

> "Open my project, inspect the error, find the relevant file and help me fix it."

The system can break a goal into smaller actions and use available tools.

This is one of the primary foundations for future autonomous capabilities.

---

# 🌐 Web Intelligence

ONXY provides multiple web-search modes.

Supported search categories include:

- `search`
- `news`
- `research`
- `price`
- `compare`

The search architecture can use multiple information sources and fallback mechanisms.

Example:

> "Research the latest developments in AI agents and summarize the important changes."

---

# 📰 Parallel Search Architecture

For selected news operations, ONXY can execute multiple search paths in parallel.

```text
                    User Query
                        │
                        ▼
                Search Controller
                   /          \
                  /            \
                 ▼              ▼
        Gemini Grounding     DDG News
                 │              │
                 └──────┬───────┘
                        ▼
                 First Valid Result
                        │
                        ▼
                       ONXY

---

## ⚡ Quick Start

```bash
git clone https://github.com/ravaldeepsinghvassir-cmd/ONXY.git
cd ONXY
pip install -r requirements.txt
python main.py
```

> ⚠️ **Installation Note:** Some OS-specific dependencies are not bundled in `requirements.txt` to keep the repo lightweight. If you hit a `ModuleNotFoundError`, install the missing package with `pip install <module_name>`.

---

## 📋 Requirements

| Requirement | Details |
| --- | --- |
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11 or 3.12 |
| **Microphone** | Required for voice interaction |
| **API Key** | Free Gemini API key (`config/api_keys.json`) |

---

## 🗂️ Project Structure

```
ONXY/
├── main.py                   # Core loop — Gemini Live session, audio I/O, tool dispatch
├── ui.py                     # PyQt6 HUD — waveform, log panel, interrupt button, camera feed
├── setup.py                  # First-run configuration wizard
├── actions/
│   ├── web_search.py         # Gemini + DDG parallel search (news, research, price, compare)
│   ├── screen_processor.py   # Screen capture & webcam vision via Gemini Live
│   ├── background_monitor.py # User-configured topic watching — daily DDG check, no crypto
│   ├── proactive.py          # Proactive 2.0 — time/context/rotation-aware check-ins
│   ├── reminder.py           # OS-native scheduled notifications
│   ├── system_monitor.py     # CPU / RAM / GPU / temperature telemetry
│   ├── computer_settings.py  # Volume, brightness, WiFi, power
│   ├── computer_control.py   # Keyboard shortcuts, mouse, window management
│   ├── open_app.py           # Application launcher
│   ├── browser_control.py    # Web browser control
│   ├── file_controller.py    # File system operations
│   ├── file_processor.py     # Document reading and summarization
│   ├── send_message.py       # Messaging integration
│   ├── weather_report.py     # Live weather data
│   ├── flight_finder.py      # Flight search
│   ├── youtube_video.py      # YouTube playback control
│   ├── game_updater.py       # Game update management (Steam / Epic)
│   ├── code_helper.py        # Code review and generation
│   ├── dev_agent.py          # Developer task agent
│   └── desktop.py            # Desktop and taskbar control
├── memory/
│   ├── memory_manager.py     # Load/save long_term.json — sessions, monitors, identity
│   └── long_term.json        # Persistent store: identity, preferences, projects, sessions, monitors
├── core/
│   └── prompt.txt            # Assistant personality and tool-routing rules
└── config/
    └── api_keys.json         # API key, OS setting, assistant name, user name
```

---

## ⚠️ License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## 👤 Connect with the Creator

Engineered by a developer building a real-world ONXY-style assistant.
⭐ **Star the repository to support the journey to ONXY 100.**


