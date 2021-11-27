import requests


class API:
    """
    Api для популярного приложения по просмотру аниме - anixart.

    """

    def __init__(self, token: str = None):
        self.api_domain = 'https://api.anixart.tv'
        self.api_domain_aniu = 'https://aniu.ru'
        self.token = token
        self.user_id = None

    def auth_firebase(self):
        """
        Возвращает topicName
        PS: не изучено

        :return: JSON
        """
        return requests.post(
            url=self.api_domain + '/auth/firebase',
            params={'token': self.token}
        ).json()

    def auth_resend(self, login: str, email: str, password: str, _hash: str, vkAccessToken: str = None,
                    googleIdToken: str = None):
        """
        Повторная отправка кода на email (верификация email после регистрации)

        :param login:
        :param email:
        :param password:
        :param _hash:
        :param vkAccessToken:
        :param googleIdToken:
        :return:
        """
        p = [('login', login), ('email', email), ('password', password), ('hash', _hash)]
        if vkAccessToken is not None and googleIdToken is None:
            p.append(('vkAccessToken', vkAccessToken))
        elif vkAccessToken is None and googleIdToken is not None:
            p.append(('googleIdToken', googleIdToken))

        return requests.post(
            url=self.api_domain + '/auth/resend',
            params=p
        ).json()

    def auth_restore(self, data):
        """
        Не изучено

        :param data:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/restore',
            params={'data': data}
        ).json()

    def auth_restore_resend(self, data, password: str, _hash: str):
        """
        Не изучено

        :param data:
        :param password:
        :param _hash:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/restore/resend',
            params={'data': data,
                    'password': password,
                    'hash': _hash}
        ).json()

    def auth_restore_verify(self, data, password: str, _hash: str, code):
        """
        Не изучено

        :param data:
        :param password:
        :param _hash:
        :param code:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/restore/verify',
            params={'data': data,
                    'password': password,
                    'hash': _hash,
                    'code': code}
        ).json()

    def auth_signIn(self, login: str, password: str):
        """
        Авторизация. Возможность получить информацию о пользователе и token

        :param login:
        :param password:
        :return:
        """
        resp = requests.post(
            url=self.api_domain + '/auth/signIn',
            params={'login': login,
                    'password': password}
        ).json()
        self.token = resp['profileToken']['token'] if resp['code'] == 0 else None
        self.user_id = resp['profile']['id'] if resp['code'] == 0 else None
        return resp

    def auth_google(self, googleIdToken: str):
        """
        Авторизация через Google

        :param googleIdToken:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/google',
            params={'googleIdToken': googleIdToken}
        ).json()

    def auth_google_2(self, login: str, email: str, googleIdToken: str):
        """
        Авторизация через Google
        Второй метод, значение: не мзвестно.
        Предположительно для регистрации

        :param login
        :param email
        :param googleIdToken:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/google',
            params={'login': login,
                    'email': email,
                    'googleIdToken': googleIdToken}
        ).json()

    def auth_vk(self, vkAccessToken: str):
        """
        Авторизация через ВК

        :param vkAccessToken:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/vk',
            params={'vkAccessToken': vkAccessToken}
        ).json()

    def auth_vk_2(self, login: str, email: str, vkAccessToken: str):
        """
        Авторизация через ВК
        Второй метод, значение: не мзвестно.
        Предположительно для регистрации

        :param login
        :param email
        :param vkAccessToken:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/vk',
            params={'login': login,
                    'email': email,
                    'vkAccessToken': vkAccessToken}
        ).json()

    def auth_signUp(self, login, email, password):
        """
        Регистрация

        :param login:
        :param email:
        :param password:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/auth/signUp',
            params={'login': login,
                    'email': email,
                    'password': password}
        ).json()

    def auth_verify(self, login: str, email: str, password: str, _hash, code, vkAccessToken: str = None,
                    googleIdToken: str = None):
        """
        Метод производит верификацию только что зарегистрировавшихся аккаунтов



        :param login:
        :param email:
        :param password:
        :param _hash: выданный при регистрации
        :param code: код из email
        :param vkAccessToken: необязательное поле
        :param googleIdToken: необязательное поле
        :return:
        """
        p = [('login', login), ('email', email), ('password', password), ('hash', _hash), ('code', code)]
        if vkAccessToken is not None and googleIdToken is None:
            p.append(('vkAccessToken', vkAccessToken))
        elif vkAccessToken is None and googleIdToken is not None:
            p.append(('googleIdToken', googleIdToken))

        return requests.post(
            url=self.api_domain + '/auth/verify',
            params=p
        ).json()

    def get_page_url(self, kodik_token, player_link):
        """
        Возвращает страницу с встроенным плеером Kodik,
        если нет своего сайта.

        :param kodik_token: токен, который можно получить в https://bd.kodik.biz/api/info/search
        :param player_link: ссылка на плеер из метода episode
        :return: JSON
        """
        return requests.post(
            url='https://bd.kodik.biz/api/info/search',
            params={'token': kodik_token, 'player_link': player_link, 'with_page_links': 'true'}
        ).json()

    def search_collections(self, page: int, database):
        """
        Метод осуществляет поиск среди коллекций
        Не работает, нуждается в дополнительных параметрах.

        :param page: номер страницы
        :return: JSON
        """
        return requests.post(
            url=self.api_domain + '/search/collections/' + str(page),
            params={'token': self.token}
        ).json()

    def search_favoriteCollections(self, page, database):
        """
        Метод осуществляет поиск среди любимых коллекций
        Не работает, нуждается в дополнительных параметрах.

        :param page:
        :param database:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/search/favoriteCollections/' + str(page),
            params={'token': self.token}
        ).json()

    def search_favorites(self, page, database):
        """
        Метод осуществляет поиск среди любимых anime
        Не работает, нуждается в дополнительных параметрах.

        :param page:
        :param database:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/search/favorites/' + str(page),
            params={'token': self.token}
        ).json()

    def search_history(self, page, database):
        """
        Метод осуществляет поиск среди истории просмотра
        Не работает, нуждается в дополнительных параметрах.

        :param page:
        :param database:
        :return:
        """
        return requests.post(
            url=self.api_domain + '/search/history/' + str(page),
            params={'token': self.token}
        ).json()

    def search_profileCollections(self, p_id, page, release_id, database):
        """
        Метод осуществляет поиск среди коллекций профиля юзера
        Не работает, нуждается в доп данных

        :param p_id:
        :param page:
        :param release_id:
        :param database
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/search/profileCollections/{p_id}/{page}',
            params={'token': self.token}
        ).json()

    def search_profile_list(self, status, page):
        """
        Не изучено


        :param status:
        :param page:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/search/profile/list/{status}/{page}',
            params={'token': self.token}
        ).json()

    def search_profiles(self, page):
        """
        Не изучено

        :param page:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/search/profiles/{page}',
            params={'token': self.token}
        ).json()

    def search_releases(self, page):
        """
        Не изучено

        :param page:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/search/releases/{page}',
            params={'token': self.token}
        ).json()

    def search_release_aniu(self, query: str) -> list:
        """
        Метод осуществляет поиск аниме,
        используя aniu api.

        :param query:
        :return: list(json)
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/release.search',
            params={'query': query}
        ).json()

    def get_genre(self):
        """
        Метод возвращает информациб о жанрах
        и их список

        :return:
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/genre.list'
        ).json()

    def genre_list_anime(self, genre_name):
        """
        Метод возвращает список аниме по жанрам.

        :param genre_name: get_genre()->title_ru - название жанра на русском
        :return:
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/genre',
            params={'name': genre_name}
        ).json()

    def new_release(self):
        """
        Метод возвращает новые релизы

        :return:
        """
        return requests.get(url=f'{self.api_domain_aniu}/api/release.list.new').json()

    def now_release(self):
        """
        Метод возвращает релизы из категории <<смотрят сейчас>>

        :return:
        """
        return requests.get(url=f'{self.api_domain_aniu}/api/release.list.now').json()

    def popular_release(self):
        """
        Метод возвращает популярные релизы аниме

        :return:
        """
        return requests.get(url=f'{self.api_domain_aniu}/api/release.list.popular').json()

    def raiting_release(self, releaseId):
        """
        Метод возвращает рейтинг аниме

        :return:
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/release.raiting',
            params={'id': releaseId}
        ).json()

    def release_links(self, releaseId):
        """
        Метод возвращает хронологию и связи аниме

        :return:
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/release.links',
            params={'id': releaseId}
        ).json()

    def released(self, relatedId, page: int = 0):
        """
        Метод возвращает выпущенные anime по relatedId.
        По умолчанию page = 0

        :param relatedId:
        :param page:
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/related/{relatedId}/{page}',
            params={'token': self.token}
        ).json()

    def release(self, r_id, pirate_mode: bool = False):
        """
        Метод возвращает релизы anime по r_id.
        Не изучено полностью

        Может использоваться без авторизации! (без токена)

        :param r_id:
        :param pirate_mode: неизвестное булевое значение
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/release/{r_id}',
            params={'pirate_mode': pirate_mode,
                    'token': self.token}
        ).json()

    def release_random(self, pirate_mode: bool = False):
        """
        Метод возвращает рандомные релизы аниме.

        Может использоваться без авторизации! (без токена)

        :param pirate_mode:
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/release/random',
            params={'pirate_mode': pirate_mode,
                    'token': self.token}
        ).json()

    def release_report(self, r_id):
        """
        Не изучено



        :param r_id:
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/release/report/{r_id}',
            params={'token': self.token}
        ).json()

    def release_vote_add(self, r_id, vote):
        """
        Метод добавляет оценку к релизу

        :param r_id:
        :param vote: от 1 до 5 (вроде)
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/release/vote/add/{r_id}/{vote}',
            params={'token': self.token}
        ).json()

    def release_vote_delete(self, r_id):
        """
        Метод удаляет голос (я хз что он делает)
        Не изучено

        :param r_id:
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/release/vote/delete/{r_id}',
            params={'token': self.token}
        ).json()

    def poster_to_jpg(self, poster_hash):
        """
        Преобразует полученные poster hash в jpg

        :param poster_hash:
        :return:
        """
        return f'https://static.anixart.tv/posters/{poster_hash}.jpg'

    def schedule(self):
        """
        Метод возвращает календарь выхода серий на неделю

        :return:
        """
        return requests.get(self.api_domain + '/schedule').json()

    def episode_target(self, releaseId, sourceId, position):
        """
        Метод возвращает серию эпизода

        Может использоваться без авторизации! (без токена)

        :param releaseId:
        :param sourceId: номер источника
        :param position: номер серии
        :return: JSON
        """
        return requests.get(
            url=self.api_domain + f'/episode/target/{releaseId}/{sourceId}/{position}',
            params={'token': self.token}
        ).json()

    def episode_aniu(self, releaseId):
        """
        Метод аналогичный episode(), однако более удобный, ибо возвращает
        полную информацию о аниме, всключая ссылку на видео.

        :param releaseId:
        :return:
        """
        return requests.get(
            url=f'{self.api_domain_aniu}/api/release',
            params={'id': releaseId}
        ).json()

    def episode(self, releaseId, typeId=None, sourceId=None, sort=0):
        """
        Метод возвращает описание релиза аниме по releaseID, доступные озвучки и серии(url) к озвучкам.

        :param releaseId:
        :param typeId: необязательный параметр, который указывает на (вроде тип озвучки)
        :param sourceId: необязательный параметр, который указывает на номер серии
        :param sort:
        :return:
        """
        req = f'/episode/{releaseId}/{typeId if typeId is not None else ""}/{sourceId if sourceId is not None else ""}'
        return requests.get(
            url=self.api_domain + req,
            params={'sort': sort, 'token': self.token}
        ).json()

    def episode_report(self, releaseId, sourceId, position):
        """
        Метод не изучен


        :param releaseId:
        :param sourceId: номер источника(озвучки)
        :param position: номер серии
        :return: JSON
        """
        return requests.get(
            url=self.api_domain + f'/episode/report/{releaseId}/{sourceId}/{position}',
            params={'token': self.token}
        ).json()

    def episode_watch(self, releaseId, sourceId, position=None):
        """
        Метод помечает серию как просмотренную


        :param releaseId:
        :param sourceId:
        :param position:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/episode/watch/{releaseId}/{sourceId}/{position if position is not None else ""}',
            params={'token': self.token}
        ).json()

    def episode_unwatch(self, releaseId, sourceId, position=None):
        """
        Метод убирает просмотр определенной серии

        :param releaseId:
        :param sourceId:
        :param position: необязательный параметр обозначающий номер серии
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/episode/unwatch/{releaseId}/{sourceId}/{position if position is not None else ""}',
            params={'token': self.token}
        ).json()

    def episode_updates(self, releaseId, page):
        """
        Метод (Не проверено)

        :param releaseId:
        :param page:
        :return:
        """
        return requests.get(
            url=self.api_domain + f'/episode/updates/{releaseId}/{page}',
            params={'token': self.token}
        ).json()

    def discover_comments(self):
        """
        Метод возвращает популярные комментарии к релизам,
        не требует авторизации (token)

        :return:
        """
        return requests.post(
            url=self.api_domain + f'/discover/comments'
        ).json()

    def discover_discussing(self):
        """
        Обсуждаемые релизы
        (не требует токена)

        :return:
        """
        return requests.post(
            url=self.api_domain + f'/discover/discussing'
        ).json()

    def discover_interesting(self):
        """
        Интересное
        (не требует токена)

        :return:
        """
        return requests.post(
            url=self.api_domain + f'/discover/interesting'
        ).json()

    def discover_recommendations(self, page, previous_page):
        """
        Метод возвращает рекомендации для пользователя,
        на основе недавно просмотренного.


        :param page:
        :param previous_page:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/discover/recommendations/{page}',
            params={'previous_page': previous_page, 'token': self.token}
        ).json()

    def discover_watching(self, page):
        """
        Метод возвращает часто просматриваемое (точно не разобрался)

        Метод не требует авторизации! ! ! (без токена)

        :param page:
        :return:
        """
        return requests.post(
            url=self.api_domain + f'/discover/watching/{page}',
            params={'token': self.token}
        ).json()

    def add_friend(self, user_id):
        """
        Метод отправляет запрос в друзья по
        user_id
        
        :param user_id: обязательный параметр, обозначающий субьект, которому отправляется заявка
        :return: JSON

        code: 3 - успешный результат
        code: 1 - безуспешный результат или заявка уже отправлена
        code: 8 - хз
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/request/send/' + str(user_id),
            params={'token': self.token}
        ).json()

    def remove_friend(self, user_id):
        """
        Метод отправляет запрос в друзья по
        user_id

        :param user_id: обязательный параметр, обозначающий субьект, которому отправляется заявка
        :return: JSON

        code: 3 - успешный результат
        code: 1 - безуспешный результат или заявка уже отправлена
        code: 8 - хз
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/request/remove/' + str(user_id),
            params={'token': self.token}
        ).json()

    def get_friend_recommendations(self):
        """
        Метод возвращает рекомнгдуемых друзей

        :return: JSON
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/recommendations',
            params={'token': self.token}
        ).json()

    def hide_friend_request(self, user_id):
        """
        Метод скрывает отправленные вам заявки в друзья
        (альтернатива кнопки "добавить" - "скрыть")

        :param user_id: id пользователя, которого нужно скрыть
        :return: JSON

        code: 1 - неуспешно
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/request/hide/' + str(user_id),
            params={'token': self.token}
        ).json()

    def get_friends_requests_in_page(self, page, last: bool = False):
        """
        Метод выдает список отправленных вам заявок в друзья
        по страницам или последнюю

        :param page: номер страницы с заявками
        :param last: если True, тогда выводит последнюю заявку без надобности парам param page
        :return: JSON
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/requests/in/' + str('list' if last else page),
            params={'token': self.token}
        ).json()

    def get_friends_requests_out_page(self, page: int, last: bool = False):
        """
        Метод выдает список отправленных вами заявок в друзья
        по страницам или последнюю

        :param page: номер страницы с заявками
        :param last: если True, тогда выводит последнюю заявку без надобности парам param page
        :return: JSON
        """
        return requests.get(
            url=self.api_domain + '/profile/friend/requests/out/' + str('list' if last else page),
            params={'token': self.token}
        ).json()

    def get_socials_from_profile(self, user_id):
        """
        Метод выдает информацию о
        добавленных соц сетях пользователя

        :param user_id:
        :return:
        """

        return requests.get(
            url=self.api_domain + f'/profile/social/{user_id}',
            params={'token': self.token}
        ).json()

    def get_profile(self, user_id):
        """
        Метод выдает информацию о
        профиле

        :param user_id:
        :return:
        """

        return requests.get(
            url=self.api_domain + f'/profile/{user_id}'
        ).json()

    def get_my_profile(self):
        """
        Метод выдает информацию о
        вашем профиле

        :return:
        """

        return requests.get(
            url=self.api_domain + f'/profile/{self.user_id}'
        ).json()
