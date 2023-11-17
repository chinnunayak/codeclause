import time

def calculate_accuracy(prompt, user_input):
    prompt_words = prompt.split()
    user_words = user_input.split()

    correct_words = sum(w1 == w2 for w1, w2 in zip (prompt_words, user_words))
    accuracy_percentage = (correct_words / len(prompt_words)) * 100

    return accuracy_percentage

def speed_typing_test():
    user_prompt = input("Enter the text for the typing test: ")

    print("\nType the following text:")
    print(user_prompt)

    input("Press Enter When you are ready to start.")

    start_time = time.time()

    user_input = input("Type here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    accurancy_percentage = calculate_accuracy(user_prompt, user_input)

    print(f"\nYour typing accuracy: {accurancy_percentage:.2f}%")

if __name__ == "__main__":
    speed_typing_test()
