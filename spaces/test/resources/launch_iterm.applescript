set currentWindow to ""
if application "iTerm" is not running then
  tell application "iTerm"
    activate
    delay 1
    set currentWindow to window 1
  end tell
else
  tell application "iTerm"
    set currentWindow to (create window with default profile)
  end tell
end if
tell application "iTerm"
  tell current session of currentWindow
    write text "123"
  end tell
  add_window("iTerm", currentWindow) of me
end tell
