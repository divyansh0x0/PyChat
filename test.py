import dearpygui.dearpygui as dpg

# define global variables to be used in the toggle function
maximized: bool = False
position: list
width: int
height: int


def toggle_function():
    # use global variables
    global maximized
    global position
    global width
    global height

    # When maximized the old values need to be set to the viewport again
    if maximized:
        # proposal: make some sort of function to make windows/any OS aware of the not maximized state
        dpg.set_viewport_pos(position)
        dpg.set_viewport_width(width)
        dpg.set_viewport_height(height)

    # Store the values for future use if we want to get back from maximize
    else:
        position = dpg.get_viewport_pos()
        width = dpg.get_viewport_width()
        height = dpg.get_viewport_height()

        dpg.maximize_viewport()

    # set the maximized state to the negative of the current state
    #   so on the next button click, this value can be used properly
    maximized = not maximized
    print(maximized)


dpg.create_context()
dpg.create_viewport(title='Maximize toggle', width=300, height=300)

with dpg.window(label="Maximize test window", tag="PrimaryWindow"):
    dpg.add_text("Toggle Maximize Test")
    dpg.add_button(label="Toggle me!", callback=toggle_function)

dpg.set_primary_window("PrimaryWindow", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()