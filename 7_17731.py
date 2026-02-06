original_size = 60
channels_ratio = 2 / 4          # стерео / квадро
sample_rate_ratio = 1 / 3       # частота в 3 раза меньше
bit_depth_ratio = 4.5           # разрешение в 4.5 раза выше
# или точнее: bit_depth_ratio = 9 / 2

new_size = original_size * channels_ratio * sample_rate_ratio * bit_depth_ratio
print(int(new_size))            # выводит 45
