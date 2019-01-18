
def test(k1, k2, k3):
    print(k1, k2, k3)

def main(**kwargs):
    print(kwargs)
    test(**kwargs)

main(k1='v1', k2='v2', k3='v3')
