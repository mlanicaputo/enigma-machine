import string
from typing import Dict, List, Tuple

class Rotor:
    """A rotor for the enigma machine.
    Rotating the rotor moves the cipher alphabet +1
    in relation to the ascii alphabet."""
    notches: str
    num_notches: int
    position: int # NEED TO IMPLEMENT POSITIONAL BEHAVIOR
    # position is an int, the number of places the
    # rotor is offset from the origin
    subs: dict

    def __init__(self, cipher_alphabet: str, notches: str, num_notches: int) -> None:
        """A rotor for the enigma machine."""
        assert len(notches) == num_notches
        self.notch_letter = notch_letter
        self.num_notches = num_notches

        alphabet = string.ascii_lowercase
        cipher_alphabet = cipher_alphabet.lower()
        # TODO make sure that there are not other characters
        # cipher_alphabet = [letter for letter in cipher_alphabet if letter.isalpha()]
        # create the subs dict
        alph_list = list(alphabet)
        cipher_list = list(cipher_alphabet)
        self.subs = dict(zip(alph_list, cipher_list))

    def encode(self, letter: str) -> str:
        """Return an encoded letter."""
        return self.subs.get(letter)

    def input_letter(self, letter: str, prev_rotor_pos: int) -> str:
        """Change previous output letter to current input letter
        according to difference in rotor positions."""
        letter_int = ord(letter)
        letter_int += (self.position - prev_rotor_pos)
        # if the alphabet has been exceeded, subtract 26
        if letter_int > 122:
            letter_int -= 26
        # return the char associated with the ascii int
        return chr(letter_int)

    def shift(self, num_digits: int=1) -> None:
        """Shift the rotor by num_digits."""
        self.position += num_digits


class Reflector(Rotor):
    """A reflector rotor.

    Basically just another substitution rotor.

    Depending on the version, the Reflector:
    * could have between 2 and 26 possible positions
    * could step or not
    """
    
    def __init__(self):
        self.notches = None
        self.num_notches = 0


class Plugboard:
    """A plugboard."""
    # pairs of letters, encryption goes both directions
    key: Dict

    def __init__(self, connections: List[Tuple]):
        self.key = dict()
        for connection in connections:
            # TODO check that each connection is the right length and type
            # TODO check that connections contains no duplicates
            # TODO create a class for connections perhaps?
            letter1, letter2 = connection
            self.key.update({letter1: letter2, letter2: letter1})

    def substitute(self, input_letter: str) -> str:
        value = self.key.get(input_letter)
        # if the input letter has a connection in the key
        if value:
            return value
        
        return input_letter

    
class Enigma:
    """The Enigma machine."""
    ref: Reflector
    pb: Plugboard
    
    
    



def main():
    # r = Rotor("qwertyuiopasdfghjklzxcvbnm")
    # print(
    #     f"f: {r.encode('f')}\n"
    #     f"g: {r.encode('g')}\n"
    #     f"h: {r.encode('h')}\n"
    #     f"i: {r.encode('i')}\n"
    # )

    cns = [
        ("a", "b"),
        ("c", "d"),
        ("e", "f"),
        ("g", "h"),
        # ("i", "j"),
        # ("k", "l"),
        # ("m", "n"),
        # ("o", "p"),
        # ("q", "r"),
        # ("s", "t"),
        # ("u", "v"),
        # ("w", "x"),
        # ("y", "z")
    ]
    p = Plugboard(cns)
    print(p.substitute("a"))
    print(p.substitute("b"))
    print(p.substitute("y"))
    print(p.substitute("z"))


if __name__ == "__main__":
    main()



