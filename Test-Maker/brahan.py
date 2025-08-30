# -*- coding: utf-8 -*-
"""
brahan: Var = brahan.brahan(text:need 'str')

brahan.NamedVar: Var.NamedVar(set:need empty,set:need empty)
"""

class brahan:
    def __init__(self,text):
        self.text = text
    def ListHashCharecter(self):
        catch = []
        for cit in self.text:
            
            divice = hash(self.text)
            catch.append(divice)
        return catch
    def LetToRad(self):
        chenge = []
        _lett_ = dict(a ='1',b = '5',c='3',d='4',e='2',f='7',g='6',h='8',i='9',
                      j='0',k='<',l='>',m='*',n='@',o='=',p=';',q="ه",r='~',s='#',t='!',
                      u='"',v="'",w='$',x='`',y='/',z='-',A =':',B = '^',C='&',
                      D='(',E=')',F='7',G='_',H='Ä',I='+'
                      ,J='.',K='[',L=']',M='{',N='}',O='\\',P=',',Q='ح',R='?',S='×',T='÷',
                      U='«',V="»",W='ء',X='î',Y='Å',Z='Æ')
        _lett_[' ']=' '
    
        for istr in self.text:
            try:
                chenge.append(_lett_[istr])
            except:
                f = []
        return ''.join(chenge)
    def RadToLet(self):
        chenge = []
        _lett_ = {'1':'a','5':'b','3':'c', '4':'d', '2':'e', '7':'f','6':'g','8':'h','9':'i',
                      '0':'j','<':'k','>':'l','*':'m','@':'n','=':'o',';':'p','~':'r','ه':'q','#':'s','!':'t',
                      '"':'u',"'":'v','$':'w','`':'x','/':'y','-':'z',':':'A','^':'B','&':'C',
                      '(':'D',')':'E','7':'F','_':'G','Ä':'H','+':'I'
                      ,'.':'J','[':'K',']':'L','{':'M','}':'N','\\':'O',',':'Q','?':'R','×':'S','÷':'T',
                      '«':'U',"»":'V','ء':'W','î':'X','Å':'Y','Æ':'Z'}
        _lett_[' ']=' '
        for istr in self.text:
            try:
                chenge.append(_lett_[istr])
            except:
                f = []
        return ''.join(chenge)
    def NamedVar(self,data1:set,data2:set):
        xcd1 = len(data1)
        xcd2 = len(data2)
        self.data1 = tuple(data1)
        self.data2 = tuple(data2)
        if xcd1 != xcd2:
            raise ValueError("Values are not equal.:(")
    def Open(self,arg):
        try:
            tare = self.data1.index(arg)
            return self.data2[tare]
        except:
            raise IndexError(f'tuple.index("{arg}"): "{arg}" not in tuple.:(')
    def Show(self):
        for icon in range(len(self.data1)):
            print(f'{self.data1[icon]} = {self.data2[icon]}')
    def To(self,numb:int):
        try:
            rot = self.data1[numb],self.data2[numb]
            return rot
        except:
            raise IndexError('Index out of range.:(')
    def Addset(self,key,val):
        ld1 = list(self.data1)
        ld2 = list(self.data2)
        ld1.append(key)
        ld2.append(val)
        self.data1 = tuple(ld1)
        self.data2 = tuple(ld2)
        self.Show()
    def Removeset(self,key):
        ld1 = list(self.data1)
        ld2 = list(self.data2)
        end = ld1.index(key)
        ld1.remove(key)
        ld2.remove(ld2[end])
        self.data1 = tuple(ld1)
        self.data2 = tuple(ld2)
        self.Show()
    def MovementByIndex(self,index):
            ld1 = list(self.data1)
            ld2 = list(self.data2)
            c = ld1[index]
            ld1[index] = ld2[index]
            ld2[index] = c
            self.data1 = tuple(ld1)
            self.data2 = tuple(ld2)
            self.Show()
    def MovementByKey(self,Key):
        ld1 = list(self.data1)
        ld2 = list(self.data2)
        index = ld1.index(Key)
        c = ld1[index]
        ld1[index] = ld2[index]
        ld2[index] = c
        self.data1 = tuple(ld1)
        self.data2 = tuple(ld2)
        self.Show()
    def MoveAll(self):
        for index in range(len(self.data1)):
            ld1 = list(self.data1)
            ld2 = list(self.data2)
            c = ld1[index]
            ld1[index] = ld2[index]
            ld2[index] = c
            self.data1 = tuple(ld1)
            self.data2 = tuple(ld2)
        self.Show()
    def Replace(self,key,val):
        ld1 = list(self.data1)
        ld2 = list(self.data2)
        index = ld1.index(key)
        ld2[index] = val
        self.data1 = tuple(ld1)
        self.data2 = tuple(ld2)
        self.Show()
    def Keys(self):
        return self.data1
    def Vals(self):
        return self.data2
    def Popset(self):
        ld1 = list(self.data1)
        ld2 = list(self.data2)
        ld1.pop()
        ld2.pop()
        self.data1 = tuple(ld1)
        self.data2 = tuple(ld2)
        self.Show()
    
    
        