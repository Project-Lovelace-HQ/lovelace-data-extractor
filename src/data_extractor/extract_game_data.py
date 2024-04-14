def extract_game_data(subscribed_games_updated_data_list):
    updated_games = [
        update_price_in_game(game) for game in subscribed_games_updated_data_list
    ]
    return find_lowest_priced_game(updated_games)


def update_price_in_game(game):
    updated_game = game.copy()
    updated_game["price"] = convert_price_to_float(game["price"])
    return updated_game


def convert_price_to_float(price):
    return float(price.replace("R$", "").strip().replace(",", "."))


def find_lowest_priced_game(game_list):
    return min(game_list, key=lambda game: game["price"])
