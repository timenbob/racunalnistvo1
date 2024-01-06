def kovanci_k(kovanci, k=1):
    slovar = {}
    n = len(kovanci)
    def pomoc(i):
        if i >= n:
            return 0
        if i not in slovar:
            slovar[i] = max(kovanci[i] + pomoc(i+k+1), pomoc(i+1))
        return slovar[i]
    return pomoc(0)

print(kovanci_k([10,20,5,10,20,10], k=2))