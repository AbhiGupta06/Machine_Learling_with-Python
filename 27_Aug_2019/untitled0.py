# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:37:33 2019

@author: BSDU
"""
import tkinter as tk
class GameBoard(tk.Frame):
    def __init__(x, parent, rows=8, columns=8, size=32, color1="white", color2="black"):
         x.rows = rows
         x.columns = columns
         x.size = size
         x.color1 = color1
         x.color2 = color2
         x.pieces = {}
         canvas_width = columns * size
         canvas_height = rows * size
         tk.Frame.__init__(x, parent)
         x.canvas = tk.Canvas(x, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height)
         x.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
         x.canvas.bind("<Configure>", x.refresh)
        
    def placepiece(x, name, row, column):
          x.pieces[name] = (row, column)
          x0 = (column * x.size) + int(x.size/2)
          y0 = (row * x.size) + int(x.size/2)
          x.canvas.coords(name, x0, y0)
          
    def refresh(x, event):      
             xsize = int((event.width-1) / x.columns)
             ysize = int((event.height-1) / x.rows)
             x.size = min(xsize, ysize)
             x.canvas.delete("square")
             color = x.color2
             
             for row in range(x.rows):
                  color = x.color1 if color == x.color2 else x.color2
                  for col in range(x.columns):
                      x1 = (col * x.size)
                      y1 = (row * x.size)
                      x2 = x1 + x.size
                      y2 = y1 + x.size
                      x.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                      color = x.color1 if color == x.color2 else x.color2
                      
             for name in x.pieces:
                x.placepiece(name,x.pieces[name][0], x.pieces[name][1])
             x.canvas.tag_raise("piece")
             x.canvas.tag_lower("square")
            
if __name__ == "__main__":
       root = tk.Tk()
       board = GameBoard(root)
       board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
       root.mainloop()

    