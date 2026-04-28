# Pre-Lecture Setup: Agentic Coding Tools in VS Code

**Please complete this setup before arriving at the lecture.**
If you run into problems, bring your laptop and we will sort it out together at the start.

> ⚠️ **Note:** This space is moving extremely fast. The specific tools and installation
> steps below are likely to change — possibly before the next edition of this course.
> If something looks out of date, check the tool's official documentation first and let us know.

---

## What we require

You need **two things** working before the lecture:

1. **Visual Studio Code** installed on your laptop
2. **One agentic coding tool** integrated into VS Code — your choice which one

That's it. You do not need all of them, and you do not need to use the same tool as
the person next to you. The goal is that everyone arrives with at least one working setup
so we can spend the lecture using the tools rather than installing them.

---

## Step 1 — Install VS Code

Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com).
It is free, cross-platform (macOS, Windows, Linux), and the default editor used throughout this course.

**Verify:** open VS Code and confirm you can open a terminal inside it
(`Terminal → New Terminal` from the menu bar).

---

## Step 2 — Choose and install one agentic tool

Pick whichever option fits your existing accounts and preferences.
You only need one to work.

---

### Option A — GitHub Copilot (recommended if you have a .edu email)

GitHub offers Copilot for free to students via the
[GitHub Education Pack](https://education.github.com/pack).

1. Sign up or log in at [github.com](https://github.com) with your `.edu` email address
2. Apply for the GitHub Education Pack at [education.github.com/pack](https://education.github.com/pack)
   (approval is usually instant or within a few hours)
3. In VS Code, open the Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`)
4. Search for **GitHub Copilot** and install it
5. Also install **GitHub Copilot Chat** if it is not bundled automatically
6. Sign in to GitHub when prompted

**Verify:** open the Copilot Chat panel (speech bubble icon in the sidebar),
type `@workspace what files are in this folder?` and confirm you get a response.
To use agent mode, click the dropdown next to the send button and select **Agent**.

---

### Option B — Claude Code

Claude Code is Anthropic's terminal-based agentic tool.
It runs in VS Code's integrated terminal and has a free tier.

**Requirements:** Node.js installed ([nodejs.org](https://nodejs.org), LTS version)
and a free Anthropic account ([console.anthropic.com](https://console.anthropic.com)).

```bash
# Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# Authenticate (opens a browser login)
claude login

# Verify installation
claude --version
```

**Usage inside VS Code:** open the integrated terminal (`Ctrl+\`` / `Cmd+\``)
and run `claude` from your project folder. Claude Code will read and edit files
in the current directory.

**Note on free tier:** the free tier has usage limits. If you hit them during the lecture,
you may need to wait briefly or switch to another option.

---

### Option C — OpenAI Codex CLI

OpenAI's terminal-based agentic coding tool, similar in spirit to Claude Code.

**Requirements:** Node.js installed and an OpenAI account ([platform.openai.com](https://platform.openai.com)).
New accounts receive free credits; after that, usage is pay-as-you-go.

```bash
# Install Codex CLI globally
npm install -g @openai/codex

# Set your API key (get it from platform.openai.com/api-keys)
export OPENAI_API_KEY="your-key-here"
# On Windows (PowerShell):
# $env:OPENAI_API_KEY="your-key-here"

# Verify installation
codex --version
```

**Usage inside VS Code:** open the integrated terminal and run `codex` from your project folder.

**Tip:** add the `export` line to your shell profile (`.bashrc`, `.zshrc`, etc.)
so you do not have to set it each session.

---

### Option D — Cline (open source, works with any provider)

Cline is an open-source VS Code extension that acts as an agentic coding assistant.
It supports a wide range of backend models — OpenAI, Anthropic, Google Gemini,
local models via Ollama, and others — so you can connect it to whatever account you already have.

1. In VS Code, install the **Cline** extension from the Extensions panel
2. Open the Cline panel (robot icon in the sidebar)
3. Click the settings gear and enter your API key for whichever provider you prefer
4. Select the corresponding model from the dropdown

**Verify:** ask Cline to `list the .ipynb files in the current folder` and confirm it responds correctly.

**Why this option is useful:** if you already have an API key from any major provider,
Cline lets you use it without installing anything on the command line.

---

## Step 3 — Verify your setup

Once you have installed one of the above, do this quick check to confirm everything works:

1. Open VS Code and navigate to the `lecture_10_astropy` folder from this course
2. Open your agentic tool (chat panel or terminal)
3. Give it this prompt:

   > *"Using astropy.units, write a one-liner that computes the Schwarzschild radius
   > of the Sun (r_s = 2GM/c²) and prints the result in kilometres."*

4. Run the code it produces and verify the output is approximately **2.95 km**

If that works, you are ready for the lecture.

---

## Troubleshooting

| Problem | Likely cause | Fix |
| ------- | ------------ | --- |
| `npm: command not found` | Node.js not installed | Install from [nodejs.org](https://nodejs.org) |
| API key errors | Key not set or expired | Re-check your account and regenerate the key |
| Copilot not responding | Not signed in | `Shift+Cmd+P` → *GitHub Copilot: Sign In* |
| Rate limit / quota exceeded | Free tier exhausted | Wait, or switch to a different option for the lecture |

If you are stuck, bring your laptop — we will have 10 minutes at the start of the lecture to sort out setup issues.

---

## A note on choice

We are not prescribing a specific tool because the landscape is changing too quickly
for any single recommendation to stay current. What matters for this lecture is that
you have *something* working so you can participate in the exercises.
In practice, you will likely settle on one tool that fits your workflow,
and it may well be different from what a colleague uses — that is fine.
