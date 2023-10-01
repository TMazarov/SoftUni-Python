budget = float(input())

gpu_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

gpu_price = 250
cpu_price = (gpu_quantity * gpu_price) * 0.35
ram_price = (gpu_quantity * gpu_price) * 0.10

total_gpu = gpu_quantity * gpu_price
total_cpu = cpu_quantity * cpu_price
total_ram = ram_quantity * ram_price

final_price = total_gpu + total_cpu + total_ram

if gpu_quantity > cpu_quantity:
    final_price = final_price - (final_price * 0.15)


if final_price <= budget:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")
