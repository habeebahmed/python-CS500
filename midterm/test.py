def main() -> None:
    dict_countries: dict[str, str] = {
        "india": "delhi",
        "china": "beijing",
        "germany": "berlin",
        "thailand": "bangkok",
        "japan": "tokyo",
        "united states": "washington, d.c",
        "afghanistan": "kabul",
        "antigua and barbuda": "st. john's"
    }

    correct_count: int = 0

    for country, captial in dict_countries.items():
        user_input: str = input(f"What is the capital of {country}?")
        if user_input == captial:
            correct_count += 1
            print("Your answer is correct")
        else:
            print(f"The correct answer should be {capcaptialital_cap}")

    print(f"The correct count is {correct_count}")



if __name__=="__main__":
    main()

