# [run.py](run.py) # <mark>основной запускаемый файл проекта

# Структура приложения:

## [app](app) # директория приложения
- ### [bp_api](app/bp_api) # директория обработчика запросов api
  - [bp_api_views.py](bp_api%2Fbp_api_views.py) # файл обработчик api
- ### [bp_bookmarks](app/bp_bookmarks) # обработчик закладок
- ### [bp_errorhandlers](app/bp_errorhandlers) # обработчик ошибок
  - [bp_errorhandlers_views.py](app%2Fbp_errorhandlers%2Fbp_errorhandlers_views.py) # файл обработчика ошибок
- ### [bs_posts](app/bs_posts) # директория обработчика постов
  - [dao](app%2Fbp_posts%2Fdao) # директория DAO для постов
    - [comments_dao.py](app%2Fbp_posts%2Fdao%2Fcomments_dao.py) # DAO для комментариев
    - [posts_dao.py](app%2Fbp_posts%2Fdao%2Fposts_dao.py) # DAO для постов
  - [templates](app%2Fbp_posts%2Ftemplates) # шаблоны представлений для постов
    - [index.html](app%2Fbp_posts%2Ftemplates%2Findex.html) # шаблон главной страницы
    - [post.html](app%2Fbp_posts%2Ftemplates%2Fpost.html) # шаблон поста
    - [search.html](app%2Fbp_posts%2Ftemplates%2Fsearch.html) # шаблон поиска по содержимому
    - [tag.html](app%2Fbp_posts%2Ftemplates%2Ftag.html) # шаблон поиска по тегам
    - [user-feed.html](app%2Fbp_posts%2Ftemplates%2Fuser-feed.html) # шаблон постов одного пользователя
  - [bp_posts_views.py](app%2Fbp_posts%2Fbp_posts_views.py) # файл обработчика постов

## [config](config) # директория конфигурационных файлов
- ### [config.py](config/config.py) # файл конфигурации

## [data](data) # директория данных
  - [bookmarks.json](data%2Fbookmarks.json) # файл закладок
  - [comments.json](data%2Fcomments.json) # файл комментариев
  - [posts.json](data%2Fposts.json) # файл постов

## [logs](logs) # директория логов
  - [api.log](logs%2Fapi.log) # файл логов обработчика api

## [static](static) # директория стилей, картинок и аватарок
  - [css](static%2Fcss) # директория стилей
  - [img](static%2Fimg) # директория картинок и аватарок

## [templates](templates) # директория неиспользуемых шаблоны
  - [bookmarks.html](templates%2Fbookmarks.html) # шаблон поиска по закладкам 
  
## [tests](tests) # директория тестов
  - [api_test.py](tests%2Fapi_test.py) # файл для теста обработчика api
  - [conftest.py](tests%2Fconftest.py) # конфигурационный (установочный) файл тестов
  - [posts_dao_test.py](tests%2Fposts_dao_test.py) # файл для теста DAO постов, используемых в обработчике api 
