import dearpygui.dearpygui as dpg

dpg.create_context()

title_bar_height = 30


#following code styles and themes for the component
with dpg.theme() as main_window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvInputInt):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (100, 150, 100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

with dpg.theme() as side_bar_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0, category=dpg.mvThemeCat_Core)

with dpg.theme() as chat_window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)  
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (21, 21, 21), category=dpg.mvThemeCat_Core)
              
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)


#Create a primary window item that will contain everything
#syntax for creating any item is "with dpg.<component>() as <name>:"
#then <name> can be passed to other gui related functions 
with dpg.window(label="Main", no_title_bar=True,) as window:
        dpg.bind_item_theme(window, main_window_theme)
        dpg.set_primary_window(window, True)
        with dpg.child_window(pos=(-1, 0), width=200, autosize_y=True, border=False, autosize_x=False) as sidebar:
            dpg.add_button(label="User 1", width=-1, height=30)
            #sets the theme for sidebar
            dpg.bind_item_theme(sidebar, side_bar_theme)
        

        with dpg.child_window( pos=(200, 0), height=-1, border=False) as chat_window:
            dpg.add_button(label="Button in chat window")
            #sets the theme for chatwindow
            dpg.bind_item_theme(chat_window, chat_window_theme)
#the parent of component can also be set explicitly
dpg.add_button(label="button2", parent=sidebar)
#viewport is what os creates on the screen
dpg.create_viewport(title='PyChat', width=800, height=600)
#the order of execution of following function matters, do not change them
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()