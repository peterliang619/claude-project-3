#!/usr/bin/env python3
"""
Security Monitor Game
A text-based game where you manage security monitors across different rooms.
Control lights, doors, cameras, and respond to various events.
"""

import os
import time
import random
from typing import Dict, List, Optional


class Room:
    """Represents a room that can be monitored and controlled."""

    def __init__(self, name: str, channel: int, description: str):
        self.name = name
        self.channel = channel
        self.description = description
        self.lights_on = True
        self.door_locked = False
        self.camera_active = True
        self.temperature = random.randint(18, 24)
        self.motion_detected = False
        self.alert = None
        self.events = []

    def toggle_lights(self) -> str:
        self.lights_on = not self.lights_on
        status = "ON" if self.lights_on else "OFF"
        return f"Lights turned {status} in {self.name}"

    def toggle_door(self) -> str:
        self.door_locked = not self.door_locked
        status = "LOCKED" if self.door_locked else "UNLOCKED"
        return f"Door {status} in {self.name}"

    def toggle_camera(self) -> str:
        self.camera_active = not self.camera_active
        status = "ACTIVE" if self.camera_active else "INACTIVE"
        return f"Camera {status} in {self.name}"

    def get_status(self) -> str:
        """Returns the current status of the room."""
        status = f"\n{'='*60}\n"
        status += f"  CHANNEL {self.channel}: {self.name.upper()}\n"
        status += f"{'='*60}\n\n"
        status += f"Description: {self.description}\n\n"
        status += f"Status:\n"
        status += f"  Lights:      [{'ON ' if self.lights_on else 'OFF'}]\n"
        status += f"  Door:        [{'LOCKED  ' if self.door_locked else 'UNLOCKED'}]\n"
        status += f"  Camera:      [{'ACTIVE  ' if self.camera_active else 'INACTIVE'}]\n"
        status += f"  Temperature: {self.temperature}°C\n"
        status += f"  Motion:      [{'DETECTED' if self.motion_detected else 'NONE    '}]\n"

        if self.alert:
            status += f"\n⚠️  ALERT: {self.alert}\n"

        if self.events:
            status += f"\nRecent Events:\n"
            for event in self.events[-3:]:  # Show last 3 events
                status += f"  • {event}\n"

        return status


class MonitorSystem:
    """Manages the security monitor system."""

    def __init__(self):
        self.rooms: Dict[int, Room] = {}
        self.current_channel = 1
        self.game_time = 0
        self.score = 0
        self.initialize_rooms()

    def initialize_rooms(self):
        """Initialize all rooms in the facility."""
        self.rooms[1] = Room(
            "Main Office",
            1,
            "A spacious office with desks and computers. The main hub of activity."
        )

        self.rooms[2] = Room(
            "Storage Room",
            2,
            "Shelves stacked with supplies and equipment. Dimly lit and quiet."
        )
        self.rooms[2].lights_on = False

        self.rooms[3] = Room(
            "Research Lab",
            3,
            "High-tech laboratory with sensitive equipment. Temperature controlled."
        )
        self.rooms[3].door_locked = True
        self.rooms[3].temperature = 20

        self.rooms[4] = Room(
            "Hallway A",
            4,
            "Long corridor connecting different sections. Motion sensors installed."
        )

        self.rooms[5] = Room(
            "Security Room",
            5,
            "Your current location. Banks of monitors and control panels."
        )
        self.rooms[5].door_locked = True

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('clear' if os.name != 'nt' else 'cls')

    def display_header(self):
        """Display the game header."""
        print("\n" + "="*60)
        print("  🎮 SECURITY MONITOR SYSTEM v2.0")
        print("="*60)
        print(f"Time: {self.game_time:02d}:00 | Score: {self.score} | Current Channel: {self.current_channel}")
        print("="*60 + "\n")

    def display_channel_list(self):
        """Display available channels."""
        print("\nAvailable Channels:")
        for channel, room in sorted(self.rooms.items()):
            alert_indicator = " ⚠️" if room.alert else ""
            motion_indicator = " 👁️" if room.motion_detected else ""
            print(f"  [{channel}] {room.name}{alert_indicator}{motion_indicator}")

    def display_controls(self):
        """Display available controls for current room."""
        print("\nControls:")
        print("  [L] Toggle Lights")
        print("  [D] Toggle Door Lock")
        print("  [C] Toggle Camera")
        print("  [1-5] Switch Channel")
        print("  [W] Wait (advance time)")
        print("  [Q] Quit Game")

    def switch_channel(self, channel: int) -> bool:
        """Switch to a different channel."""
        if channel in self.rooms:
            self.current_channel = channel
            return True
        return False

    def advance_time(self):
        """Advance game time and trigger random events."""
        self.game_time += 1
        self.trigger_random_events()

    def trigger_random_events(self):
        """Randomly trigger events in rooms."""
        # Random motion detection
        for room in self.rooms.values():
            if random.random() < 0.2:  # 20% chance
                room.motion_detected = not room.motion_detected
                if room.motion_detected and room != self.rooms[5]:
                    room.events.append(f"Motion detected at {self.game_time:02d}:00")

        # Random temperature changes
        for room in self.rooms.values():
            if random.random() < 0.3:  # 30% chance
                change = random.choice([-1, 1])
                room.temperature += change

        # Special events
        if self.game_time == 3 and not self.rooms[2].lights_on:
            self.rooms[2].alert = "Unusual activity detected in darkness"
            self.rooms[2].motion_detected = True

        if self.game_time == 5 and self.rooms[3].temperature > 22:
            self.rooms[3].alert = "Temperature exceeds safe threshold!"

        if self.game_time == 7 and not self.rooms[4].camera_active:
            self.rooms[4].alert = "Camera offline - security breach possible"
            self.rooms[4].motion_detected = True

        # Clear old alerts
        if self.game_time > 10:
            for room in self.rooms.values():
                if room.alert and random.random() < 0.3:
                    room.alert = None

    def calculate_score(self):
        """Calculate score based on security status."""
        score = 0
        for room in self.rooms.values():
            if room.camera_active:
                score += 10
            if not room.alert:
                score += 5
            if room.name == "Research Lab" and room.door_locked:
                score += 15
            if room.name == "Research Lab" and 19 <= room.temperature <= 21:
                score += 10
        return score

    def run(self):
        """Main game loop."""
        self.clear_screen()
        print("\n" + "="*60)
        print("  🎮 SECURITY MONITOR SYSTEM")
        print("="*60)
        print("\nWelcome, Security Officer!")
        print("\nYour job is to monitor multiple rooms via security channels.")
        print("Keep an eye on alerts, control room systems, and maintain")
        print("security throughout the facility.")
        print("\nPress Enter to begin your shift...")
        input()

        while True:
            self.clear_screen()
            self.display_header()

            current_room = self.rooms[self.current_channel]
            print(current_room.get_status())

            self.display_channel_list()
            self.display_controls()

            choice = input("\nEnter command: ").strip().upper()

            if choice == 'Q':
                final_score = self.calculate_score()
                self.clear_screen()
                print("\n" + "="*60)
                print("  SHIFT ENDED")
                print("="*60)
                print(f"\nTime Worked: {self.game_time} hours")
                print(f"Final Score: {final_score}")
                print("\nThank you for keeping the facility safe!")
                print("="*60 + "\n")
                break

            elif choice == 'L':
                result = current_room.toggle_lights()
                print(f"\n✓ {result}")
                current_room.events.append(result)
                time.sleep(1)

            elif choice == 'D':
                result = current_room.toggle_door()
                print(f"\n✓ {result}")
                current_room.events.append(result)
                time.sleep(1)

            elif choice == 'C':
                result = current_room.toggle_camera()
                print(f"\n✓ {result}")
                current_room.events.append(result)
                time.sleep(1)

            elif choice in ['1', '2', '3', '4', '5']:
                channel = int(choice)
                if self.switch_channel(channel):
                    print(f"\n✓ Switched to Channel {channel}")
                    time.sleep(0.5)
                else:
                    print("\n✗ Invalid channel")
                    time.sleep(1)

            elif choice == 'W':
                print("\n⏰ Time advancing...")
                self.advance_time()
                self.score = self.calculate_score()
                time.sleep(1)

            else:
                print("\n✗ Invalid command")
                time.sleep(1)


def main():
    """Main entry point for the game."""
    game = MonitorSystem()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!\n")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
