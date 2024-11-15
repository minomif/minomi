let strip: neopixel.Strip = null
input.onButtonPressed(Button.A, function () {
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
    strip.showRainbow(1, 360)
})
input.onButtonPressed(Button.B, function () {
    strip.showRainbow(1, 180)
})
