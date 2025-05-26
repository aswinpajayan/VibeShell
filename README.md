# VibeShell

![VibeShell Logo](https://via.placeholder.com/150)

> A lean, local-first boilerplate code generator for command-line loving geeks.

VibeShell is a lightweight CLI tool that generates boilerplate code using locally hosted Ollama models - no cloud dependencies, no logins, just pure coding flow.

## ✨ Features

- **100% Local** - All processing happens on your machine using Ollama models
- **Zero Telemetry** - Your code and prompts never leave your system
- **CLI-Centric** - Designed for terminal workflows and keyboard-driven development
- **Customizable** - Easily configure templates and model parameters
- **Zero Dependencies** - No need for external accounts or API keys

<!--
## 🚀 Installation

### Using uv (recommended)

```bash
uv add vibeshell
```

### Using pip

```bash
pip install vibeshell
```

### From source

```bash
git clone https://github.com/yourusername/vibeshell.git
cd vibeshell
uv add -e .
```
-->
## 🔧 Prerequisites

- Python 3.12+
- Docker
- uv
- npx

### llama 3.2 setup
- for the first run of ollama service, bind a folder to download the ollama model.
you can do this by modifying to docker compose file.  run the ollama service
```bash
docker compose up ollama
```
- pull llama3.2 by using one of the commands [here](https://github.com/ollama/ollama#model-library)
```bash
docker exec -it ollama ollama run llama3.2
```
> you have to select a version of llama that [support tool calling](https://ollama.com/search?c=tools)

## 📋 Usage

Make sure the ollama service is running. 
```bash
docker compose up ollama
```
Spawn an agent using fast agents
```bash
uv sync
uv run agent.py --model generic.llama3.2
```

Coming soon
> currently only filesystem server is registered. Its a work in progress


Add your requirements in requirements.vibe
<!--
### Basic Commands

Generate a React component:

```bash
vibe gen component LoginForm
```

Create a Python utility file:

```bash
vibe gen util data_processor
```

Get a quick explanation of code:

```bash
vibe explain < mycode.js
```
-->
### Configuration
<!--
Create or edit your config file:

```bash
vibe config init
```

Set your preferred Ollama model:

```bash
vibe config model codellama:7b-instruct
```

## ⚙️ Configuration Options

VibeShell can be configured via `~/.config/vibeshell/config.yml`:

```yaml
# Default model to use
model: codellama:7b-instruct

# Templates directory
templates_dir: ~/.config/vibeshell/templates

# Output formatting
output:
  syntax_highlight: true
  show_tokens: false

# Resource limits
limits:
  max_tokens: 2048
  timeout_seconds: 30
```
-->
> **Note:** For additional configuration options, check the [fast-agents-mcp configuration page](https://github.com/fast-agents-mcp/docs/config). 

To set up fast-agent integration, run:

```bash
fast-agent setup
```

**Important:** Make sure to add all secrets files to your `.gitignore`:

```
# Add to .gitignore
.env
secrets/
*_key.json
config.local.yml
```

## 🛠️ Creating Custom Templates

> **Note:** Custom templates feature is coming soon and not yet available in the current version.

In future releases, VibeShell will support custom templates for code generation. Stay tuned for updates!

## 📖 Documentation

Coming soom
For full documentation, visit [the VibeShell documentation site](https://vibeshell.dev).

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### Contributing Guidelines

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/aswinpajayan/VibeShell.git

# Install dev dependencies
cd VibeShell
uv add -e ".[dev]"
fast-agent setup

# edit secrets file and them to .gitignore

# configure the bind path of volume for ollama in docker-compose.yaml file
# start ollama service. 
docker compose up ollama

# if running for the first time, download a model using the below command. 
docker exec -it ollama ollama run llama3

# Run tests
pytest
```

>checkout all [models from ollama](https://github.com/ollama/ollama#model-library)

### Areas We Need Help With

- **Template Creation**: Adding more language-specific templates
- **Model Optimization**: Improving prompts for better code generation
- **Documentation**: Helping with guides and examples
- **Testing**: Writing more comprehensive tests
- **UI Improvements**: Making terminal output more readable

> **Feel free to add any new feature you'd like!** We just ask that you raise an issue before starting development to discuss your idea and ensure no duplicate efforts.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- The [Ollama](https://ollama.ai/) team for making local LLMs accessible
- [fast-agents-mcp](https://github.com/fast-agents-mcp) for their excellent MCP implementation
- [Anthropic](https://www.anthropic.com/) for developing the Model Context Protocol (MCP)
- Linus Torvalds for creating Linux and making it all possible
- All our contributors and early adopters
- The open source community for inspiration and support

---

<p align="center">Made with ❤️ by command-line enthusiasts</p>
