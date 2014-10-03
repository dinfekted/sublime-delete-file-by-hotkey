import sublime
import sublime_plugin
import os

class DeleteCurrentFile(sublime_plugin.TextCommand):
  def run(self, edit):
    os.remove(self.view.file_name())

    # mark view "dirty"; otherwise sublime will not ask confirmation before
    # closing the file
    self.view.insert(edit, 0, ' ')
    self.view.replace(edit, sublime.Region(0, 1), '')

class RenameCurrentFile(sublime_plugin.TextCommand):
  def run(self, edit):
    file = self.view.file_name()

    sublime.active_window().show_input_panel("Enter new filename",
      os.path.basename(file), self._on_enter, None, None)

  def _on_enter(self, new_name):
    file = self.view.file_name()
    new = os.path.dirname(file) + '/' + new_name
    os.rename(file, new)
    window = self.view.window()
    window.run_command('close_file')
    window.open_file(new)