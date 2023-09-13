def load(filename):
    """
    Due to the author's network problems, a third-party package
    called `dotenv` could not be installed, so I built my own wheel instead.
    :param filename:
    :return: dict
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
