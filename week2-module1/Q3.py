def text_preprocessing(text):
        text = text.lower()
        text = text.replace(',', '')
        text = text.replace('.', '')
        word = text.split()
        return word

def exercise3(document):
    words = text_preprocessing(document)
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    print(result)


if __name__ == "__main__":
    document = "Ngày xửa ngày xưa, có hai chị em cùng cha khác mẹ tên là Tấm và Cám."
    exercise3(document)