#!/usr/bin/env python
import time
import pyautogui

# On the harp:
# 1 = C
# 2 = D
# 3 = E
# 4 = F
# 5 = G
# 6 = A
# 7 = B
# 8 = C

class Conductor:

    octave_map = {
            '(': lambda self: self._SwitchUp(),
            ')': lambda self: self._SwitchDown(),
            '[': lambda self: self._SwitchDown(),
            ']': lambda self: self._SwitchUp(),
            }

    interval_map = {
            '.': 4/4,
            ';': 2/4,
            ',': 1/4,
            ':': 1/8,
            '"': 1/16,
            '!': 1/32,
            }

    current_interval = 1/4

    in_chord = False
    chord_stack = []

    def __init__(self, tempo=60):
        self.tempo = tempo
        self.pausemap = { -1: 0.05,
                1: 0.075,
                2: 0.125,
                3: 0.25,
                4: 0.5,
                5: 1,
                }

    def _ConvertToNote(self, n):
        return {1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'z',
                7:'x',
                8:'c'}[n]

    def _SwitchUp(self):
        pyautogui.typewrite('r')

    def _SwitchDown(self):
        pyautogui.typewrite('v')

    def _PlayChord(self):
        notes = [self._ConvertToNote(int(c)) for c in self.chord_stack]
        pyautogui.hotkey(*notes)
        self.chord_stack = []
        self._Wait()
        self.in_chord = False

    def _PlayNote(self, n):
        pyautogui.press(self._ConvertToNote(n))
        self._Wait()

    def Play(self, piece):
        time.sleep(1)
        for c in piece:
            if c in self.interval_map: # interval signature
                self.current_interval = self.interval_map[c]
            elif c in self.octave_map:
                self.octave_map[c](self)
            elif c is '<': # chord
                self.in_chord = True
            elif c is '>': # end chord
                self._PlayChord()
            elif c is ' ':
                self._Wait()
            elif self.in_chord:
                self.chord_stack.append(c)
            else:
                self._PlayNote(int(c))

    def _Wait(self):
        time.sleep(self.current_interval*(60/self.tempo))

    def SetTempo(self, new_tempo):
        self.tempo = new_tempo


def MorrowindTheme():
    c = Conductor(70)
    song = ',678 (123 352 321)76 678 (123 356 5 76) (6 78, 7 6 5 654 3 2) (132) 876'
    c.Play(song)

def OdeToTheJoy():
    c = Conductor(40)
    song = '6678876544566" ,55 6678876544565" 44; ,55645:67,65 5:67,65 45;1,6678876544565" 44'
    c.Play(song)

def SugarPlumFairy():
    c = Conductor(70)
    song = '7576 4 5 444 333 222 25352'
    c.Play(song)

def TerraTheme(): # To be improved
    c = Conductor(80)
    song = ':5" :6" :7" :(2" ).6:6" :5" ;6, ;2, '
    song += ':5" :6" :7" :(2" ).6:6" :5" ;6, ;(2), '
    song += ':7" :8" :(2" :4" :2)" :8" :7" ;8, .4,76.5,76.5'
    
    #765765–567(2)7–6562–567(2)7–656(2)–78(242)–8784–765765–78(242)–8784–78(242)–878(4)–567(2)7–6562–765765'
    c.Play(song)

def FF9YouAreNotAlone():
    c = Conductor(70)
    song = ',8: ,6 56;3, :8" :8" :8" ,7: ,6: ,5: ,7;3'
    song += '(,3: ,3: ,3: ,2: ,1: ),8: ,7: ,6: ,7:87,6: .7'
    song += ',8: ,6 56;3, :8" :8" :8" ,7: ,6: ,5: ,7;(3)'
    song += '(,3: ,3: ,3: ,2: ,1: ),8: ,7: ,6: ,8:76,5: .6'
    song += ',876 (6 5 31 2 22 123)6 666 8(23 8 .7)'
    song += ',(65678 532 22 123)6 6 787 ;5.6'
    song += ',876 (6 5 31 2 22 123)6 666 8(23 8 .7)'
    song += ',(65678 532 22 123)6 6 787 .5 .<631>'
    c.Play(song)

def GoTTheme(): # to be fixed
    c = Conductor(60)
    song = '513451342472347321'
    c.Play(song)

def EarthGodLyric():
    c = Conductor(60)
    song = '5 <135> (13 21) 7 <468> 64 8686 <457> 54 8 <46> 7 <358> (23 12)'
    song += '<135> 5 <135> (13 21) 7 <468> 64 8686 <257> 8 <57>( 342) 78 <358>'
    c.Play(song)

def CorridorsOfTime():
    c = Conductor(60)
    song = '1367(3) 367(2) 367(3) 367'
    song += '1367(3) 367(2) 367(3) 367'
    song += '1367(3) 367(2) 367(3) 367'
    song += '1367(3) 367(2) 367(3) 367'
    song += '4 <62> <62> <52> <52> 567876 <53> <53> <42> <42>'
    song += '4 <62> <62> <52> <52> 456 7 <62> <62> <75> <75>'
    song += '5 61456 7 8 <75>'
    song += '25678 7 <75> <63> <63>'
    c.Play(song)

def MonkeyIslandTheme():
    c = Conductor(50)
    song = '   (:<42>"<42>! "<42>! : "<42>! "<42>! : "<31>! "<31>! : "<42>! "<42>! : "<42>! "<42>! '
    song += ': "<31>! "<31>! : "<42>! "<42>!'
    song += ':2"2432:1,2: 1")876(2:1" :1" ,)7: (:2" :2" 432:1,2:2" 3:4" :4" ,5'
    song += ':3" 43213:4" :4" ,3:2" 43213:4" :4" ,3:2" 432:12" :2" ,2: 2)"8768:7" :7" ,6'
    song += '. :68(8,4,4"8768:74,4:) ,6(:4511" 56545:<46><34>" :<24>)6" ,6'
    song += ':34"5375(3)7(53)75(3)7(5374:<42>2" :2" 4:3" :4" 3424)'
    song += '"4[7]42747(2)74(2)7(4247'
    song += ':13" :3" 3:2" :3" 23:1'
    song += ':2" 2432:1" ,2:) 8"8768:7" :7" ,6:( :2" :2" 432:1,2:2" 3:4" :4" ,5'
    song += ':3" 43213:4" :4" ,3:2" 43213:4" :4" ,3:2" 432:12" :2" ,2:) 8"76:7'
    song += '6,( :2" :2" 432:1222" 45435423.2)'
    c.Play(song)
