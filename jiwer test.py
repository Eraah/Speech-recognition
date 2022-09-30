import jiwer

with open('ск оригинал.txt', 'r', encoding="utf-8") as data_o, open('ск црт.txt', 'r', encoding="utf-8") as data_x, open('ск яндекс.txt', 'r', encoding="utf-8") as data_y:
    reference = data_o.read()
    hypothesisX = data_x.read()
    hypothesisY = data_y.read()

measuresX = jiwer.compute_measures(reference, hypothesisX)
measuresY = jiwer.compute_measures(reference, hypothesisY)
print('Метрики ЦРТ для сказки: WER - ', round(measuresX['wer'], 3), 'MER - ', round(measuresX['mer'], 3), 'WIL - ', round(measuresX['wil'], 3))
print('Метрики Яндекс для сказки: ЦРТ WER - ', round(measuresY['wer'], 3), 'MER - ', round(measuresY['mer'], 3), 'WIL - ', round(measuresY['wil'], 3))

transformation = jiwer.Compose([
    jiwer.ToLowerCase(),  # все приводится к нижнему регистру
    jiwer.RemovePunctuation(),  # удаляется вся пунктуация
    jiwer.RemoveWhiteSpace(replace_by_space=True),  # удаляются пробелы и переносы строк с заменой на обычные пробелы
    jiwer.RemoveMultipleSpaces(),  # удаляются множественные пробелы
    jiwer.ReduceToListOfListOfWords(word_delimiter=" ")  # строка разделяется на пословный массив строк
])

measuresX= jiwer.compute_measures(reference, hypothesisX, truth_transform=transformation, hypothesis_transform=transformation)
measuresY = jiwer.compute_measures(reference, hypothesisY, truth_transform=transformation, hypothesis_transform=transformation)
print('Метрики ЦРТ c предобработкой для сказки: WER - ', round(measuresX['wer'], 3), 'MER - ', round(measuresX['mer'], 3), 'WIL - ', round(measuresX['wil'], 3))
print('Метрики Яндекс c предобработкой для сказки: ЦРТ WER - ', round(measuresY['wer'], 3), 'MER - ', round(measuresY['mer'], 3), 'WIL - ', round(measuresY['wil'], 3))

with open('зддр оригинал.txt', 'r', encoding="utf-8") as data_o, open('зддр црт.txt', 'r', encoding="utf-8") as data_x, open('зддр яндекс.txt', 'r', encoding="utf-8") as data_y:
    reference = data_o.read()
    hypothesisX = data_x.read()
    hypothesisY = data_y.read()

measuresX = jiwer.compute_measures(reference, hypothesisX)
measuresY = jiwer.compute_measures(reference, hypothesisY)
print('Метрики ЦРТ для ЗДдР: WER - ', round(measuresX['wer'], 3), 'MER - ', round(measuresX['mer'], 3), 'WIL - ', round(measuresX['wil'], 3))
print('Метрики Яндекс для ЗДдР: ЦРТ WER - ', round(measuresY['wer'], 3), 'MER - ', round(measuresY['mer'], 3), 'WIL - ', round(measuresY['wil'], 3))

transformation = jiwer.Compose([
    jiwer.ToLowerCase(),  # все приводится к нижнему регистру
    jiwer.RemovePunctuation(),  # удаляется вся пунктуация
    jiwer.RemoveWhiteSpace(replace_by_space=True),  # удаляются пробелы и переносы строк с заменой на обычные пробелы
    jiwer.RemoveMultipleSpaces(),  # удаляются множественные пробелы
    jiwer.ReduceToListOfListOfWords(word_delimiter=" ")  # строка разделяется на пословный массив строк
])

measuresX= jiwer.compute_measures(reference, hypothesisX, truth_transform=transformation, hypothesis_transform=transformation)
measuresY = jiwer.compute_measures(reference, hypothesisY, truth_transform=transformation, hypothesis_transform=transformation)
print('Метрики ЦРТ c предобработкой для ЗДдР: WER - ', round(measuresX['wer'], 3), 'MER - ', round(measuresX['mer'], 3), 'WIL - ', round(measuresX['wil'], 3))
print('Метрики Яндекс c предобработкой для ЗДдР: ЦРТ WER - ', round(measuresY['wer'], 3), 'MER - ', round(measuresY['mer'], 3), 'WIL - ', round(measuresY['wil'], 3))