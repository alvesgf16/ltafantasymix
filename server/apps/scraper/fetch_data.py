from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get(
    "https://gol.gg/players/list/season-S15/split-Spring/tournament-ALL/"
)


def filter_leagues_for_lta_regions():
    select_league("LTA North")
    select_league("LTA South")
    apply_filters()


def select_league(league_name):
    # Use JavaScript to access the selectize API and add items
    script = f"""
    var selectize = $('#leagueFilter')[0].selectize;
    selectize.addItem('{league_name}');
    """

    driver.execute_script(script)


def apply_filters():
    refresh_button = driver.find_element(By.ID, "btn_refresh")
    refresh_button.click()


def filter_players_by_roles():
    number_of_role_links = len(
        driver.find_elements(By.CSS_SELECTOR, "#roleBox a")
    )
    for i in range(1, number_of_role_links):
        role_link = driver.find_elements(By.CSS_SELECTOR, "#roleBox a")[i]
        role_link.click()


try:
    filter_leagues_for_lta_regions()
    filter_players_by_roles()

finally:
    driver.quit()
