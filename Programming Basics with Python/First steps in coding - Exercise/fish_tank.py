length = int(input())
width = int(input())
height = int(input())
percent_taken = float(input()) / 100

aquarium_volume = length * width * height
aquarium_volume_liters = aquarium_volume * 0.001

liters_needed = aquarium_volume_liters * (1 - percent_taken)

print(liters_needed)
