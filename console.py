from models.staff import Staff

import repositories.staff_repository as staff_repo

staff_repo.delete_all()

staff1 = Staff("Joe Bloggs", "21/03/2019", "Aquarium", 4)
staff_repo.save(staff1)
staff2 = Staff("Jane Bloggs", "21/05/2018", "Apes", 3)
staff_repo.save(staff2)
staff3 = Staff("Johny Morris", "21/06/2010", "Reptiles", 5)
staff_repo.save(staff3)

# all_staff = staff_repo.select_all()
# for staff in all_staff:
#     print(staff.name)

staff_member = staff_repo.select(2)
print(staff_member.name)
