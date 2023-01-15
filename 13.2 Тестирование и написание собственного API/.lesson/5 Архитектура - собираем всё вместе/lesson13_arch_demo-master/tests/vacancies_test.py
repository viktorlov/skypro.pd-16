class TestVacancies:

    def test_all_status(self, test_client):
        """ Проверяем, получается ли при запросе вакансий нужный статус-код """
        response = test_client.get('/vacancies', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех вакансий неверный"

    def test_single_status(self, test_client):
        """ Проверяем, получается ли при запросе одной вакансии нужный статус-код """
        response = test_client.get('/vacancies/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса одной вакансии неверный"
