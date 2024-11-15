strip: neopixel.Strip = None

def on_button_pressed_a():
    global strip
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
    strip.show_rainbow(1, 360)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    strip.show_rainbow(1, 180)
input.on_button_pressed(Button.B, on_button_pressed_b)
