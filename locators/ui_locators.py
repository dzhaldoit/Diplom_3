class Locators:
    PERSONAL_ACCOUNT_BUTTON = './/p[text()="Личный Кабинет"]'
    EMAIL_INPUT = './/input[@type="text"]'
    PASSWORD_INPUT = './/input[@type="password"]'
    LOGIN_BUTTON = './/button[text()="Войти"]'
    LOGOUT_BUTTON = './/button[text()="Выход"]'
    TEXT_LOGOUT = './/h2[text()="Вход"]'
    SAVE_BUTTON = './/button[text()="Сохранить"]'

    TEXT_RECOVERY = './/h2[text()="Восстановление пароля"]'
    RECOVERY_PASSWORD_BUTTON = './/a[text() ="Восстановить пароль"]'
    RECOVERY_BUTTON = '//button[text()="Восстановить"]'

    EYE_BUTTON = '//div[contains(@class, "input_status_active")]'

    BUN_INGREDIENT = './/img[@alt="Флюоресцентная булка R2-D3"]'
    BASKET_ORDER = './/section[contains(@class, "BurgerConstructor_basket__29Cd7")]'
    CONSTRUCTOR_BUTTON = './/p[text()="Конструктор"]'
    CREATE_ORDER_BUTTON = './/button[text()="Оформить заказ"]'
    LIST_ORDER_BUTTON = './/p[text()="Лента Заказов"]'
    HISTORY_ORDER_BUTTON = './/a[text()="История заказов"]'
    COMLETED_INVISIBLE = './/li[text()="Все текущие заказы готовы!"]'
    MODULE_WINDOW = './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]'

    WINDOW_LIST_ORDER = './/ul[@class="OrderFeed_list__OLh59"]'
    CLICK_ORDER_IN_LIST_ORDER = '//a[@class="OrderHistory_link__1iNby"]'
    TEXT_NUMBER_ORDER_IN_MODAL_WINDOW = ".Modal_modal__title_shadow__3ikwq"
    CLOSE_MODAL_WINDOW_BUTTON = '//section[contains(@class,"Modal_modal_opened")]//button[contains(@class,"Modal_modal__close_modified")]'

    IN_PROGRESS_ORDER = '.OrderFeed_orderListReady__1YFem'
    COMPLETED_ORDER_LIST = ('//*[contains(@class, "orderListReady")]/child:'
                            ':li[@class="text text_type_digits-default mb-2"]')

    TEXT_COMPLETED_ALL_TIME = '//*[text()="Выполнено за все время:"]/following::p[1]'
    TEXT_COMPLETED_TODAY = '//*[text()="Выполнено за сегодня:"]/following::p[1]'
    NUMBER_ORDER_INVISIBLE = './/h2[text()="9999"]'

    ORDER_IN_LIST_ORDERS = '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'

    INGREDIENT_DETAILS = './/h2[text()="Детали ингредиента"]'
    CALORIES_INGREDIENT = './/p[text()="643"]'

    COUNT_INGREDIENT = '//p[contains(@class, "counter")]'

    TEXT_PASSWORD_RECOVERY = '//input[@value=""]'
