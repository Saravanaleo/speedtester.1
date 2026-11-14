import time
prompt =("With great power comes greater responsibility"
         "")
print("Type the sentence below and hit ENTER:\n")
print(f'"{prompt}"\n')
input("Press ENTER when you are ready to begin...")
start = time.time()
user_input = input("\nStart typing:")
elapsed = time.time() - start
word_count = len(user_input.split())
wpm = round((word_count / (elapsed / 60))) if elapsed > 0 else 0
correct_chars = sum(1 for a, b in zip(user_input, prompt) if a == b)
accuracy = round((correct_chars / max(len(prompt),1)) * 100, 1)
print("\n--- Results ---")
print(f"Time Taken :{elapsed:.2f} seconds"
      f"")
print(f"Speed :{wpm} WPM")
print(f"Accuracy :{accuracy}%")

