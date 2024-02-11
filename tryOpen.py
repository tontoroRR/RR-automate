import yaml
from modules.counter import *
from modules.styles import *
import time

f = open('setting.yml', 'r')
d = yaml.safe_load(f)
f.close()
style = RhandumLeague()
style.import_from(d['style'])

c = Counter(style)
c.focus_app()

_o = c.op
while True:
    if _o.exists('images/spectatorForTop1Btn.png', 0.2):
        _o.exist_click('images/spectatorForTop1Btn.png', 1, (-15, 0))
        for _i in range(20):
            if _o.exists('images/cannotWatchSpectatorFull.png', 0.2):
                break
            time.sleep(0.2)
    _o.exist_click('images/backToPrevRhandumLeagueBtn.png', 0.2)
    time.sleep(0.3)
    _o.exist_click('images/rhandumLeagueCard.png', 0.2)
    time.sleep(0.3)
        

# while True:
#     time.sleep(1)
