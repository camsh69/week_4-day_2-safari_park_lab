from models.staff import Staff

import repositories.staff_repository as staff_repo

staff_repo.delete_all()

staff1 = Staff("Joe Bloggs", "21/03/2019", "Aquarium", 4)
staff_repo.save(staff1)

staff2 = Staff("Jane Bloggs", "21/03/2019", "Apes", 4)
staff_repo.save(staff2)

all_staff = staff_repo.select_all()
for staff in all_staff:
    print(staff.name)
