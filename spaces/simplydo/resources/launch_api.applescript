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
    write text "workon api; a; yarn start"
  end tell
  tell currentWindow
    set newTab to (create tab with default profile)
    tell current session of newTab
      write text "workon api; a"
    end tell
  end tell
end tell
set end of windowList to (id of currentWindow)
