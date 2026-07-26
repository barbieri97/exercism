def transform(legacy_data: dict):
    data = dict()
    for item in legacy_data:
        for i in legacy_data[item]:
            i=i.lower()
            data[i]=item

    return data