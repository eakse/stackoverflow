import gi
import os
from pprint import pprint


gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Pango


def print_something(data, settings=None, page_setup=None):
    if settings != None:
        print.set_print_settings( settings)
        
    if page_setup != None:
        print.set_default_page_setup(page_setup)
        
    print.connect( "begin-print", begin_print, data)
    print.connect("draw-page", draw_page, data)
       
    res = print.run(Gtk.PRINT_OPERATION_ACTION_PRINT_DIALOG, parent)
       
    if res == Gtk.gtkprint_OPERATION_RESULT_ERROR:
        error_dialog = Gtk.MessageDialog(parent,
                                         Gtk.DIALOG_DESTROY_WITH_PARENT,
                                         Gtk.MESSAGE_ERROR,
      	                        		 Gtk.BUTTONS_CLOSE,
      					                 "Error printing file:\n")
        error_dialog.connect("response", lambda w,id: w.destroy())
        error_dialog.show()
    elif res == Gtk.PRINT_OPERATION_RESULT_APPLY:
        settings = print.get_print_settings()
      

print_something("asdasda")
exit(0)


parent = Gtk.Window()

printers = os.popen("lpstat -e").read().strip().split("\n")
print(f"Available printers: {printers}")

printcontext = Gtk.PrintContext()
context = printcontext.create_pango_context()
layout = Pango.Layout.new(context)
layout.set_text("Hello!")
printsettings = Gtk.PrintSettings()


print(f"Printing to: {printers[1]}")
print()
printsettings.set_printer(printers[1])
printsettings.set_print_pages(Gtk.PrintPages.ALL)
printoperation = Gtk.PrintOperation().new()
printoperation.set_print_settings(printsettings)
# printoperation.set_job_name("jobby")
printoperation.set_n_pages(1)
result = printoperation.run(Gtk.PrintOperationAction.PRINT, parent)
# print(result.APPLY)
# pprint(dir(result))
print(f"Printing result: {result}")
