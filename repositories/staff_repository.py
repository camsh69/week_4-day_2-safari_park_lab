from models.staff import Staff
from db.run_sql import run_sql


def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)


def save(staff_member):
    sql = "INSERT INTO staff (name, start_date, department, performance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff_member.name, staff_member.start_date,
              staff_member.department, staff_member.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff_member.id = id
    return staff_member


def select_all():
    staff = []

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        staff_member = Staff(row['name'], row['start_date'],
                             row['department'], row['performance'])
        staff.append(staff_member)
    return staff


def select(id):
    staff_member = None
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff_member = Staff(result['name'], result['start_date'],
                             result['department'], result['performance'], result['id'])
    return staff_member


def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(staff_member):
    sql = "UPDATE staff SET (name, start_date, department, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff_member.name, staff_member.start_date,
              staff_member.department, staff_member.performance, staff_member.id]
    run_sql(sql, values)
