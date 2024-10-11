import pytest
from app import Person, Email

@pytest.fixture
def valid_person():
    emails = [Email("amanda@gmail.com")]
    return Person("Amanda Vieira de Oliveira", 20, emails)

@pytest.fixture
def invalid_person():
    emails = [Email("a@a")]
    return Person("Amanda", 20, emails)

@pytest.fixture
def person_with_single_name():
    emails = [Email("amanda@gmail.com")]
    return Person("Amanda", 20, emails)

@pytest.fixture
def person_with_non_alphabetic_name():
    emails = [Email("amanda@gmail.com")]
    return Person("Amanda 123", 20, emails)

@pytest.fixture
def person_with_out_of_range_age():
    emails = [Email("amanda@gmail.com")]
    return Person("Amanda Vieira de Oliveira", 201, emails)

@pytest.fixture
def person_without_email():
    return Person("Amanda Vieira de Oliveira", 20, [])

@pytest.fixture
def person_with_invalid_emails():
    emails = [Email("amanda@gmail.com"), Email("semArrobaEPontoCom")]
    return Person("Amanda Vieira de Oliveira", 20, emails)


# ------------------------------------------------------------------------


def test_valid_name(valid_person):
    assert valid_person.isValidToInclude() == []

def test_invalid_name(invalid_person):
    assert invalid_person.isValidToInclude() == ["O nome deve ser composto por ao menos 2 partes", "Formato de email inválido! Siga esse padrão: ___@___.__"]

def test_single_name(person_with_single_name):
    assert "O nome deve ser composto por ao menos 2 partes" in person_with_single_name.isValidToInclude()

def test_non_alphabetic_name(person_with_non_alphabetic_name):
    assert "O nome deve ser composto apenas de letras" in person_with_non_alphabetic_name.isValidToInclude()

def test_age_range():
    person = Person("Amanda Vieira de Oliveira", 0, [Email("amanda@gmail.com")])
    assert "A idade deve estar no intervalo entre 1 e 200" in person.isValidToInclude()

def test_out_of_range_age(person_with_out_of_range_age):
    assert "A idade deve estar no intervalo entre 1 e 200" in person_with_out_of_range_age.isValidToInclude()

def test_person_without_email(person_without_email):
    assert "Pessoa deve ter pelo menos um email associado" in person_without_email.isValidToInclude()

def test_invalid_emails(person_with_invalid_emails):
    assert "Formato de email inválido! Siga esse padrão: ___@___.__" in person_with_invalid_emails.isValidToInclude()
