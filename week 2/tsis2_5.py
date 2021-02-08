class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        summ = 0
        if 10000 <= n < 100000:
            n1, n2, n3, n4, n5 = n // 10000, (n % 10000) // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10
            pro, summ = n1 * n2 * n3 * n4 * n5, n1 + n2 + n3 + n4 + n5 
            return pro - summ
        elif 1000 <= n < 10000:
            n1, n2, n3, n4 = n // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10
            pro, summ = n1 * n2 * n3 * n4, n1 + n2 + n3 + n4
            return pro - summ
        elif 100 <= n < 1000:
            n1, n2, n3 = n // 100, (n % 100) // 10, n % 10
            pro, summ = n1 * n2 * n3, n1 + n2 + n3
            return pro - summ
        elif 10 <= n < 100:
            n1, n2 = n // 10, n % 10
            pro, summ = n1 * n2, n1 + n2
            return pro - summ
        else:
            return 0