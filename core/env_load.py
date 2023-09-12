def load(filename):
    """
    due to the network problem I cannot install 'dotenv' package successfully,
    so i write it
    :param filename:
    :return:
    """
    d = {}
    with open(filename,'r',encoding='utf8') as f:
        fc = f.read()
        line = fc.split("\n")
        for l in line:
            item = l.split('=')
            if len(item) < 2:
                continue
            d.update({item[0].replace(" ",""):item[1].replace(" ","")})
        f.close()
    return d
