
from advanced.static.sample import static_sample

first = static_sample()
second = static_sample()
static_sample.update_counter(20)
third = static_sample()
static_sample.reset_counter()
fourth = static_sample()

first.print_id()
second.print_id()
third.print_id()
fourth.print_id()