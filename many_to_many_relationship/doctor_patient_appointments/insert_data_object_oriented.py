import mysql.connector
from faker import Faker
fake_data = Faker()


adapter = mysql.connector.connect(user= "root", password="testing123", database= "many_to_many_db")
client = adapter.cursor()

class Doctor:

    def __init__(self):
        self.id = None
        self.first_name = fake_data.first_name()
        self.last_name = fake_data.last_name()
        self.email = fake_data.email()
        self.phone_number = fake_data.phone_number()
        self.area = fake_data.city()
        self.specialist_in = fake_data.random_elements(elements=('skin', 'child', 'bones'), length=1, unique=False)
        self.working_hours = fake_data.random_elements(elements=('9AM to 12PM ', '12PM to 5PM', '11AM to 3PM'), length=1, unique=False)


    def save(self):
        sql_form = "INSERT INTO doctors(first_name, last_name, email, phone_number,area,specialist_in, working_hours ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        client.execute(sql_form, [self.first_name, self.last_name, self.email, self.phone_number, self.area , self.specialist_in[0], self.working_hours[0]])
        adapter.commit()

    @classmethod
    def random_doctor(cls):
        client.execute("Select * from doctors ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        doctor_object = {}
        for i in range(0, len(columns)):
            doctor_object[columns[i]] = result[i]            
        return doctor_object


class Patient:

    def __init__(self):
        self.id = None
        self.first_name = fake_data.first_name()
        self.last_name = fake_data.last_name()
        self.patient_age = fake_data.random_digit()
        self.sex = fake_data.random_elements(elements=('M', 'F', 'NA'), length=1, unique=False)
        self.city = fake_data.country()
        self.state_address = fake_data.state()

    def save(self):
        sql_form = "INSERT INTO patients(first_name, last_name, age , sex, city,state_address) VALUES (%s, %s, %s, %s, %s, %s)"
        client.execute(
        sql_form, 
        [ self.first_name, self.last_name, self.patient_age, self.sex[0], self.city , self.state_address]
        )
        adapter.commit()

    @classmethod
    def random_patient(cls):
        client.execute("Select * from patients ORDER BY RAND() limit 1")
        result = client.fetchone()
        columns = client.column_names
        patient_object = {}
        for i in range(0, len(columns)):
            patient_object[columns[i]] = result[i]            
        return patient_object        

class Appointment:
    def __init__(self, doctor_id, patient_id):
        self.id = None
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.concerned_problem = fake_data.lexify(text='???? ????? ???? ???', letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.appointment_time = fake_data.date(pattern='%Y-%m-%d', end_datetime=None)
        self.appointment_day = fake_data.day_of_week()
        self.booking_status = fake_data.random_elements(elements=('Completed','Cancelled'), length=1, unique=False)
        self.approval = fake_data.random_elements(elements=('Yes', 'No'), length=1, unique=False)

    def save(self):
        sql_form = "INSERT INTO appointments\
                    (doctor_id, patient_id, concerned_problem, appointment_time, appointment_day, booking_status, approval) \
                    VALUES (%s,%s, %s, %s,%s,%s,%s)"
        client.execute(sql_form, [
            self.doctor_id, self.patient_id, self.concerned_problem, self.appointment_time, 
            self.appointment_day, self.booking_status[0], self.approval[0]
        ])        
        adapter.commit()
    
    @classmethod
    def last(cls):
        client.execute("Select * from appointments order by id desc limit 1")
        result = client.fetchone()
        columns = client.column_names
        appointment_object = {}
        for i in range(0, len(columns)):
            appointment_object[columns[i]] = result[i]            
        return appointment_object




def insert_rows(row_count):
    for i in range(0, row_count):
        first_doctor = Doctor()    
        first_doctor.save()
        doctor = Doctor.random_doctor()

        first_patient = Patient()    
        first_patient.save()
        patient = Patient.random_patient()

        first_appointment = Appointment(doctor['id'], patient['id'])
        first_appointment.save()
        appointment = Appointment.last()
        
        print(doctor)
        print(patient)
        print(appointment)
        


insert_rows(5)
  
        
        

