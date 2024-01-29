import asyncio
import time

class Awa:
    def returnAsync(self):
        return self.waiting

    async def waiting(self, *a):
        try:
            print("finished!!")
            await asyncio.sleep(2)
        except Exception as e:
            print(e)
            pass

    async def task(self):
        tasks = list(map(self.returnAsync(), range(3)))

        # tasks = [self.waiting(), self.waiting(), self.waiting()]
        # tasks = (*[self.waiting(), self.waiting(), self.waiting()])
        await asyncio.gather(
            *tasks
            # self.waiting(), self.waiting(), self.waiting()
            )

    async def retA2(self, st, x):
        print(st, x)

    async def t2(self):
        r = lambda x: self.retA2(x, 0.1)
        tasks = list(map(r, range(3)))
        await asyncio.gather(*tasks)

"""
def pp(i, x):
    return (i*i , x*x)
print(pp(4,3))

qq = lambda x, y=5:pp(x,y)
print(qq(10))
mm = map(qq, range(3))
print(list(mm))
"""
a = Awa()
# a.waiting()
s = time.time()
# asyncio.run(a.task())
asyncio.run(a.t2())
print(time.time() - s)

"""
def write_mail(number):
    print(f"書き込み({number}番目)：こんにちは")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：げんきですか？")
    time.sleep(0.03)
    print(f"書き込み({number}番目)：さようなら")
    time.sleep(0.03)

# 非同期処理を行う関数は、async と付けなければならない
async def send_mail(number):
    print(f"送付({number}番目)")
    await asyncio.sleep(5)

def check_response(number):
    hoge=0
    # 無駄な計算
    for i in range(1, 100000000):
        hoge += i/3 + i/5 + i/7 + i/9 + i/11
    print(f"確認OK({number}番目)")

async def task():
    # 書類書き込み（同期処理）
    write_mail(1)
    write_mail(2)
    write_mail(3)
    # メール送付＆待ち(非同期処理) <- ここだけ非同期処理
    await asyncio.gather( # 処理が全部終わるまで待つ
        send_mail(1),
        send_mail(2),
        send_mail(3)
    )
    # 書類チェック（同期処理）
    # check_response(1)
    # check_response(2)
    # check_response(3)


if __name__ == '__main__':
    start_time=time.time()
    asyncio.run(task())
    print(f"かかった時間：{time.time()-start_time}s")
"""
