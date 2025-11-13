# Working with Sets
from pyscript import display

emerald = {'Banaag', 'Casal', 'DelaCruz'}
peaceful = {'Valencia', 'Rodriguez', 'Lua'}
students = emerald | peaceful
math = {'Casal', 'DelaCruz', 'Lua'}
writing = {'Banaag', 'Valencia', 'Lua', 'Rodriguez'}
both = math & writing
one = math - writing

display(f"All students: {students}", target='output')
display(f"Math Club members: {math}", target='output')
display(f"Writing Club members: {writing}", target='output')
display(f"Students in one club: {both}", target='output')
display(f"Students in only one club: {one}", target='output')