money = float(input('Сумма вклада под процент на год: '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [proc * (money / 100) for proc in per_cent.values()]

print('Сумма процентов за год с вашей суммы в этих банках: ' + str(sorted(deposit)))
print('Максимальная сумма, которую вы можете заработать: ' + str(max(deposit)))