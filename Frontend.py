import tkinter.ttk
from Backend import SmartPlug, SmartHome, SmartWashingMachine
from tkinter import *

smart_home = SmartHome()
main_win = Tk()
# SP, C, SP, SP, C


def setup_home():
    plug1 = SmartPlug()
    smart_washing_machine = SmartWashingMachine()
    plug2 = SmartPlug()
    plug3 = SmartPlug()
    smart_washing_machine_2 = SmartWashingMachine()

    smart_home.add_device(plug1)
    smart_home.add_device(smart_washing_machine)
    smart_home.add_device(plug2)
    smart_home.add_device(plug3)
    smart_home.add_device(smart_washing_machine_2)
    # smart_home.add_device(smart_washing_machine_2)
    print(smart_home)


def main():
    setup_home()
    setup_main_win()


# main()




def turn_all_off():
    smart_home.turn_all_off()
    devices = len(smart_home.get_devices())

    for device in range(devices):
        item = smart_home.get_device_at(device)
        plug_out_text = Text(main_win, height=1, width=50)
        plug_out_text.insert("1.0", item)
        plug_out_text.grid(row=4 + device, column=0, sticky="w", padx=15)


def turn_all_on():
    smart_home.turn_on_all()
    devices = len(smart_home.get_devices())

    for device in range(devices):
        item = smart_home.get_device_at(device)
        plug_out_text = Text(main_win, height=1, width=50)
        plug_out_text.insert("1.0", item)
        plug_out_text.grid(row=4 + device, column=0, sticky="w", padx=15)


def add_device_command():

    def add_device():
        new_device = drop_box.get()
        smart_home.add_device_v2(new_device)
        number_of_device = smart_home.get_device_length()
        height = 500 * (number_of_device + 1)
        main_win.geometry("600x{}".format(height))

        setup_main_win()

    config_win = Toplevel()
    config_win.geometry("400x300")
    config_win.resizable(False, False)
    config_win.title("Add device")

    choose_device_label = Label(config_win, text="Choose device")
    choose_device_label.grid(row=0, column=0, padx=10, pady=10)

    device_list = ["Smart plug", "Custom"]
    drop_box = tkinter.ttk.Combobox(config_win, values=device_list)
    drop_box.grid(row=0, column=1, padx=10, pady=10)

    add_button = Button(config_win, text="+", command=add_device)
    add_button.grid(row=0, column=2, padx=10, pady=10)

    submit_btn = Button(config_win, text="Apply change", command=config_win.destroy)
    submit_btn.grid(row=1, column=1, padx=10, pady=10)


def setup_main_win():
    main_win.geometry("900x400")
    main_win.columnconfigure(index=0, weight=1)
    main_win.columnconfigure(index=1, weight=2)
    main_win.title("SmartHome-[🏠]")
    # main_win.resizable(False, False)
    label = Label(main_win, text="Smart Home", font="helvetica")
    label.grid(row=1, column=0, columnspan=3)

    # buttons

    turn_all_off_button = Button(main_win, text="Turn all off", padx=10, command=turn_all_off)
    turn_all_off_button.grid(row=2, column=0, sticky="w", padx=10)
    turn_all_on_button = Button(main_win, text="Turn all on", padx=10, command=turn_all_on)
    turn_all_on_button.grid(row=3, column=0, sticky="w", padx=10)

    add_new_device = Button(main_win, text="Add device", padx=10, command=add_device_command)
    add_new_device.grid(row=2, column=1, padx=10, pady=10)

    on_devices_label = Label(main_win, text=str(smart_home.get_devices_on_count()))
    on_devices_label.grid(row=2, column=2, padx=10, pady=10)

    for device_index in range(len(smart_home.get_devices())):
        item = smart_home.get_device_at(device_index)

        def toggle_individual(index=device_index):
            toggle_device_at(index)

        def config_command(index=device_index):
            config_window(index)

        def delete_at_index(index=device_index):
            delete_device_at(index)

        toggle_this_btn = Button(main_win, text="Toggle this 🔦", command=toggle_individual, background="black",
                                 foreground="white")
        toggle_this_btn.grid(row=4 + device_index, column=1, padx=10, pady=5, sticky="e")

        plug_out_text = Text(main_win, background="white", height=1, width=50)
        plug_out_text.insert("1.0", item)
        plug_out_text.grid(row=4 + device_index, column=0, sticky="w", padx=15)
        plug_out_text.config(state=DISABLED)

        config_btn = Button(main_win, text="Configure--⚙️", padx=10, command=config_command)
        config_btn.grid(row=4 + device_index, column=2, padx=10, pady=5)

        delete_btn = Button(main_win, text="Delete--🗑️", padx=10, command=delete_at_index)
        delete_btn.grid(row=4 + device_index, column=3, padx=10, pady=5)

    def delete_device_at(index):
        smart_home.remove_device(index)
        # removed_device = smart_home.get_device_at(index)
        # plug_out_text.config(text=str(removed_device))

        for removed_index in range(index):
            print("device number:", removed_index)

        plug_out_text.grid_remove()
        config_btn.grid_remove()
        toggle_this_btn.grid_remove()
        delete_btn.grid_remove()
        setup_main_win()

    # setup_main_win()

    def toggle_device_at(index):
        smart_home.toggle_switch(index)
        flipped = smart_home.get_device_at(index)
        plug_out_text.insert("1.0", flipped)
        setup_main_win()

        # fixed
        # how do I update the gui accordingly, at the moment it update the right values on one spot
        # plug_out_text.grid(row=4 + device_index, column=0, sticky="w", padx=15)

    def config_window(config_device_index):
        config_win = Toplevel()
        config_win.geometry("400x300")
        config_win.resizable(False, False)

        device = smart_home.get_device_at(config_device_index)
        config_win.title("configure {}".format(str(device)[0:6]))

        def update_btn_command():
            new_consumption_rate = int(modify_rates_entry.get())
            device.set_consumption_rate(new_consumption_rate)
            setup_main_win()

        def update_washing_machine():  # change to cbox
            # print(*option)
            new_mode = mode_entry.get()
            device.set_wash_mode_options(new_mode)
            setup_main_win()
            config_win.destroy()

            # # print(new_state)
            # device.set_wash_mode_options("0")

        if isinstance(device, SmartPlug):
            modify_rates = Label(config_win, text="consumption Rate:")
            modify_rates.grid(row=1, column=0, padx=15, pady=5, sticky="w")
            # var = StringVar()
            modify_rates_entry = Entry(config_win)
            modify_rates_entry.insert(0, str(device.get_consumption_rate()))
            modify_rates_entry.grid(row=1, column=1, padx=10, pady=10)

            cancel_btn = Button(config_win, text="Cancel", command=config_win.destroy)
            cancel_btn.grid(row=2, column=0, padx=10, pady=10)

            update_btn = Button(config_win, text="Update", command=update_btn_command)
            update_btn.grid(row=2, column=1, padx=10, pady=10)

            submit_btn = Button(config_win, text="Submit", command=config_win.destroy)
            submit_btn.grid(row=2, column=2, padx=10, pady=10)

        elif isinstance(device, SmartWashingMachine):
            modify_wash_mode = Label(config_win, text="Select Mode:")
            modify_wash_mode.grid(row=1, column=0, padx=15, pady=5, sticky="w")

            select = StringVar()
            select.set(device.set_wash_mode_options(0))

            options = ["Daily wash", "Quick wash", "Eco"]

            mode_entry = tkinter.ttk.Combobox(config_win, values=options)
            mode_entry.grid(row=1, column=1, padx=10, pady=10)

            cancel_config_btn = Button(config_win, text="Cancel", command=config_win.destroy)
            cancel_config_btn.grid(row=2, column=0, padx=10, pady=10)

            submit_mode_btn = Button(config_win, text="Update mode", command=update_washing_machine)
            submit_mode_btn.grid(row=2, column=1, padx=10, pady=10)

            destroy_btn = Button(config_win, text="Submit", command=config_win.destroy)
            destroy_btn.grid(row=2, column=2, padx=10, pady=10)

            # option = ["0", "1", "2"]
            # select_mode_menu = OptionMenu(config_win, select, *option)
            # select_mode_menu.grid(row=1, column=1, padx=10, pady=10)
            #
            # wash_mode_label = Label(config_win, text=device.get_wash_mode_options())
            # wash_mode_label.grid(row=1, column=2, padx=10, pady=10)
            #
            # update_btn = Button(config_win, text="Submit", command=update_washing_machine)
            # update_btn.grid(row=2, column=1, padx=10, pady=10)

        # wash mode selection
        # washmode = Entry(config_win)
        # washmode.insert(0, str(device.get))

    main_win.mainloop()


# setup_main_win()


if __name__ == "__main__":
    main()



