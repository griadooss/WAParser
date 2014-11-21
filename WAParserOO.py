class Column:
    def __init__(self, attrib):
        self.pos = attrib[1]
        self.datatype = attrib[0]
   
    def __str__(self):
       return "Column is at position " + str(self.pos)
   
    def draw(self):
        pass
    
    def drag(self):
        pass
       
       
       
WAMap = { 'cust_id': [int, 1], 
         'first_name': [str, 2] }   

col1 = Column( WAMap['cust_id'] )
col2 = Column( WAMap['first_name'] )

print col1
print col2

# I am following along video 16_13_02 at time 08:00
# but that video uses SimpleGUI
# i have gone in search of how 
# to use either Tkinter or pygame
# Goto change the lines below to use Tk or pygame

def draw(canvas):
    pass

#create frame, labels and buttons
frame = simplegui.create_frame("WAParser", 400, 400)
frame.set_draw_handler(draw)

#start
frame.start()