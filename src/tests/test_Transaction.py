def test_Transaction_init(tr_fixture):

    assert tr_fixture.id_ == 11111111
    assert tr_fixture.state == 'EXECUTED'
    assert str(tr_fixture.date) == '2023-07-07 10:00:00.111111'
    assert tr_fixture.currency_name == 'руб.'
    assert tr_fixture.amount == '10000.99'
    assert tr_fixture.currency_name == 'руб.'
    assert tr_fixture.currency_code == 'RUB'
    assert tr_fixture.description == 'Перевод организации'
    assert tr_fixture.from_ == 'Maestro 1234123412341234'
    assert tr_fixture.to_ == 'Счет 12345123451234512345'
