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
