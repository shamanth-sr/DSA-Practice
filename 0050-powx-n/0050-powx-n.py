class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.Pow(x , -n)
        
        return self.Pow(x, n)
        
    def Pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            return self.Pow(x * x, n // 2)

        else:
            return x * self.myPow(x, n - 1)