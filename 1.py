def filter_numbers(numbers, threshold=0, greater=True):
    p=[]
    for i in numbers:
        if greater:
            if i>threshold:
                p.append(i)
        else:
            if i<threshold:
                p.append(i)
    return p
