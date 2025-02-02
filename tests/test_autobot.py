from autochatgpt.autobot import AutoBot


def test_autobot():
    # Test ChatGPTBot class
    bot = AutoBot(debug_mode=True, wait=10)
    bot.auto_login()
    bot.set_chat_history_and_training(check=False)
    bot.set_gpt_model(model_version="GPT-3.5")
    bot.send_prompt(prompt="Hello, world!")
    # user_prompt = bot.get_user_prompt()
    gpt_response = bot.get_gpt_response()

    # Check if the user prompt and GPT response are not empty
    # assert user_prompt is not None
    assert gpt_response is not None

    print(gpt_response)

    # Teardown
    bot.driver.quit()
