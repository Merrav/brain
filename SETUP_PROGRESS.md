# Brain Setup Progress

## ✅ Completed
1. **Repository cloned** to `/Users/prag/Documents/Code/Claude/Projects/Brain`
2. **System dependencies installation started** (running in background)
   - Installing: yt-dlp, ffmpeg, whisper (~2GB model download), graphify, Obsidian

## ⏳ Currently Installing
- `yt-dlp` - YouTube video/caption downloader
- Will proceed to: ffmpeg → whisper → graphify → Obsidian

## ⬜ Remaining Steps (to run in Claude Code interface)

After system dependencies complete, open Claude Code and run these commands in order:

### 1. Add the Brain plugin to marketplace
```
/plugin marketplace add peleg-jpg/brain
```

### 2. Install the Brain plugin
```
/plugin install brain@brain
```

### 3. Initialize Brain (creates vault, installs starter notes, configures Claude Code)
```
/brain-init
```
This will:
- Create Obsidian vault at `~/obsidian-brain`
- Copy 146 starter study notes
- Copy 16 wiki master pages
- Build initial 614-node knowledge graph
- Create `~/.claude/brain-config.json`
- Merge framework rules into `~/.claude/CLAUDE.md`

### 4. (Optional) Install claude-mem plugin for session memory
```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem@thedotmack
```

### 5. (Optional) Initialize graphify for the vault
```
graphify install --platform claude
```

## What You'll Have When Done

- **YouTube Capture**: `/yt-capture` - Drop a YouTube URL to transcript and ingest
- **Vault Processing**: `/vault-ingest` - Turn raw captures into wiki notes
- **Knowledge Graph**: Visual map of concepts and links in Obsidian
- **Memory Management**: `/dream` - Auto-memory cleanup; `/harvest` - distill projects into wiki notes
- **Brain Health**: `/brain-doctor` - Weekly vault checkup
- **Session Search**: `transcript-memory` - Full-text search over all past Claude Code sessions

## Vault Structure
```
~/obsidian-brain/
├── _vault-index.md      # Navigation hub
├── _log.md              # Change log
├── raw/                 # Incoming video transcripts (processed → deleted)
├── wiki/                # Master pages (16 starter notes)
├── notes/               # Study notes (146 starter notes)
└── graphify-out/        # Knowledge graph visualization
```

## System Requirements Met
- ✅ macOS (arm64)
- ✅ Homebrew
- ⏳ yt-dlp, ffmpeg, whisper, graphify, Obsidian
