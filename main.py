#------ INFO ------
# Creator: Lukas Lev
# Date: 08/05/2023
# Description: Using GUI python ligrary DearPyGUI and python classes i created character story ctreator

#----- IMPORT ------
import dearpygui.dearpygui as dpg
import plot
import PIL
import numpy
import array

#---- VARIABLES ----
viewport_width=1500
viewport_height=1000
gapX=100
gapY=100
window_height=viewport_height-gapY*2.2
char=''

#--- REGISTRY ---
#step1
img = plot.step1(); img.putalpha(255)
print(img.width)
img_step1 = array.array('f', numpy.frombuffer(img.tobytes(), dtype=numpy.uint8) / 255.0)
#step2
img = plot.step2(); img.putalpha(255)
print(img.width)
img_step2 = array.array('f', numpy.frombuffer(img.tobytes(), dtype=numpy.uint8) / 255.0)
#step3
img = plot.step3(); img.putalpha(255)
print(img.width)
img_step3 = array.array('f', numpy.frombuffer(img.tobytes(), dtype=numpy.uint8) / 255.0)
#step4
img = plot.step4(); img.putalpha(255)
print(img.width)
img_step4 = array.array('f', numpy.frombuffer(img.tobytes(), dtype=numpy.uint8) / 255.0)

#------ DPG ------
dpg.create_context()
dpg.create_viewport(title='Mandelbrot DearpyGui', width=viewport_width, height=viewport_height, resizable=False)

with dpg.texture_registry(show=True):
    dpg.add_raw_texture(width=img.width, height=img.height, default_value=img_step1, format=dpg.mvFormat_Float_rgba, tag="img_step1")
    dpg.add_raw_texture(width=img.width, height=img.height, default_value=img_step2, format=dpg.mvFormat_Float_rgba, tag="img_step2")
    dpg.add_raw_texture(width=img.width, height=img.height, default_value=img_step3, format=dpg.mvFormat_Float_rgba, tag="img_step3")
    dpg.add_raw_texture(width=img.width, height=img.height, default_value=img_step4, format=dpg.mvFormat_Float_rgba, tag="img_step4")

with dpg.window(label="Main Window", width=img.width+5, height=img.height+80,pos=(gapX,gapY),no_resize=True):
    with dpg.tab_bar():
        with dpg.tab(label="Step 1"):
            dpg.add_text("Gray scale", bullet=True)
            dpg.add_image("img_step1")
        with dpg.tab(label="Step 2"):
            dpg.add_text("HSV colors", bullet=True)
            dpg.add_image("img_step2")
        with dpg.tab(label="Step 3"):
            dpg.add_text("Smooth coloring", bullet=True)
            dpg.add_image("img_step3")
        with dpg.tab(label="Step 4"):
            dpg.add_text("Histogram coloring", bullet=True)
            dpg.add_image("img_step4")
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()