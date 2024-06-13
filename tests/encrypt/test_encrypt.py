import pytest
from challenges.challenge_encrypt_message import encrypt_message

frase_teste = "abcdef"
frase_teste_2 = "dcba"
chave_impar = 3
chave_par = 4
chave_negativa = -1
chave_fora_do_range = 10
chave_incorreta = "a"


def test_encrypt_message():
    assert encrypt_message(frase_teste, chave_par) == "fe_dcba"
    assert encrypt_message(frase_teste, chave_impar) == "cba_fed"

    assert encrypt_message(frase_teste, chave_negativa) == "fedcba"

    with pytest.raises(TypeError):
        encrypt_message(frase_teste, chave_incorreta)

    assert encrypt_message(frase_teste_2, 2) == "ab_cd"
