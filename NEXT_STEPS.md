# Brain Setup - Final Steps (Claude Code UI)

## ✅ System Setup Complete

All dependencies are installed and working:
- ✅ yt-dlp (YouTube downloader)
- ✅ ffmpeg (media processing)
- ✅ graphify (knowledge graph builder)
- ✅ Obsidian 1.13.7 (vault GUI)
- ⚠️ whisper (optional - only needed for videos without auto-captions)

The Brain plugin is already copied to `~/.claude/skills/brain/`

---

## ⬜ Remaining Steps - Run in Claude Code

**Open Claude Code and run these commands in the terminal or chat:**

### Step 1: Initialize the Brain (creates vault + config)
```
/brain-init
```

This will:
- Create Obsidian vault at `~/obsidian-brain`
- Copy 146 starter study notes
- Copy 16 wiki master pages
- Build initial knowledge graph
- Create `~/.claude/brain-config.json`
- Set up Claude Code hooks and auto-use rules

### Step 2: (Optional) Install claude-mem for session memory
```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem@thedotmack
```

### Step 3: Open Obsidian
Click on the Obsidian icon in Applications, then:
1. Click "Open folder as vault"
2. Navigate to `~/obsidian-brain`
3. Select it as your vault

---

## 🚀 After Setup Complete - How to Use Brain

### Capture a YouTube Video
```
/yt-capture https://www.youtube.com/watch?v=...
```
Claude will:
1. Download the video
2. Extract captions (or transcribe with Whisper)
3. Save transcript to `raw/` folder
4. Offer ingest options

### Process Captures into Wiki
```
/vault-ingest
```
Converts raw captures into permanent wiki notes, creates links, rebuilds knowledge graph.

### View Your Knowledge Graph
Open Obsidian and use the Graph View to see concepts and connections.

### Query Specific Topics
```
graphify query "machine learning"
```
Returns only notes connected to that topic (saves tokens!).

### Weekly Maintenance
```
/brain-doctor
```
Checks for:
- Broken wikilinks
- Stale graph
- Raw/ backlog
- Memory budget
- Auto-fixes safe issues, proposes others

### Distill Projects into Wiki
```
/harvest
```
After shipping a project, creates one evergreen note with lessons learned.

---

## 📁 Vault Structure

```
~/obsidian-brain/
├── _vault-index.md      # Navigation hub - start here
├── _log.md              # Change log of all vault edits
├── raw/                 # Incoming transcripts (deleted after ingest)
├── wiki/                # Master pages (permanent knowledge)
│   └── 16 starter pages on YouTube/content strategy
├── notes/               # Study notes (146 starter)
└── graphify-out/        # Knowledge graph visualization
    ├── graph.json       # Full graph data
    └── index.html       # Interactive graph viewer
```

---

## 🔧 Configuration

Brain config is stored in:
```
~/.claude/brain-config.json
```

Claude rules and auto-use triggers are in:
```
~/.claude/CLAUDE.md
```

---

## ⚡ Key Skills Available

| Command | Does | Auto-triggers on |
|---------|------|------------------|
| `/yt-capture` | Drop URL → transcript + ingest menu | "save this video", YouTube URL |
| `/vault-ingest` | Convert raw to wiki notes | "ingest this", "obsidian this" |
| `/graphify . --update` | Rebuild knowledge graph | After any vault edit |
| `graphify query "topic"` | Search notes by topic | "find notes on..." |
| `/brain-doctor` | Vault health check | "check my vault", Mondays |
| `/dream` | Clean up auto-memory | "clean my memory", budget exceeded |
| `/harvest` | Distill project → wiki note | "harvest this", "distill this" |
| `/brain-router` | Where should this memory go? | "remember this", corrections |

---

## 🎯 Next Steps

1. **Open Claude Code** and run `/brain-init`
2. **Wait** for vault creation (~1 min)
3. **Open Obsidian** and point to `~/obsidian-brain`
4. **Try it**: Drop a YouTube video URL in Claude with `/yt-capture`
5. **Explore**: Open Obsidian's Graph View to see the knowledge map

---

## 📚 Learn More

- Brain philosophy: `/Users/prag/Documents/Code/Claude/Projects/Brain/docs/philosophy.md`
- Workflow guide: `/Users/prag/Documents/Code/Claude/Projects/Brain/docs/workflow.md`
- All skills detailed: `/Users/prag/Documents/Code/Claude/Projects/Brain/SKILLS.md`
