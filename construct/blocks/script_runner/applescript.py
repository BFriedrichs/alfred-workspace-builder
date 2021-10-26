import os
user = os.environ['USER']

extension = '.applescript'
wrapper = """
global windowList
set windowList to {brackets}

on add_window(applicationName, theWindow)
	set end of windowList to (applicationName & "=" & (the id of theWindow))
end add_window

on write_to_file(this_data, target_file, append_data) -- (string, file path as string, boolean)
  set f to open for access (POSIX file target_file) with write permission
  if append_data
    write this_data to f as "utf8" starting at eof
  else
    write this_data to f as "utf8"
  end if
  close access f
end write_to_file

{script}

set text item delimiters to ","
write_to_file((windowList as text) & ",", "/Users/{user}/.currentWindows.txt", true)
"""
