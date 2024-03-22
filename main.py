def on_sound_loud():
    basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

basic.show_icon(IconNames.ROLLERSKATE)

def on_forever():
    pass
basic.forever(on_forever)
