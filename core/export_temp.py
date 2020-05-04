from stocks.models import Stock


def export_data():
    file = 'temp/NYSE.txt'
    with open(file, 'r') as f:
        for i in f.readlines():
            source = i.split()
            Stock.objects.create(symbol=source[0], information=" ".join(source[1:]))
        return True
