# Exercise 0

## 1. Hospital task

You have this json data, convert it into three tables: Hospital, Department and Doctor. Fill these tables with data. Do this manually and not programmatically.

```json
{
  "hospital": "Sjukhusstock",
  "address": "Drottninggatan 3, Stockholm",
  "departments": [
    {
      "name": "Kardiologi",
      "doctors": [
        { "id": 1, "name": "Dr. Abra Abrahamson" },
        { "id": 2, "name": "Dr. Erika Eriksson" }
      ]
    },
    {
      "name": "Neurologi",
      "doctors": [{ "id": 3, "name": "Dr. Sven Svensson" }]
    }
  ]
}
```

### Solution

Approach

- identify entities
- identify relationships and cardinalities
- create conceptual ERD
- create tables

**Initial naive conceptual ERD**

<img src = "../assets/initial_conceptual_model_ex1.png" width=300>

**Initial tables**

Hospital

| hospital_id | name         | address          |
| ----------- | ------------ | ---------------- |
| 1           | Sjukhusstock | Drottninggatan 3 |

Department

| department_id | name       |
| ------------- | ---------- |
| 1             | Kardiologi |
| 2             | Neurologi  |

Doctor

| doctor_id | name                |
| --------- | ------------------- |
| 1         | Dr. Abra Abrahamson |
| 2         | Dr. Erika Eriksson  |
| 3         | Dr. Sven Svensson   |

Refined with bridge tables to reflect many-to-many relationships

<img src = "../assets/conceptual_hospital_ex0_1.png" width=500>

HospitalDepartment

| hospital_department_id | hospital_id | department_id |
| ---------------------- | ----------- | ------------- |
| 1                      | 1           | 1             |
| 2                      | 1           | 2             |

HospitalDoctor

TODO: left for the reader

DepartmentDoctor

TODO: left for the reader


Test a join

Want information on Sjukhusstock and its departments
- hospital_department can join with department_id on department table and hospital_id on hospital_table
- query name from hospital table and name from department table 

TODO: left for reader: create this SQL query

---
## 2. Library Bookly

A library called Bookly keeps track of books and members who borrow them. Each book has a title, author, and ISBN number. Each member has a membership ID, name, and contact information. A member can borrow multiple books, but each book can be borrowed by only one member at a time.

a) Identify the entities and attributes for each entity.

b) Determine the relationship between member and books.

c) Draw a conceptual ERD using crow foots notation.


### Solution

a) Entities:

**Book**
- ISBN
- title
- author

> [!NOTE]
> ISBN is a unique number for a book, which could be used as a `primary key`, this will make it into a `natural key`

**Member**
- membership_id
- first_name
- last_name
- phone
- adress
- email

**Borrowing**
- borrowing_id
- ISBN
- membership_id
- return_date
- borrow_date


b) 

- A Member can have zero, one or several Borrowings
- A Borrowing can be made by one and only one Member
- A Borrowing is linked to one and only one Book
- A Book can be in zero, one or more Borrowings 


c) 

Initial conceptual ERD
<img src = "../assets/bookly_ex0_2_1.png" width=500>

<br>

Replaced many-to-many with a bridge table (composite entity)
<img src = "../assets/bookly_ex0_2_2.png" width=500>


--- 

## 3. Car rental

This is an ERD conceptual diagram that a database designer and the business stakeholders agreed upon in a car rental company called Carent.

<img src="https://github.com/kokchun/assets/blob/main/data_modeling/car_rental.png?raw=true" alt="car rent" width="500">

a) Describe the entities in this conceptual ERD.

b) Write out the relationship labels.

c) Describe the relationships between the entities (one-to-many, one-to-one and many-to-many).

d) Define the relationship statement for example: "A Customer can have one or more Rentals".


### Solution

a) 

- Customer is a person that can make rentals for cars.

- Car is the cars that can be rented by person

- Rental (composite entity) is a transaction between customers and cars


alternative to put in descriptions into the entities directly in conceptual ERD

<img src="../assets/carent_descriptive_conceptual.png" alt="car rent" width="500">

b) see image above

c) 

- Customer to rental (one-to-many)
- Rental to Customer (many-to-one)
- Rental to Car (many-to-one)
- Car to Rental (one-to-many)

d) 

- Each Customer makes one or more Rentals over time
- Each Rental is connected to one Customer
- Each Rental is for one Car
- Each Car can be in several Rentals  

## 5. University 

Conceptual ERD.   

<img src="../assets/university_exercise.png" alt="university" width="500">

 
