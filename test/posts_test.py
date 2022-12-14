class TestPosts:

    def test_all_posts_status(self, test_client):
        """ Проверяем при запросе постов нужный статус-код """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код запроса кандидатов не ок"

    def test_single_posts_status(self, test_client):
        """ Проверяем при запросе одного поста нужный статус-код """
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса кандидата не ок"
