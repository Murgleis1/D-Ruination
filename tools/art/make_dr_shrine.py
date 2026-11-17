import sys
from PIL import Image
PAL = {'.':(115,197,165),'K':(41,33,41),'R':(132,52,44),'r':(156,90,66),'B':(90,60,41),'n':(165,115,74),
       'd':(90,90,107),'m':(140,140,156),'l':(189,189,206),'w':(247,239,214),'y':(255,231,99),'o':(239,140,49),
       'p':(231,107,148),'g':(66,140,74),'G':(222,181,66)}
ORDER = '.KRrBndmlwyopgG'
rows = [
".......KK.......",
"......KrrK......",
".....KrrRRK.....",
"....KrrRRRRK....",
"...KrrRRRRRRK...",
"..KrrRRRRRRRRK..",
"..KKKKKKKKKKKK..",
"...KnnnnnnnnK...",
"...KnKKKKKKBK...",
"...KnKKKKKKBK...",
"...KnKKyyKKBK...",
"...KnKKooKKBK...",
"...KnKKwwKKBK...",
"...KnBBBBBBBK...",
"...KKKKKKKKKK...",
"......KnBK......",
"......KnBK......",
"......KnBK......",
"..y...KnBK...y..",
"..o...KnBK...o..",
"..w.y.KnBK.y.w..",
"..w.o.KnBK.o.w..",
"..wpwgKnBKgwpw..",
".KllllllllllllK.",
".KmmmmmmmmmmmdK.",
".KddddddddddddK.",
".KKKKKKKKKKKKKK.",
]
rows = ["."*16]*(31-len(rows)) + rows + ["."*16]
assert len(rows)==32 and all(len(r)==16 for r in rows), [len(r) for r in rows]
im = Image.new('P',(16,32)); pal=[]
for ch in ORDER: pal+=list(PAL[ch])
im.putpalette(pal+[0,0,0]*(256-len(ORDER)))
for y,r in enumerate(rows):
    for x,ch in enumerate(r): im.putpixel((x,y),ORDER.index(ch))
im.save(sys.argv[1])
