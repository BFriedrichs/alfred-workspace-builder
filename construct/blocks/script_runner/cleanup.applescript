set windowString to read POSIX file "/Users/{user}/.currentWindows.txt" as text
set the text item delimiters to ","
set windowList to windowString's (text items 1 thru -2)

repeat with windowPair in windowList
  set the text item delimiters to "="
  set appName to the first text item of windowPair
  set windowId to the second text item of windowPair

  tell application appName
    try
      repeat with openWindow in windows
        if the (id of openWindow as string) is equal to windowId then
          close openWindow
        end if
      end repeat
    end try
  end tell
end repeat
