# 🎭 Claude Code Persona Configuration System

This document describes the persona configuration system for Claude Code. This system allows you to customize how Claude Code communicates, uses emojis, and presents information.

## Overview

The persona system is designed with future MEML (Emoji Markup Language) integration in mind. Currently, it uses JSON configuration files (`.personarc`), with hooks prepared for MEML-based control.

## Configuration Files

### `.personarc.schema.json`
The JSON schema that defines the structure and valid values for persona configurations. Use this to:
- Validate your custom persona configs
- Understand all available options
- See descriptions and defaults

### `.personarc.example`
An example persona configuration showing heavy emoji usage. This demonstrates what's possible with the persona system.

### `.personarc` (Custom)
Your custom persona configuration. Create this at:
- **User level:** `~/.personarc` (applies to all projects)
- **Project level:** `./.personarc` (applies to this project only)

## Configuration Options

### `persona` — Core Settings

```json
{
  "persona": {
    "name": "Claude Code ✨",
    "emoji_level": "heavy",    // "none" | "minimal" | "moderate" | "heavy"
    "tone": "friendly",         // professional, casual, playful, technical, friendly
    "style": "detailed"         // terse, concise, verbose, detailed, academic
  }
}
```

- **`emoji_level`**: Controls how frequently emojis appear in output
  - `none`: No emojis
  - `minimal`: Only status indicators (✅ ❌)
  - `moderate`: Headers + status indicators (recommended)
  - `heavy`: Comprehensive emoji usage throughout

- **`tone`**: Communication style
- **`style`**: Output verbosity

### `greetings` — Messages

```json
{
  "greetings": {
    "greeting": "🚀 Ready to code!",
    "sign_off": "✨ Generated with Claude Code"
  }
}
```

### `responses` — Reaction Styles

```json
{
  "responses": {
    "success_emoji": "✅",
    "error_emoji": "❌",
    "warning_emoji": "⚠️",
    "info_emoji": "ℹ️",
    "success_style": "exuberant",   // exuberant, understated, technical, playful
    "error_style": "supportive"      // detailed, brief, supportive, technical
  }
}
```

### `features` — Feature Toggles

```json
{
  "features": {
    "use_markdown_headers": true,
    "use_status_indicators": true,
    "use_section_dividers": true,
    "use_todo_lists": true
  }
}
```

## MEML Integration (Future)

The persona system includes hooks for future MEML (Emoji Markup Language) integration:

```json
{
  "meml_integration": {
    "enabled": false,
    "meml_file": "persona.meml",
    "auto_reload": true
  }
}
```

### How It Will Work

Once MEML integration is implemented, you'll be able to define personas using MEML syntax:

```meml
🎭 Persona: "Claude Code Heavy Emoji"
  emoji_level: 🔥 (heavy)
  tone: 🤝 (friendly)
  style: 📚 (detailed)

  responses:
    success: ✅ (exuberant)
    error: ❌ (supportive)
    warning: ⚠️
```

This allows persona configuration as a first-class language feature with full emoji support.

## Examples

### Example 1: Professional Minimal

```json
{
  "version": "1.0",
  "persona": {
    "name": "Claude Code Professional",
    "emoji_level": "minimal",
    "tone": "professional",
    "style": "concise"
  }
}
```

### Example 2: Casual Emoji-Heavy

```json
{
  "version": "1.0",
  "persona": {
    "name": "Claude Code Emojis",
    "emoji_level": "heavy",
    "tone": "casual",
    "style": "verbose"
  },
  "greetings": {
    "greeting": "🚀 Let's build something amazing!",
    "sign_off": "✨ Keep coding! ✨"
  }
}
```

### Example 3: Technical Detailed

```json
{
  "version": "1.0",
  "persona": {
    "name": "Claude Code Technical",
    "emoji_level": "moderate",
    "tone": "technical",
    "style": "detailed"
  },
  "responses": {
    "success_style": "technical",
    "error_style": "detailed"
  }
}
```

## Current Implementation Status

✅ **Schema Definition** — Full JSON schema defined
✅ **Example Config** — Heavy emoji persona available
🟡 **Loading Mechanism** — Hooks prepared for future implementation
🟡 **MEML Integration** — Structure ready, awaiting MEML feature completion

## TODO / Future Work

- [ ] Implement `.personarc` loading in Claude Code CLI
- [ ] Add persona switching command (`claude persona set`)
- [ ] Integrate MEML language parser once available
- [ ] Create UI for persona customization
- [ ] Share popular personas via registry
- [ ] Add persona composition (inherit + override)

## See Also

- 🎭 **MEML Project**: https://github.com/caboose-ai/meml
- 📚 **JSON Schema**: `.personarc.schema.json`
- 📋 **Example Config**: `.personarc.example`
