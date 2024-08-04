def car(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info


print(car('Ford', 'Mustang', color='red', year=1964))
