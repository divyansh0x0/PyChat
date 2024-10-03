import dearpygui.dearpygui as dpg
from pychat_network import Client
resizing_window = False
_initialized = False
delta_width = 17  # UI design: viewport width - non-primary window width
delta_height = 43
viewport_width = 0
viewport_height = 0
sidebar_width = 200
title_bar_height = 30

close_btn, min_btn = 0, 0
window, chat_window, sidebar = 0, 0, 0
add_client_btn, send_message_btn = 0, 0
text_box = 0
client_name_field, client_ip_field = 0, 0
button_client_dictionary = {}
client_chat_dictionary = {}
last_window_pos = [0, 0]

last_viewport_pos = [0,0]

def close_window():
    print("Closing window")
    dpg.stop_dearpygui()



def mouse_released():
    global resizing_window
    resizing_window = False

def save_viewport_location():
    global last_viewport_pos
    
    last_viewport_pos = dpg.get_viewport_pos()

def move_viewport(a,delta):
    global resizing_window
    if resizing_window:
        return
    print(a,delta)
    global last_window_pos
    delta_x = delta[1]
    delta_y = delta[2]

    dpg.set_viewport_pos([last_viewport_pos[0] + delta_x, last_viewport_pos[1] + delta_y])




def resize_viewport():
    global resizing_window, viewport_width, viewport_height, last_window_pos, last_viewport_pos
    resizing_window = True
    curr_window_pos = dpg.get_item_pos(window)
    delta_x = curr_window_pos[0] - last_window_pos[0]
    delta_y = curr_window_pos[1] - last_window_pos[1]
    dpg.set_item_pos(window,last_window_pos)
    last_viewport_pos = dpg.get_viewport_pos()
    last_viewport_pos[0] += delta_x
    last_viewport_pos[1] += delta_y
    viewport_width = dpg.get_item_width(window)
    viewport_height = dpg.get_item_height(window)
    dpg.set_viewport_width(viewport_width)
    dpg.set_viewport_height(viewport_height)
    dpg.set_viewport_pos(last_viewport_pos)
    last_window_pos = dpg.get_item_pos(window)


def update_bounds():
    if not _initialized:
        return
    add_client_btn_pos = dpg.get_item_pos(add_client_btn)
    add_client_btn_size = dpg.get_item_rect_size(add_client_btn)
    sidebar_size = dpg.get_item_rect_size(sidebar)
    
    send_msg_btn_pos = dpg.get_item_pos(send_message_btn)
    send_msg_btn_size = dpg.get_item_rect_size(send_message_btn)

    chatview_size = dpg.get_item_rect_size(chat_window)
    dpg.set_item_pos(add_client_btn, [add_client_btn_pos[0], sidebar_size[1] - add_client_btn_size[1]])
    dpg.set_item_pos(send_message_btn, [chatview_size[0] - send_msg_btn_size[0], chatview_size[1] - send_msg_btn_size[1]])


def init():
    dpg.create_context()

    # dpg.create_viewport(title='PyChat', resizable=False, decorated=False, width=800, height=600)
    # # the order of execution of following function matters, do not change them
    # dpg.setup_dearpygui()
    # dpg.show_viewport()
    # dpg.start_dearpygui()
    # dpg.destroy_context()
    # add_callbacks()
    print('Starting dpg')

    dpg_thread_on = True

    dpg.create_context()
    dpg.create_viewport(title='PyChat', decorated=False, width=600, height=200)
    dpg.setup_dearpygui()

    global _initialized
    _initialized = True


def submit_client(client: Client):
    button_id = create_client_button(client.name)
    chat_window_id = create_client_chat_window(client)

    button_client_dictionary[button_id] = client
    client_chat_dictionary[client] = chat_window_id


def create_client_chat_window(client):
    return dpg.child_window(pos=(sidebar_width, 0), height=-1, border=False)


def create_client_button(content):
    if not _initialized:
        return

    return dpg.add_button(label=content, parent=window)


def add_callbacks():
    dpg.set_viewport_resize_callback(update_bounds)


def apply_themes():
    # following code styles and themes for the component
    with dpg.theme() as main_window_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
            # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (100, 150, 100), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    with dpg.theme() as side_bar_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0, category=dpg.mvThemeCat_Core)

    with dpg.theme() as chat_window_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (21, 21, 21), category=dpg.mvThemeCat_Core)

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    dpg.bind_item_theme(window, main_window_theme)
    dpg.bind_item_theme(sidebar, side_bar_theme)
    dpg.bind_item_theme(chat_window, chat_window_theme)


def show():
    if not _initialized:
        raise RuntimeError("GUI has not been initialized")
    global window, chat_window, sidebar, add_client_btn, close_btn, running, min_btn,send_message_btn

    with dpg.window(label="Main", no_title_bar=True, no_move=True, no_resize=False, min_size=[600, 400]) as window:
        # dpg.set_primary_window(window, True)
        with dpg.group(horizontal=True):
            close_btn = dpg.add_button(label="close", callback=close_window)
            min_btn = dpg.add_button(label="minimize", callback=dpg.minimize_viewport)
        with dpg.handler_registry():
            dpg.add_mouse_drag_handler(button=dpg.mvMouseButton_Left, callback=move_viewport)
            dpg.add_mouse_down_handler(button=dpg.mvMouseButton_Left, callback=save_viewport_location)
            
            dpg.add_mouse_release_handler(button=dpg.mvMouseButton_Left, callback=mouse_released)
            # dpg.add_mouse_move_handler(callback=move_viewport)
        # Resize handler for window
        with dpg.item_handler_registry() as resize_handler:
            dpg.add_item_resize_handler(callback=resize_viewport)
            dpg.bind_item_handler_registry(window, resize_handler)

        with dpg.group(horizontal=True):
            # side bar
            with dpg.child_window(width=sidebar_width, autosize_y=True, border=False,
                                  autosize_x=False) as sidebar:
                add_client_btn = dpg.add_button(label="Add New", width=-1, height=30)
                # sets the theme for sidebar
            # text area
            with dpg.child_window(height=-1, border=False) as chat_window:
                send_message_btn = dpg.add_button(label="send", height=30)
                # sets the theme for chatwindow
        apply_themes()
        add_callbacks()
        dpg.show_viewport()

        dpg.start_dearpygui()
        print('Stopping dpg')
        dpg.destroy_context()
        print('Destroyed context')
