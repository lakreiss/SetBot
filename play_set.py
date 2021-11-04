from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from set_card import SetCard 

class SetBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager(version="95.0.4638.54").install())
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def begin_game(self):
        self.driver.get('https://setwithfriends.com')

        # close popup
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button').click()

        # make a private game
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[1]/button[2]').click()

        # begin the game
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/button').click()

    def make_match(self):
        sleep(1)
        board_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]')
        processed_board = self.get_processed_board(board_element)
        match = self.find_match(processed_board)
        if match:
            for card in match:
                # print(str(card))
                card.parent.click()
            return True
        else:
            return False

    def find_match(self, processed_board):
        for i in range(len(processed_board)):
            for j in range(i + 1, len(processed_board)):
                for k in range(j + 1, len(processed_board)):
                    cards = [processed_board[i], processed_board[j], processed_board[k]]
                    numbers = set([card.number for card in cards])
                    colors = set([card.color for card in cards])
                    shapes = set([card.shape for card in cards])
                    shades = set([card.shade for card in cards])
                    if (len(numbers) == 1 or len(numbers) == 3) and (len(colors) == 1 or len(colors) == 3) and (len(shapes) == 1 or len(shapes) == 3) and (len(shades) == 1 or len(shades) == 3):
                        return cards
        return None

    def get_processed_board(self, board_element):
        board_divs = board_element.find_elements(By.TAG_NAME, 'div')
        visibile_divs = [board_div for board_div in board_divs if 'jss82' in board_div.get_attribute("class")]
        return self.get_processed_cards(visibile_divs)
    
    def get_processed_cards(self, visibile_divs):
        all_cards = []
        for div in visibile_divs:
            svgs = div.find_elements(By.TAG_NAME, 'svg')
            number = len(svgs)
            uses = svgs[0].find_elements(By.TAG_NAME, 'use')

            # print(number, use.get_attribute('href'), use.get_attribute('mask'), use.get_attribute('fill'))
            all_cards.append(SetCard(div.find_element(By.XPATH, '..'), number, uses[0].get_attribute('href'), uses[0].get_attribute('mask'), uses[0].get_attribute('fill'), uses[1].get_attribute('stroke')))
        return all_cards

bot = SetBot()
bot.begin_game()

while bot.make_match():
    continue