import time
import sys

from pywinauto import ElementAmbiguousError, ElementNotFoundError
from pywinauto import application

# open new firefox window
app = application.Application(backend='uia').start(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# make sure the window opens
time.sleep(5)

# connect to new window
if app.windows():
  print('windows found')
  firefox = app.window(best_match='Mozilla Firefox')
else:
  print('try connect()')
  app = application.Application(backend='uia').connect(best_match='Mozilla Firefox')
  firefox = app.window(best_match='Mozilla Firefox')

# open bookmarks in container tab
try:
  folderName = sys.argv[1] if len(sys.argv) > 1 else 'startup'
  containerName = sys.argv[2] if len(sys.argv) > 2 else 'Social Media'

  # TODO: handle edge cases where folder or container elements are not found
  bookmarksToolbar = app['Mozilla Firefox']['BookmarksToolbar']
  startupFolder = bookmarksToolbar.child_window(best_match=folderName)
  startupFolder.click_input(button='right')
  toolbarMenu = app.MozillaFirefox.Menu
  toolbarMenu.OpenBookmarkInContainerTab.select()
  containerOption = toolbarMenu.child_window(best_match=containerName)
  containerOption.select()
  # TODO: close new tab that is not part of the container tabs

except (AttributeError, ElementAmbiguousError, ElementNotFoundError) as error:
  print(error)

sys.exit()