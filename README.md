# busylight
DIY project to turn on a busy light when I am in a meeting.

## Installation
1. Clone this git repo
2. Change the `/Users/ricardostamato/pet_projects/busylight/camera_monitor.py` string in `com.rcstamato.busylight.plist` file to reflect the location of the camera_monitor.py file in your file system
3. Copy `com.rcstamato.busylight.plist` to `~/Library/LaunchAgents`
4. Run `launchctl load -w ~/Library/LaunchAgents/com.rcstamato.busylight.plist`

