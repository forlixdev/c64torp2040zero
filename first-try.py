import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Inizializza la tastiera USB
kbd = Keyboard(usb_hid.devices)

# Definisci i pin di colonne e righe secondo lo schema hardware
col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)

# Crea la matrice hardware. Questo gestisce il debouncing in automatico
matrix = keypad.KeyMatrix(row_pins, col_pins)

# Mappatura dei 64 tasti della matrice C64 ai codici USB standard del PC.
# L'ordine è: Riga 0 (Col0...Col7), Riga 1 (Col0...Col7), e così via.
keymap = [
    # Riga 0
    Keycode.BACKSPACE, Keycode.RETURN, Keycode.RIGHT_ARROW, Keycode.F7, Keycode.F1, Keycode.F3, Keycode.F5, Keycode.DOWN_ARROW,
    # Riga 1
    Keycode.THREE, Keycode.W, Keycode.A, Keycode.FOUR, Keycode.Z, Keycode.S, Keycode.E, Keycode.LEFT_SHIFT,
    # Riga 2
    Keycode.FIVE, Keycode.R, Keycode.D, Keycode.SIX, Keycode.C, Keycode.F, Keycode.T, Keycode.X,
    # Riga 3
    Keycode.SEVEN, Keycode.Y, Keycode.G, Keycode.EIGHT, Keycode.B, Keycode.H, Keycode.U, Keycode.V,
    # Riga 4
    Keycode.NINE, Keycode.I, Keycode.J, Keycode.ZERO, Keycode.M, Keycode.K, Keycode.O, Keycode.N,
    # Riga 5
    Keycode.MINUS, Keycode.P, Keycode.L, Keycode.EQUALS, Keycode.PERIOD, Keycode.SEMICOLON, Keycode.LEFT_BRACKET, Keycode.COMMA,
    # Riga 6
    Keycode.RIGHT_BRACKET, Keycode.BACKSLASH, Keycode.QUOTE, Keycode.HOME, Keycode.RIGHT_SHIFT, Keycode.GRAVE_ACCENT, Keycode.APOSTROPHE, Keycode.SLASH,
    # Riga 7
    Keycode.ONE, Keycode.ESCAPE, Keycode.LEFT_CONTROL, Keycode.TWO, Keycode.SPACE, Keycode.LEFT_GUI, Keycode.Q, Keycode.LEFT_ALT
]

print("Tastiera C64 USB Avviata!")

# Ciclo principale infinito
while True:
    # Controlla se c'è un evento nella matrice (tasto premuto o rilasciato)
    event = matrix.events.get()
    
    if event:
        # Recupera il tasto USB mappato per l'incrocio premuto
        usb_keycode = keymap[event.key_number]
        
        if event.pressed:
            kbd.press(usb_keycode)
            # print(f"Premuto: Indice {event.key_number} -> Codice USB {usb_keycode}")
            
        elif event.released:
            kbd.release(usb_keycode)
