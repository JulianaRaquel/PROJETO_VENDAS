import pytest
from model_bakery import baker
from django.urls import reverse

from produtos.models import Produto


@pytest.fixture
def playstation(db):
    return baker.make(Produto, nome='Playstation', preco=3999)


def test_adicionar_carrinho_vazio(client, playstation):
    response = client.post(
        reverse('add_carrinho'), data={'id': playstation.id, 'quantidade': 1}
    )

    assert response.status_code == 302
    assert response['Location'] == reverse('ver_carrinho')
    assert client.session['carrinho'] == [{
        'id_produto': playstation.id,
        'preco': playstation.preco,
        'quantidade': 1,
        'subtotal': playstation.preco,
    }]


def test_adicionar_com_produto_no_carrinho(client, playstation):
    item = {
        'id_produto': playstation.id,
        'preco': playstation.preco,
        'quantidade': 1,
        'subtotal': playstation.preco,
    }
    session = client.session
    session['carrinho'] = [item]
    session.save()

    response = client.post(
        reverse('add_carrinho'), data={'id': playstation.id, 'quantidade': 1}
    )
    assert response.status_code == 302
    assert response['Location'] == reverse('ver_carrinho')
    assert client.session['carrinho'][0]['quantidade'] == 2
    assert client.session['carrinho'][0]['subtotal'] == 2 * playstation.preco


def test_remover_carrinho(client, playstation):
    item = {
        'id_produto': playstation.id,
        'preco': playstation.preco,
        'quantidade': 1,
        'subtotal': playstation.preco,
    }
    session = client.session
    session['carrinho'] = [item]
    session.save()

    response = client.get(reverse('remover_carrinho', args=[playstation.id]))
    assert response.status_code == 302
    assert response['Location'] == reverse('ver_carrinho')
    assert client.session['carrinho'] == []
