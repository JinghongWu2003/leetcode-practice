class Solution(object):
    def intToRoman(self, num):
        table = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
                 (100,'C'), (90,'XC'), (50,'L'), (40,'XL'),
                 (10,'X'),  (9,'IX'),  (5,'V'),  (4,'IV'), (1,'I')]
        res = []
        append = res.append  # 微优化：减少属性查找
        for v, s in table:
            q, num = divmod(num, v)  # 一次得到商和余数
            if q:
                append(s * q)
            if num == 0:             # 提前结束（通常能少走几步）
                break
        return ''.join(res)
