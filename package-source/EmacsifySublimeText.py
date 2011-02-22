import sublime_plugin, sublime, re

#
# Mimic Emacs Ctrl-o, which insert a newline after the cursor
# 
class InsertNewlineAfterCursorCommand(sublime_plugin.TextCommand):
  global marks 
  def run(self, edit, args=None):
    point = self.view.sel()[0].end()
    self.view.insert(edit, point, "\n")
    self.view.run_command("move", {"by": "characters", "forward": False})

#
# Expand selection to word part, then to the next word part etc., but 
# not beyond hard word limits. Uses "-", "_" and "." as soft delimiters.
# 
class IntelligentExpandSelection(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    start_pos = self.view.sel()[0].begin()
    end_pos = self.view.sel()[0].end()
    before = self.view.substr(start_pos - 1)
    after = self.view.substr(end_pos)
    soft_limits_pattern = re.compile('[-_.]')
    if re.match(soft_limits_pattern, after) != None:
      self.view.sel().add(sublime.Region(end_pos, end_pos + 1))
    if re.match(soft_limits_pattern, before) != None:
      self.view.sel().add(sublime.Region(start_pos - 1, start_pos))
    self.view.run_command("expand_selection", {"to": "word"})

#
# Perform LocalDeleteToMark if a mark is set, otherwise do IntelligentExpandSelection
# 
class ExpandOrKill(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    mark = self.view.get_regions("mark")
    if len(mark) == 0:
      self.view.run_command('intelligent_expand_selection')
    else:
      self.view.run_command('local_delete_to_mark')
  
#
# Cancel an existing mark, enable transient mode, set mark
# 
class LocalSetMark(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    self.view.run_command('local_cancel_mark')
    self.view.settings().set('transient_mode_on', True)
    self.view.run_command('set_mark')

#
# Delete to mark, disable transient mode, cancel mark
# 
class LocalDeleteToMark(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    self.view.run_command('delete_to_mark')
    self.view.settings().set('transient_mode_on', False)
    self.view.run_command('local_cancel_mark')

#
# Yank, then cancel the mark
# 
class LocalYank(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    self.view.run_command('yank')
    self.view.run_command('local_cancel_mark')

#
# Add region to kill ring, then cancel the mark
# 
class LocalAddToKillRing(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    self.view.run_command('add_to_kill_ring', {"forward": False})
    self.view.run_command('local_cancel_mark')

#
# Disable transient mode, cancel the mark, clear any selections
# 
class LocalCancelMark(sublime_plugin.TextCommand):
  def run(self, edit, args=None):
    self.view.settings().set('transient_mode_on', False)
    self.view.run_command('clear_bookmarks', {"name": "mark"})
    self.view.run_command('hide_panel')       # These don't appear
    self.view.run_command('hide_overlay')     # to do anything. Bug?
    regions = [s.b for s in self.view.sel()]
    self.view.sel().clear()
    for r in regions:
      self.view.sel().add(sublime.Region(r))

