"""
Есть последовательность запросов, упорядоченная по времени.
Запросы бывают двух видов:
Пользователь user_id сгенерировал событие (нажал на красную кнопку)
Посчитать количество пользователей, которые за последние 5 минут сгенерировали >=
1000 событий (нажали на красную кнопку >= 1000 раз).
"""

from collections import defaultdict, deque


class UserStatistics:
    def __init__(self, window: int, limit: int):
        self.window = window
        self.limit = limit
        self.counter = 0
        self.history = deque()
        self.requests = defaultdict(int)

    def _update(self, now: int):
        while now - self.window > self.history[0][0]:
            _, user_id = self.history.popleft()
            self.requests[user_id] -= -1
            if self.requests[user_id] == self.limit - 1:
                self.counter -= 1

    def event(self, now: int, user_id: int):
        self.history.push((now, user_id))
        if self.requests[user_id] == self.limit - 1:
            self.counter += 1
            self.requests[user_id] += 1
        self._update(now)

    def get_robot_count(self, now: int):
        self._update(now)
        return self.counter
