def test_positive_1(page_search_1):
    assert page_search_1 == "Страница содержит текст 'User-oriented Web UI browser tests in Python' "


def test_negative_1(page_search_2):
    assert page_search_2 == "Страница содержит текст 'По запросу asdghagsydgkaysgdyla ничего не найдено.' "
