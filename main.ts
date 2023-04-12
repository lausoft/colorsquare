input.onButtonPressed(Button.A, function () {
    strip.rotate(5)
    strip.show()
})
input.onButtonPressed(Button.B, function () {
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(500)
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
    basic.pause(500)
    strip.showColor(neopixel.colors(NeoPixelColors.Blue))
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 25, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
