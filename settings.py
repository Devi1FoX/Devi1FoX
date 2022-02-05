class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1300
        self.screen_height = 600
        self.bg_color = (180, 81, 165)

        # налаштування корабля
        self.ship_speed = 3.5
        self.ship_limit = 2

        # Параметры снаряда
        self.bullet_speed = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        

        # Темп ускорение игры
        self.speedup_scale = 1.3
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speedr = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_derection = 1 обозначает движение вправо; a -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



