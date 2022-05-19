"""
LIST OF PROPOSED CHANGES AFTER OPEN SOURCED ON GITHUB:
-MELODY NUM INPUTS (1=LOW;7=HIGH) [low]
-CREATE README.md/txt WITH INFORMATION (FOLDER IN VGR) [high]
-BETTER DOCUMENTATION && COMMENTS [medium]
-POSSIBLE ASYNC? [rejected; unable to figure out how it works]
-RELEASE AS main.blocks/.py/.ts & COMPILED VERSION [high]
-^LARGER FILE; LESS TIME SPENT WAITING FOR SLOW COMPILATION [medium]
-TBA IN SECONDS [low]
-CONSTRAIN BYPASS -- MAYBE GOES OVER BLOCKS LIMIT? [low]
-OPTIMIZE CONSTRAIN - IF MORE NEEDED [low]
-OPTIMIZE BUTTON DEFS [low]
"""
# CONNECT BUZZER TO P0 AND GND; MODIFY BELOW WHERE STATED
# define what each button does

def on_button_pressed_a():
    global buttonValue, buttonPresses
    buttonValue += 1
    buttonPresses += 1
    if verbose == 1:
        print("a  " + str(buttonValue))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global buttonValue, buttonPresses
    buttonValue += 1000000
    buttonPresses += 1
    if verbose == 1:
        print("ab " + str(buttonValue))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global buttonValue, buttonPresses
    buttonValue += 1000
    buttonPresses += 1
    if verbose == 1:
        print("b  " + str(buttonValue))
input.on_button_pressed(Button.B, on_button_pressed_b)

buttonPresses = 0
shouldMusicPlay = 0
verbose = 0
buttonValue = 0
# \\MODIFY BELOW VALUES//
# LOG THINGS TO CONSOLE
verbose = 1
# TEST LIGHTLEVEL
llTest = 1
# TIME BEFORE ARM (MS/S*1000)
tba = 2000
# BUTTON PRESS COMBINATION
# A:1 B:1000 AB:1000000
value = 2002003
# PRESSES BEFORE RESET (0-999; clamped)
# this program can support 999 button presses.
# prevents going a certain amount of times
# after maxPresses + 1, it will reset.
maxPresses = 10
# THRESHOLD BEFORE
# 1-2 BOX, 14-25 FEW FEET FROM WINDOW (NOON), 190-210 MB FACING WINDOW (NOON)
lightLevel = 4
# VOLUME (0-255; clamped)
volume = 191
# TEMPO (unsure what upper limit is)
# in blocks w/ slider, max 500; can go past
tempo = 5000
# MELODY (CDEFGAB; C=LOW B=HIGH)
melody = "A F A F A F A F" + " "
# //END MODIFIED VALUES\\
# clamp presses
maxPresses = Math.constrain(maxPresses, 0, 999)
# clamp volume
volume = Math.constrain(volume, 0, 255)
# emu change light before run
b = input.light_level()
# wait so arming is possible + emu
basic.pause(tba)
while shouldMusicPlay == 0:
    if verbose == 1:
        print("Light level: " + str(input.light_level()))
    if input.light_level() > lightLevel:
        # bad workaround for auto 255 val (hardware)
        # break broke the script, and
        # if ((val > thrsh) && (val != 255)) didn't work
        if input.light_level() == 255:
            # slight delay so doesn't lag on emu console
            basic.pause(100)
        else:
            shouldMusicPlay = 1
while llTest == 1:
    print("Light level: " + str(input.light_level()))
    # Prevent having issues with console
    basic.pause(50)
while shouldMusicPlay == 1:
    music.set_volume(volume)
    music.play_melody(melody, tempo)
    if verbose == 1:
        print("DEBUG: Playing " + melody + "@" + str(tempo))
        # Slight pause, almost unnoticeable + reduce spam
        basic.pause(50)
    if buttonPresses > maxPresses:
        buttonValue = 0
        buttonPresses = 0
        basic.show_leds("""
                # # . . .
                # . # . .
                # # . . .
                # . # . .
                # . # . .
            """,
            250)
        # More efficient way to clrscrn
        basic.clear_screen()
        if verbose == 1:
            print("DEBUG: Reset buttonValue")
    if buttonValue == value:
        shouldMusicPlay += -1
if verbose == 1:
    print("DEBUG: Finished script")
