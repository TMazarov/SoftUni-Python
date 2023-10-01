actor_name = input()
academy_score = float(input())
judges = int(input())


max_result = 1250.5
actors_result = academy_score

for i in range(1, judges + 1):
    judge_name = input()
    score = float(input())

    actors_result += ((len(judge_name) * score) / 2)

    if actors_result > max_result:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actors_result:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {max_result - actors_result:.1f} more!")
