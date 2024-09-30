pars = [0, 0, 0]

def kv(par):
    if pars[0] == 0:
        raise Exception('fuj')
    d = pars[1] ** 2 - 4 * pars[0] * pars[2]
    if d < 0:
        return []
    elif d == 0:
        return [-pars[1] / (2 * pars[0]),]
    else:
        odm = d ** 0.5
        return [(-pars[1] + odm) / (2 * pars[0]), (-pars[1] - odm) / (2 * pars[0])]
    
print(kv(pars))