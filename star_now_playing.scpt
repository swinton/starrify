-- Check if Growl is running
tell application "System Events"
  set isRunning to (count of (every process whose bundle identifier is "com.Growl.GrowlHelperApp")) > 0
end tell

-- Get URI of current Spotify track 
tell application "Spotify"
	set theTrack to current track
	set theID to id of theTrack
	set theName to name of theTrack
	log theID
end tell

-- Star the track using Starrify
do shell script "/path/to/starrify.py -t" & theID & " -u YOUR_SPOTIFY_USERNAME -p YOUR_SPOTIFY_PASSWORD"

-- Confirm via Growl
if isRunning then
	tell application id "com.Growl.GrowlHelperApp"
		-- Make a list of all the notification types 
		-- that this script will ever send:
		set the allNotificationsList to ¬
			{"Starred Notification", "Test Notification"}
		
		-- Make a list of the notifications 
		-- that will be enabled by default.      
		-- Those not enabled by default can be enabled later 
		-- in the 'Applications' tab of the Growl preferences.
		set the enabledNotificationsList to ¬
			{"Starred Notification", "Test Notification"}
		
		-- Register our script with growl.
		-- You can optionally (as here) set a default icon 
		-- for this script's notifications.
		register as application ¬
			"Starrify" all notifications allNotificationsList ¬
			default notifications enabledNotificationsList ¬
			icon of application "Script Editor"
		
		--       Send a Notification...
		notify with name ¬
			"Starred Notification" title ¬
			"Track Starred" description ¬
			"You starred '" & theName & "'." application name "Starrify"
		
	end tell
end if
