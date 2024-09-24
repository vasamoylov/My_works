import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Report:
#принимаем название файла excel соответствующего формата,
#добавляем новые столбцы "Валовая прибыль", "Рентабельность продаж"
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_excel(self.file_name)
        self.data['Валовая прибыль'] = None
        self.data['Рентабельность продаж'] = None

#в новых столбцах проводим соответстующие расчеты
#выводим Общую (валовую) прибыль по всем продажам и среднюю рентабельность
    def profit(self):
        index_sum_purchase = self.data.columns.get_loc('Покупки Сумма с НДС')
        index_sum_selling = self.data.columns.get_loc('Продажи Сумма с НДС')
        index_profit = self.data.columns.get_loc('Валовая прибыль')
        index_profitability = self.data.columns.get_loc('Рентабельность продаж')
        for row in range(0, len(self.data)):
            self.data.iat[row, index_profit] = self.data.iat[row, index_sum_selling] - self.data.iat[
                row, index_sum_purchase]
            self.data.iat[row, index_profitability] = round(
                self.data.iat[row, index_profit] / self.data.iat[row, index_sum_selling] * 100, 2)
        self.data['Рентабельность продаж'] = self.data['Рентабельность продаж'].astype(str) + ' %'
        sum_profit = round(self.data['Валовая прибыль'].sum(), 0)
        sum_selling = round(self.data['Продажи Сумма с НДС'].sum(), 0)
        profitability = '{:.1%}'.format(sum_profit / sum_selling)
        print(f'Валовая прибыль: {sum_profit} руб., Средняя рентабельность: {profitability}')

#сортируем файл по валовой прибыли от max к min
#экспотрируем в новый файл 10 лучших позиций по валовой приыбли с рентабельностью
    def report_file(self):
        data_sorted = self.data.sort_values(by=['Валовая прибыль'], ascending=[False])
        new_file = pd.DataFrame(
            {'Наименование SKU': data_sorted['Наименование SKU'], 'Валовая прибыль': data_sorted['Валовая прибыль'],
             'Рентабельность продаж': data_sorted['Рентабельность продаж']})
        new_file = new_file.head(10)
        new_file.to_excel('Фин.отчет.xlsx', index=False)
        return new_file

#выводим гистограмму по валовой прибыли
    def hist(self):
        sns.histplot(x=self.report_file()['Валовая прибыль'])
        plt.show()


report1 = Report('Свод.xlsx')
report1.profit()
report1.report_file()
report1.hist()