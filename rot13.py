class Rotary:
    def __inint__(self):
        self.__hint=''
        pass

    def SetHint(self,input):
        self.__hint=input

    def ShowHint(self):
        return self.__hint

    def TranslateHint(self):
        result=''
        for i in self.__hint:
            # After N or n shift to the left
            if (ord(i) >= ord('A') and ord(i)< ord('N')) or (ord(i)>=ord('a') and ord(i)<ord('n')):
                result += chr(ord(i)+13)
            elif (ord(i)>=ord('N') and ord(i)<=ord('Z')) or (ord(i)>=ord('n') and ord(i)<=ord('z')):
                result += chr(ord(i)-13)
            else:
                result += i
        self.__hint = result

hint='''Rirelguvat urer vf rapbqrq hfvat ebg13
Na byq ohg fgvyy npgviyl hfrq ebgnel rapbqvat, pna or hfrq nf onfr sbe bgure rapbqvatf'''

gc = Rotary()

gc.SetHint(hint)
gc.TranslateHint()
print(gc.ShowHint())

print(gc.__dict__)
