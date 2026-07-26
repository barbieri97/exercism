def transform(legacy_data: dict):
    return {k.lower():v for v in legacy_data for k in legacy_data[v]}