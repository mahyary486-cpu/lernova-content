import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(R)
idx=json.load(open('index.json',encoding='utf-8'))
ok=True
def say(good,msg):
    global ok
    print(('✅ ' if good else '❌ ')+msg)
    ok=ok and good
chap={}
for e in idx['grades']:
    for c in e.get('chapters',[]): chap[c['id']]=(e,c)
# every file belongs to a chapter in index
orphan=[f[:-5] for f in os.listdir('summaries') if f.endswith('.json') and f[:-5] not in chap]
say(not orphan,'همه‌ی فصل‌های دارای فایل در index.json ثبت‌اند'+('' if not orphan else ' | گمشده: '+', '.join(orphan)))
# summaries / details / banks per chapter
badb=[];nosum=[];nodet=[]
for cid,(e,c) in chap.items():
    sp='summaries/%s.json'%cid
    if os.path.exists(sp):
        s=json.load(open(sp,encoding='utf-8'))
        if sorted(s)!=sorted(l['title'] for l in c['lessons']): nosum.append(cid)
        for l in c['lessons']:
            if not os.path.exists('details/%s.md'%l['id']): nodet.append(l['id'])
    bp='banks/%s.txt'%cid
    if os.path.exists(bp):
        L=[x for x in open(bp,encoding='utf-8').read().split('\n') if x.strip()]
        good=len(L)==51 and L[0].startswith('#') and len(L[0])==51 and all(len(x.split('|'))==7 and x.split('|')[5] in ('0','1','2','3') for x in L[1:])
        if not good: badb.append(cid)
say(not nosum,'عنوان درس‌ها در خلاصه‌ها با index یکی است'+('' if not nosum else ' | مشکل: '+', '.join(nosum)))
say(not nodet,'همه‌ی متن‌های تشریحی موجودند'+('' if not nodet else ' | گمشده: '+', '.join(nodet[:8])))
say(not badb,'همه‌ی بانک‌های آزمون ساختار درست دارند'+('' if not badb else ' | خراب: '+', '.join(badb)))
nb=len([f for f in os.listdir('banks')])
print('ℹ️ فصل‌ها: %d | بانک آزمون: %d | درس‌ها: %d'%(len(chap),nb,len(os.listdir('details'))))
for cc in ('US',):
    for g in (9,10,11,12):
        e=[x for x in idx['grades'] if x.get('country','US')==cc and x['grade']==g and x['subject']=='Mathematics']
        if e: print('ℹ️ آمریکا ریاضی پایه %d: %d فصل'%(g,len(e[0]['chapters'])))
print('🟢 همه چیز تایید شد' if ok else '🔴 مشکل پیدا شد؛ خروجی را برای کلاد بفرست')
