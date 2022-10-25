raiz = []
raiz_neg = []
for i in range(1, 101):
    calculo = math.sqrt(i)
    calculo_neg = -calculo
    raiz.append(calculo)
    raiz_neg.append(calculo_neg)
print(raiz)
print(raiz_neg)

plt.plot(raiz_neg, raiz)
plt.grid()
plt.show()