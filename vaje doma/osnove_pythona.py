# predzadnjih sto števk števila 2 na 12345

zadnjih_200 = 2 ** 12345 % 10 ** 200
pred_100 = zadnjih_200 // 10 ** 100
print(pred_100)