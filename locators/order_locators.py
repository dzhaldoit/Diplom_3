from selenium.webdriver.common.by import By


class OrderLocators:
    BUN_INGREDIENT = By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]'
    BASKET_ORDER = By.XPATH, './/section[contains(@class, "BurgerConstructor_basket__29Cd7")]'
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]'
    CREATE_ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'
    LIST_ORDER_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]'
    HISTORY_ORDER_BUTTON = By.XPATH, './/a[text()="История заказов"]'
    COMLETED_INVISIBLE = By.XPATH, './/li[text()="Все текущие заказы готовы!"]'
    MODULE_WINDOW = By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]'

    WINDOW_LIST_ORDER = By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]'
    CLICK_ORDER_IN_LIST_ORDER = By.XPATH, '//a[@class="OrderHistory_link__1iNby"]'
    TEXT_NUMBER_ORDER_IN_MODAL_WINDOW = By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq"
    CLOSE_MODAL_WINDOW_BUTTON = By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//button[contains(@class,"Modal_modal__close_modified")]'

    INGRADIENT_CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    IN_PROGRESS_ORDER = '.OrderFeed_orderListReady__1YFem'
    COMPLETED_ORDER_LIST = By.XPATH, '//*[contains(@class, "orderListReady")]/child::li[@class="text text_type_digits-default mb-2"]'

    TEXT_COMPLETED_ALL_TIME = By.XPATH, '//*[text()="Выполнено за все время:"]/following::p[1]'
    TEXT_COMPLETED_TODAY = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::p[1]'
    NUMBER_ORDER_INVISIBLE = By.XPATH, './/h2[text()="9999"]'

    ORDER_IN_LIST_ORDERS = By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'

    INGREDIENT_DETAILS = By.XPATH, './/h2[text()="Детали ингредиента"]'
    CALORIES_INGREDIENT = By.XPATH, './/p[text()="643"]'
    COUNT_INGREDIENT = By.XPATH, '//p[contains(@class, "counter")]'
