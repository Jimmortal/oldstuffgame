# -- coding: utf-8 --
#from future import unicode_literals
from Tkinter import *
import random
import re

from datetime import datetime

root = Tk()
root.configure(background='black')
txtleft = Text(root, width=30, height=30, bg='black', fg='#00fa00')
txtright = Text(root, width=90, height=30, bg='black', fg='#00fa00', wrap=WORD)
txtmenu = Text(root, width=40, height=30, bg='black', fg='#00fa00', wrap=WORD)
frame = Frame(root, bg='black', bd=1)
framed = Frame(root, bg='black', bd=1)

class personazh:
    def __init__(self, hp, ap, name, gold,xp,subname):
        self.subname = subname
        self.hp = hp
        self.ap = ap
        self.name = name
        self.maxhp = hp
        self.gold = gold
        self.xp = xp
        
class hero:
    def __init__(self, hp, ap, name, gold):
        self.lvl = 1
        self.xp = 0
        self.ap = ap 
        self.name = name
        self.maxhp = hp 
        self.hp = self.maxhp
        self.gold = gold
    def lvlxp(self):
        if self.xp > self.lvl*(10+self.lvl):
            self.lvl+=1
            self.maxhp += self.lvl*0.4
            self.ap+=self.lvl*0.3         
            
gnom = personazh(10, 3, '$',20,3,'гном')
ork = personazh(7, 2, '&',5,12,'орк')
goblin = personazh(14, 4, '!',30,6,'гоблин')
troll = personazh(20, 30, 'X',25,16,'тролль')
spider = personazh(4, 5, '#',5,3,'паук')
crabik = personazh(5, 3, '%',5,4,'земной краб')
wizard = personazh(8, 4, 'W',40,9,'чернокнижник')
traps = personazh(2, 3, 'T',0,1,'ловушка')
rndditme = personazh(0, 0, '@',0,0,'')
owgr = personazh(11, 4, '^',15,10,'огр')
probel = personazh(0, 0, ' ',0,0,'')
glav = hero(30, 4, 'HERO',100)

heroes = [owgr.name, gnom.name, goblin.name,
          ork.name, troll.name, spider.name,
          crabik.name, wizard.name, traps.name,
          rndditme.name, ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
free_replics = ['Не стой на месте, сделай что-нибудь\n','Не махай просто так этой штукой\n','Пора выдвигаться!\n',
                'Кто стоит на месте, тот не ест\n','Бой с тенью!\n','Погнали отсюда\n',
                'Тут больше ничего нет\n','Пока ты стоишь, другие идут!\n']

dg = 30
a = [[0] * dg for i in range(dg)]
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = random.choice(heroes)
        if i == 0 or j == 0 or i == dg - 1 or j == dg - 1:
            a[i][j] = '*'
        txtleft.insert(END, a[i][j])
    txtleft.insert(END, '\n')

codin = ['Из-за камня выскочил проклятый гном и отобрал у тебя 10 монет.\n',
         'Увидев гнома, вы уронили 10 монет. Гном естесственно их подобрал.\n',
         'Раньше говорили что гномы не воруют золото. И вам врали.\n',
         'Гномы не любят золото, когда оно находится не у них.\n',
         'Вы отдали гному 10 монет из-за жалости, но потом подумали и решили что здесь что-то не так.\n',
         'Вы любите раскидываться деньгами, особенно когда на вас напал гном.\n',
         'Каждый кто хоть раз видел гнома, потом никогда не видел свои запасы золота.\n',
         'Возможно вам сегодня повезло и вы встретили меньшее зло,а гном стал на 10 богаче.\n']
cdva = ['Злой орк напал сзади. Как бестактно.\n',
        'В старых сказказ рассказывали об орках как противных существах. Сказки не врали.\n',
        'Если это засада, то перед Вами орк. Иначе вам некуда бежать.\n',
        'Услышав орчий крик вы ринулись прямо к нему.\n',
        'Орчий оскал вас не напугал!\n',
        'Раньше здесь была безопасная дорога, а теперь она ещё и с орком.\n',
        'А теперь пора пнуть этого спящего орка и преподать ему урок!\n',
        'Кто боится орков, тот сидит дома!\n']
ctri = ['Маленький хитрый гоблин знает где вы прячите свою еду. Но теперь вы не знаете где прячет еду он.\n',
        'Прятать еду вы так и не научились. Поучитесь у гоблина.\n',
        'Если оставить еду как приманку, то можно поймать гоблина.\n',
        'Голодный гоблин решил поесть, но не вами, а вашими запасами.\n',
        'Вы решили поделиться едой с гоблином, дабы получить ответ. Еды нет, ответов тоже.\n',
        'У вас невероятно отличное зрение и заметили как гоблин вытащил еду из вашего рюкзака.\n',
        'У гоблинов всегда обед по расписанию. А вы как раз пришли вовремя!\n',
        'Из-за кустов прилетели камни, надо бы их проверить на наличие голодных гоблинов.\n']
cchet = ['Что это? Камень? Холм? Неа, это тролль. Большой и злобный\n',
         'Лежащие кости на дороге должны были служить предупрежденим для путников,что их скоро сожрёт тролль\n',
         'Ну как можно не заметить огромного вонючего тролля!?\n',
         'Возможно Вас сейчас сожрут.\n',
         'Кто-то говорил что жир тролля очень сильно ценится - пора это проверить!\n',
         '"Съесть или не съесть?" - размышлял тролль смотря на Вас.\n',
         'Приключения сами себя не напишут, поэтому пора бы пнуть этого тролля!\n',
         'Вдруг на дорогу выкатился огромный тролль. Такой акробатики ещё никто не видел.\n']
cpat = ['Договориться с огром вряд ли получиться. Он всё равно ничего не понимает.\n',
        'Если быть немножечко потише, то можно пройти мимо огра незамеченным,но кастрюля тебя выдаёт.\n',
        'Вы обладаете очень плохой памятью и уже забыли как выглядит огр.\n',
        '"В этих землях живут огры" - возможно это была ваша лучшая книга и скорей всего последняя.\n',
        'Говорили что будет очень весело если посетить огра.\n',
        'Огр не тролль, по-меньше всё-так в размерах.\n',
        'Кто сказал что огры не едят людей?\n',
        'Никто не любит огров. Даже вы.\n']
csix = ['Никто не любит пауков. Особенно гигантских.\n',
        'Пауки любят мух,всяких жучков и мошек, а так же невнимательных путников.\n',
        'В детских книгах пауки были не такие злые...\n',
        'Ну почему пауки всегда такие злые? Почему нельзя их сделать добрыми!?\n',
        'Если ничего не выйдет, то можно представлять себя бабочкой до конца своей жизни.\n',
        'Восемь конечностей, хватит ли смелости сделать их количество меньше?\n',
        'А паутина нынче дорогая!\n',
        'Как можно быть таким растяпой и запутаться в паутине?\n']
csevn = ['Земных крабов не существовало. До этого времени.\n',
         'Вы услышали треск клешен, но не видите воду. О нет! Земной краб.\n',
         'Что-то вцепилось Вам в ноге и не хочет отпускать. Ох как больно!\n',
         'Крабовое мясо очень вкусное, особенно настоящее.\n',
         'Шутки про клешни как никак актуальны!\n',
         'Раздавить краба не получилось, поэтому краб будет давить тебя.\n',
         'Ну почему ты не в воде!??\n',
         'Оказалось это всего лишь краб, а не паук.\n']
cvos = ['Чёрный балахон,длинная палка,противный запах. Старый колдун не любит гостей.\n',
        'Возможно этот старик вам поможет... поможет отправиться на тот свет!\n',
        'С первого раза Вас не услышали, давайте ещё раз крикнем этому чудаку в смешной шляпе.\n',
        'Надпись "Wizard" как бы предупреждает, но вы инностраных языков не понимаете.\n',
        'Помогать незнакомцам благое дело, но только если это не чёрный маг!\n',
        'Ум есть - сила не нужна. Нельзя недооценивать старого волшебника.\n',
        'Фокусы вас уже не удивляли, поэтому вы решили посетить злого колдуна.\n',
        '"Ну кто так колдует?" - кричали вы, убегая от молний мага.\n']
cdev = ['"Хм ловушка"- подумали Вы и наступили в неё.\n',
        'Да кто же так разбрасывается деньгами? О нет это же лову....шка.\n',
        'На земле лежит, но никто не поднимает - Довольно странно?\n',
        '"Всё пригодится" - сказали вы и угодили в капкан.\n',
        'Удача-то какая, никого не встретив в замаскированной яме.\n',
        'Странные руны лежат в виде пентограммы. А что если встать в центр?\n',
        'Главное не смотреть себе под ноги. То чего не видишь, того не существует.\n',
        'А что будет если дёрнуть эту верёвку?\n']
czero = ['Если засунуть руку под камень, то можно найти ',
         'Усевшись под дерево, почувствовали под собой что-то напоминающее ',
         'Возле озера лежала чья-то сумка, из которой торчит что-то похожее на ',
         'Сегодня удачный день, вы нашли ',
         'Конечно же вы ожидали найти что-то получше чем ',
         'А кто не будет рад споткнуться об ',
         'Хорошо когда кто-то оставил ',
         'Разве так бывает? На дороге лежит ']
czero_ = ['кусок хлеба.\n',
          'меч.\n',
          'яблоко.\n',
          'волшебную палку.\n',
          'старый шлем.\n',
          'магическое кольцо.\n',
          'колбасу.\n',
          'странную накидкую.\n']

class rndspisok:
    def __init__(self, spisok):
        self.spisok = spisok
        self.spisokrnd = []

    def rnd(self):
        if len(self.spisok) > 0:
            f = random.choice(self.spisok)
            self.spisok.remove(f)
            self.spisokrnd.append(f)
        if len(self.spisok) == 0:
            self.spisok = self.spisokrnd
            self.spisokrnd = []
        return f

gnoms = rndspisok(codin)
orks = rndspisok(cdva)
goblins = rndspisok(ctri)
trolls = rndspisok(cchet)
ogrs = rndspisok(cpat)
spiders = rndspisok(csix)
crabs = rndspisok(csevn)
koldun = rndspisok(cvos)
trap = rndspisok(cdev)
itemstuf = rndspisok(czero)
freereplics = rndspisok(free_replics)

def maping(a, k, l):
    txtleft.delete(0.0, END)
    cellaction(a, k, l)
    if a[k][l] == "*":
        txtright.insert(END, 'Ты пересекаешь границу!!!\n')
        k = 1
        l = 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            f = a[i][j]
            if k == i and l == j:
                a[i][j] = "M"
                start_position.ii = [i, j]
            txtleft.insert(END, a[i][j])

            a[i][j] = f
        txtleft.insert(END, '')
    return start_position.ii

class start_position:
    ii = [1, 1]# [строка, столбец]

def offbutton():
    bw['state'] = 'disabled'
    ba['state'] = 'disabled'
    bs['state'] = 'disabled'
    bd['state'] = 'disabled'
    bhit['state']='normal'
    brun['state']='normal'
    
def printaction(nadpis):  
    txtright.insert(END, datetime.strftime(datetime.now(), "%H:%M:%S") + ':  ')
    txtright.insert(END, nadpis)
    txtright.see(END)

def printstat(hp,ap,gold,xp,lvl):
    txtmenu.delete(0.0,END)
    txtmenu.insert(END,'HP - '+ str(hp)+' AP - '+str(ap)+' GOLD - '+str(gold)+' XP- '+str(xp)+' LVL'+str(lvl))
    txtmenu.see(END)

def cellaction(a, k, l):
    if a[k][l] == "$":
        offbutton()
        printaction(gnoms.rnd())
        if glav.gold - 10>=0:
            returnus(a[start_position.ii[0]][start_position.ii[1]]).gold +=10
            glav.gold -=10
        else:
            glav.hp -= 5
            printaction('За то что у тебя нет золота, гном будет бить тебя!')
    if a[k][l] == "&":
        offbutton()
        printaction(orks.rnd())
    if a[k][l] == "!":
        offbutton()
        printaction(goblins.rnd())
    if a[k][l] == "X":
        offbutton()
        printaction(trolls.rnd())
    if a[k][l] == "^":
        offbutton()
        printaction(ogrs.rnd())
    if a[k][l] == "#":
        offbutton()
        printaction(spiders.rnd())
    if a[k][l] == "%":
        offbutton()
        printaction(crabs.rnd())
    if a[k][l] == "W":
        offbutton()
        printaction(koldun.rnd())
    if a[k][l] == "T":
        offbutton()
        printaction(trap.rnd())
    if a[k][l] == "@":
        offbutton()
        printaction(itemstuf.rnd())
        txtright.insert(END, random.choice(czero_))
        txtright.see(END)
    if a[k][l] == " ":
        bw['state'] = 'normal'
        ba['state'] = 'normal'
        bs['state'] = 'normal'
        bd['state'] = 'normal'
        txtright.see(END)

west = ['Вы направляетесь на запад.\n',
        'Вы держите путь на запад.\n',
        'Вы решили пойти на запад.\n']
east = ['Вы направляетесь на восток.\n',
        'Вы держите путь на восток.\n',
        'Вы решили пойти на восток.\n']
north = ['Вы направляетесь на север.\n',
         'Вы держите путь на север.\n',
         'Вы решили пойти на север.\n']
south = ['Вы направляетесь на юг.\n',
         'Вы держите путь на юг.\n',
         'Вы решили пойти на юг.\n']

we = rndspisok(west)
ea = rndspisok(east)
no = rndspisok(north)
so = rndspisok(south)

def rets():
    k = maping(a, start_position.ii[0] + 1, start_position.ii[1])
    if a[start_position.ii[0]][start_position.ii[1]] == " ":
        printaction(so.rnd())
def retd():
    k = maping(a, start_position.ii[0], start_position.ii[1] + 1)
    if a[start_position.ii[0]][start_position.ii[1]] == " ":
        printaction(ea.rnd())
def reta():
    k = maping(a, start_position.ii[0], start_position.ii[1] - 1)
    if a[start_position.ii[0]][start_position.ii[1]] == " ":
        printaction(we.rnd())
def retw():
    k = maping(a, start_position.ii[0] - 1, start_position.ii[1])
    if a[start_position.ii[0]][start_position.ii[1]] == " ":
        printaction(no.rnd())
        
def returnus(name):
    if name == '!':
        return goblin
    if name == '$':
        return gnom
    if name == '@':
        return rndditme
    if name == '%':
        return crabik
    if name == 'W':
        return wizard
    if name == 'T':
        return traps
    if name == '#':
        return spider
    if name == '^':
        return owgr
    if name == '&':
        return ork
    if name == ' ':
        printaction(freereplics.rnd())
        return probel
    if name == 'X':
        return troll
'''
1 гномы $
2 орки &
3 гоблины !
4 тролли X
5 огр ^
6 паук #
7 земной краб %
8 колдун W
9 ловушка T
0 случайный предмет @
'''
bw = Button(frame, text="North", background="#666", foreground="#ccc",
            padx="2", pady="1", font="11", state = 'normal',command = retw)
ba = Button(frame, text="West", background="#666", foreground="#ccc",
            padx="2", pady="1", font="11", state = 'normal',command = reta)
bs = Button(frame, text="South", background="#666", foreground="#ccc",
            padx="2", pady="1", font="11", state = 'normal',command = rets)
bd = Button(frame, text="East", background="#666", foreground="#ccc",
            padx="2", pady="1", font="11", state = 'normal',command = retd)
deathspeech = ['Кажись %s сдох.\n',
               'Поганный %s погиб.\n','Ещё бы чуть-чуть и %s навалял бы тебе.\n',
               'Не умеет %s драться\n','Теперь %s больше никого не потревожит.\n']

deatch = rndspisok(deathspeech)

udarspisok=['Герой ударяет %sа с силой равной %d.\n','Сначала %s получает по башке от героя %d.\n','Даже %s не ожидал получить удар = %d, .\n']

udar = rndspisok(udarspisok)

udarwraga = ['Но %s решает ударить с силой %d.\n','Промахнувшись,%s задевает героя ударом %d.\n','А вот %s не собирался бить так сильно и нанёс удар равный в %d.\n']

udarw = rndspisok(udarwraga)
def b_hit():
    one = returnus(a[start_position.ii[0]][start_position.ii[1]])
    
    udar_hero=random.randint(round(glav.ap-2),round(glav.ap+2))    
    udar_enemy=random.randint(round(one.ap-2),round(one.ap+2))
    if one.hp>0:
            
        one.hp -= udar_hero
        glav.hp -= udar_enemy
        
        p = (str(udar.rnd())%(str(one.subname),udar_hero))
        g = (str(udarw.rnd())%(str(one.subname),udar_enemy))
        
        printaction(p)
        printaction(g)
        printstat(glav.hp,glav.ap,glav.gold,glav.xp,glav.lvl)
        
    if one.hp <= 0:
        a[start_position.ii[0]][start_position.ii[1]] = ' '
        bw['state'] = 'normal'
        ba['state'] = 'normal'
        bs['state'] = 'normal'
        bd['state'] = 'normal'
        bhit['state'] = 'disabled'
        brun['state']='disabled'
        one.hp = one.maxhp
        glav.gold +=one.gold
        glav.xp +=one.xp
        glav.lvlxp()
        printstat(glav.hp,glav.ap,glav.gold,glav.xp,glav.lvl)
        
        one = (str(deatch.rnd())% str(one.subname))
        printaction(one)

    if glav.hp <=0:
        bw['state'] = 'disabled'
        ba['state'] = 'disabled'
        bs['state'] = 'disabled'
        bd['state'] = 'disabled'
        bhit['state'] = 'disabled'
        brun['state']='disabled'
        bheal['state'] = 'disabled'
        txtright.insert(END,'GAME OUWER')      

def b_heal():
    returnus(a[start_position.ii[0]][start_position.ii[1]]).ap += 1
    if glav.hp <= glav.maxhp:
        glav.hp += 5
        if glav.hp>glav.maxhp:
            glav.hp = glav.maxhp
    else:
        glav.hp = glav.maxhp
    printstat(glav.hp,glav.ap,glav.gold,glav.xp,glav.lvl)

def b_run():
    copyclone = returnus(a[start_position.ii[0]][start_position.ii[1]])
    returnus(a[start_position.ii[0]][start_position.ii[1]]).hp += 3
    glav.hp -= 2
    printstat(glav.hp,glav.ap,glav.gold,glav.xp,glav.lvl)
    bw['state'] = 'normal'
    ba['state'] = 'normal'
    bs['state'] = 'normal'
    bd['state'] = 'normal'
    brun['state']='disabled'
    

bhit = Button(framed, text="Hit", background="#666", foreground="#ccc",
              padx="2", pady="1", font="11",command = b_hit)
bheal = Button(framed, text="Heal", background="#666", foreground="#ccc",
               padx="2", pady="1", font="11",command = b_heal)
brun = Button(framed, text="Run", background="#666", foreground="#ccc",
              padx="2", pady="1", font="11",command = b_run)

txtleft.grid(row=0, column=1)
txtright.grid(row=0, column=2)
txtmenu.grid(row = 0,column  =3)
frame.grid(row=1, column=1)
framed.grid(row=1, column=2)

bw.grid(row=1, column=2)
ba.grid(row=2, column=1)
bs.grid(row=3, column=2)
bd.grid(row=2, column=3)
bhit.grid(row=1, column=1)
bheal.grid(row=1, column=2)
brun.grid(row=1, column=3)

txtright.insert(END, 'Приключение началось\n')
txtright.insert(END, 'Ноги уже болят\n')

mainloop()
