def on_button_pressed_a():
    strip.show_rainbow(1, 360)
    basic.pause(100)
    strip.show_rainbow(10, 360)
    basic.pause(100)
    strip.show_rainbow(30, 360)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 25, NeoPixelMode.RGB)