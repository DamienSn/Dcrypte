import string

letters = string.ascii_lowercase

class Code_lettres():
    def __init__(self, name, base, to):
        self.name = name
        self.code = [base, to]
        self.index = letters.index(self.code[1])
        self.letters = letters[self.index:len(letters)] + letters[0:self.index]

    def get_letters(self):
        return self.letters

    def get_code(self):
        return self.code

    def encoder(self, msg):
        output = ""
        for letter in msg:
            if letter not in letters:
                output += letter
            else:
                output += self.letters[letters.index(letter)]

        return output

    def decoder(self, msg):
        output = ""
        for letter in msg:
            if letter not in letters:
                output += letter
            else:
                output += letters[self.letters.index(letter)]

        return output

class Code_chiffres():
    def __init__(self, name, base, to):
        self.name = name
        self.code = [base, to]
        self.index = letters.index(base)
        self.chiffres = self.init_chiffres()
        self.letters = letters[self.index:len(letters)] + letters[0:self.index]

    def init_chiffres(self):
        output = []
        for i in range(self.code[1], 27):
            output.append(i)
        for i in range(1, self.code[1]):
            output.append(i)
        return output

    def get_chiffres(self):
        return self.chiffres

    def encoder(self, msg):
        output = ""
        for letter in msg:
            if letter not in letters:
                output += letter
                output += "/"
            else:
                index = self.letters.index(letter)
                output += str(self.chiffres[index])
                output += "/"
        return output

    def decoder(self, msg):
        msg = msg.split("/")
        output = ""
        for number in msg:
            try:
                index = self.chiffres.index(int(number))
                output += self.letters[index]

            except ValueError:
                output += number

        return output
