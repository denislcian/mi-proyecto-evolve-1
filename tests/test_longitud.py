from mi_conversor import metros_a_kilometros, pulgadas_a_centimetros

def test_metros_a_kilometros():
    assert metros_a_kilometros(1000) == 1

def test_pulgadas_a_centimetros():
    assert pulgadas_a_centimetros(1) == 2.54
    