import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_home_template_and_content(client):
    url = reverse('colaborador_list')
    response = client.get(url)
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'gestao/colaborador_list.html')
    
    content = response.content.decode('utf-8')
    
    # Verificação robusta: checa se as palavras chave estão lá
    # independente de espaços, links ou quebras de linha
    assert "Gestão" in content
    assert "EPIs" in content
    assert "Colaboradores" in content
    assert "fa-helmet-safety" in content

def test_home_url():
    assert reverse('home') == '/'
