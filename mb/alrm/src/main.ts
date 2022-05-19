/**
 * LIST OF PROPOSED CHANGES AFTER OPEN SOURCED ON GITHUB:
 * -MELODY NUM INPUTS (1=LOW;7=HIGH) [low]
 * -CREATE README.md/txt WITH INFORMATION (FOLDER IN VGR) [high]
 * -BETTER DOCUMENTATION && COMMENTS [medium]
 * -POSSIBLE ASYNC? [rejected; unable to figure out how it works]
 * -RELEASE AS main.blocks/.py/.ts & COMPILED VERSION [high]
 * -^LARGER FILE; LESS TIME SPENT WAITING FOR SLOW COMPILATION [medium]
 * -TBA IN SECONDS [low]
 * -CONSTRAIN BYPASS -- MAYBE GOES OVER BLOCKS LIMIT? [low]
 * -OPTIMIZE CONSTRAIN - IF MORE NEEDED [low]
 * -OPTIMIZE BUTTON DEFS [low]
 */
// CONNECT BUZZER TO P0 AND GND; MODIFY BELOW WHERE STATED
// define what each button does
input.onButtonPressed(Button.A, function () {
    buttonValue += 1
    buttonPresses += 1
    if (verbose == 1) {
        console.log("a  " + buttonValue)
    }
})
input.onButtonPressed(Button.AB, function () {
    buttonValue += 1000000
    buttonPresses += 1
    if (verbose == 1) {
        console.log("ab " + buttonValue)
    }
})
input.onButtonPressed(Button.B, function () {
    buttonValue += 1000
    buttonPresses += 1
    if (verbose == 1) {
        console.log("b  " + buttonValue)
    }
})
let buttonPresses = 0
let shouldMusicPlay = 0
let verbose = 0
let buttonValue = 0
// \\MODIFY BELOW VALUES//
// LOG THINGS TO CONSOLE
verbose = 1
// TEST LIGHTLEVEL
let llTest = 1
// TIME BEFORE ARM (MS/S*1000)
let tba = 2000
// BUTTON PRESS COMBINATION
// A:1 B:1000 AB:1000000
let value = 2002003
// PRESSES BEFORE RESET (0-999; clamped)
// this program can support 999 button presses.
// prevents going a certain amount of times
// after maxPresses + 1, it will reset.
let maxPresses = 10
// THRESHOLD BEFORE
// 1-2 BOX, 14-25 FEW FEET FROM WINDOW (NOON), 190-210 MB FACING WINDOW (NOON)
let lightLevel = 4
// VOLUME (0-255; clamped)
let volume = 191
// TEMPO (unsure what upper limit is)
// in blocks w/ slider, max 500; can go past
let tempo = 5000
// MELODY (CDEFGAB; C=LOW B=HIGH)
let melody = "A F A F A F A F" + " "
// //END MODIFIED VALUES\\
// clamp presses
maxPresses = Math.constrain(maxPresses, 0, 999)
// clamp volume
volume = Math.constrain(volume, 0, 255)
// emu change light before run
let b = input.lightLevel()
// wait so arming is possible + emu
basic.pause(tba)
while (shouldMusicPlay == 0) {
    if (verbose == 1) {
        console.log("Light level: " + input.lightLevel())
    }
    if (input.lightLevel() > lightLevel) {
        // bad workaround for auto 255 val (hardware)
        // break broke the script, and
        // if ((val > thrsh) && (val != 255)) didn't work
        if (input.lightLevel() == 255) {
            // slight delay so doesn't lag on emu console
            basic.pause(100)
        } else {
            shouldMusicPlay = 1
        }
    }
}
while (llTest == 1) {
    console.log("Light level: " + input.lightLevel())
// Prevent having issues with console
    basic.pause(50)
}
while (shouldMusicPlay == 1) {
    music.setVolume(volume)
    music.playMelody(melody, tempo)
    if (verbose == 1) {
        console.log("DEBUG: Playing " + melody + "@" + tempo)
// Slight pause, almost unnoticeable + reduce spam
        basic.pause(50)
    }
    if (buttonPresses > maxPresses) {
        buttonValue = 0
        buttonPresses = 0
        // Modify to wanted reset grid
        basic.showLeds(`
            # # . . .
            # . # . .
            # # . . .
            # . # . .
            # . # . .
            `, 250)
        // More efficient way to clrscrn
        basic.clearScreen()
        if (verbose == 1) {
            console.log("DEBUG: Reset buttonValue")
        }
    }
    if (buttonValue == value) {
        shouldMusicPlay += -1
    }
}
if (verbose == 1) {
    console.log("DEBUG: Finished script")
}
