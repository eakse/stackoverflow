import STACK_1
import tk

root = tk.Tk()
root.title("N Body Simulation")
root.geometry('400x300')
app = STACK_1.MyApp(root)
root.mainloop()

planets = app.planets