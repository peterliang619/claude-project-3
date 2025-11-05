# Security Monitor Game

An interactive text-based security monitor game where you control various systems across multiple rooms through security channels.

## Overview

You play as a security officer monitoring a facility through a multi-channel security system. Switch between different room cameras, control lights, doors, and security systems, and respond to various events and alerts.

## Features

- **5 Different Channels/Rooms**:
  - Channel 1: Main Office
  - Channel 2: Storage Room
  - Channel 3: Research Lab
  - Channel 4: Hallway A
  - Channel 5: Security Room

- **Interactive Controls** (per room):
  - Toggle Lights (ON/OFF)
  - Toggle Door Lock (LOCKED/UNLOCKED)
  - Toggle Camera (ACTIVE/INACTIVE)

- **Dynamic Events**:
  - Motion detection alerts
  - Temperature monitoring
  - Security breach warnings
  - Random events that require attention

- **Scoring System**:
  - Earn points for maintaining security
  - Keep cameras active
  - Manage temperature in sensitive areas
  - Keep doors locked when necessary
  - Respond to alerts promptly

## How to Play

### Starting the Game

```bash
python3 monitor_game.py
```

### Controls

- **[1-5]**: Switch between channels (rooms)
- **[L]**: Toggle lights in current room
- **[D]**: Toggle door lock in current room
- **[C]**: Toggle camera in current room
- **[W]**: Wait (advance time and trigger events)
- **[Q]**: Quit and see final score

### Game Tips

1. **Monitor All Channels**: Switch between channels regularly to check for alerts
2. **Watch for Alerts**: Rooms with ⚠️ need attention
3. **Motion Detection**: The 👁️ icon indicates motion detected in a room
4. **Temperature Control**: Keep the Research Lab between 19-21°C for bonus points
5. **Security Priority**: Keep Research Lab and Security Room doors locked
6. **Camera Coverage**: Keep cameras active for security points
7. **Advance Time**: Use [W] to progress through your shift and trigger events

### Scoring

Your score is calculated based on:
- Active cameras (+10 points per room)
- No active alerts (+5 points per room)
- Research Lab door locked (+15 points)
- Research Lab temperature in optimal range (+10 points)

## Game Objectives

- Maintain facility security throughout your shift
- Respond to alerts and events as they occur
- Keep critical systems operational
- Achieve the highest score possible

## Requirements

- Python 3.6 or higher
- Works on Linux, macOS, and Windows

## Example Gameplay

```
==============================================================
  🎮 SECURITY MONITOR SYSTEM v2.0
==============================================================
Time: 03:00 | Score: 125 | Current Channel: 3
==============================================================

  CHANNEL 3: RESEARCH LAB
==============================================================

Description: High-tech laboratory with sensitive equipment.

Status:
  Lights:      [ON ]
  Door:        [LOCKED  ]
  Camera:      [ACTIVE  ]
  Temperature: 20°C
  Motion:      [NONE    ]

Available Channels:
  [1] Main Office
  [2] Storage Room ⚠️
  [3] Research Lab
  [4] Hallway A 👁️
  [5] Security Room

Controls:
  [L] Toggle Lights
  [D] Toggle Door Lock
  [C] Toggle Camera
  [1-5] Switch Channel
  [W] Wait (advance time)
  [Q] Quit Game

Enter command:
```

## License

Open source - feel free to modify and enhance!

## Future Enhancements

Potential features for future versions:
- Save/load game state
- Multiple difficulty levels
- More rooms and channels
- Complex event chains
- Time-based challenges
- Achievement system
