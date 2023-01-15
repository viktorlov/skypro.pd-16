class TestApi:

    def test_all_posts_status(self, test_client):
        """ Проверяем, получается ли при запросе всех постов нужный статус-код """
        response = test_client.get('/api/posts/', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_single_post_status(self, test_client):
        """ Проверяем, получается ли при запросе одного поста нужный статус-код """
        response = test_client.get('/api/posts/1/', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса одного поста неверный"
