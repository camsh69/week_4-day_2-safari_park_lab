from models.staff import Staff
from models.animals import Animal

import repositories.staff_repository as staff_repo
import repositories.animals_repository as animals_repo

staff_repo.delete_all()
animals_repo.delete_all()

staff1 = Staff("Joe Bloggs", "21/03/2019", "Aquarium", 4)
staff_repo.save(staff1)
staff2 = Staff("Jane Bloggs", "21/05/2018", "Apes", 3)
staff_repo.save(staff2)
staff3 = Staff("Johny Morris", "21/06/2010", "Reptiles", 5)
staff_repo.save(staff3)

# all_staff = staff_repo.select_all()
# for staff in all_staff:
#     print(staff.name)

# staff_member = staff_repo.select(2)
# print(staff_member.name)

# staff_repo.delete(3)

# staff3.department = "Penguins"
# staff_repo.update(staff3)

animal1 = Animal("Pirhanna", "Fish", 1)
animals_repo.save(animal1)
animal2 = Animal("Guppy", "Fish", 1)
animals_repo.save(animal2)
animal3 = Animal("Gibbon", "Ape", 2)
animals_repo.save(animal3)
animal4 = Animal("Chimpanzee", "Ape", 2)
animals_repo.save(animal4)
animal5 = Animal("Cobra", "Reptile", 3)
animals_repo.save(animal5)

# all_animals = animals_repo.select_all()
# for animal in all_animals:
#     print(animal.name)

animal = animals_repo.select(2)
print(animal.name)
