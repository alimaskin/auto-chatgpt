from autochatgpt.autobot import AutoBot
from seleniumbase import SB

def autobot():
    with SB(uc=True, headed=True, headless=False) as driver:

        bot = AutoBot(driver, wait=10)
        bot.auto_login()
        bot.set_chat_history_and_training(check=False)
        bot.set_gpt_model(model_version="GPT-3.5")
        bot.send_prompt(prompt="Hello, world!")
        # user_prompt = bot.get_user_prompt()
        gpt_response = bot.get_gpt_response()


        print(gpt_response)

        # Teardown
        bot.driver.quit()

autobot()