# SCHOOL APP


School an application to create, list, edit delete Students and Teachers.

A system where we can have a Teacher and Student. 

- One teacher can have many students and students can have many teachers.

- User be able to do the following:

  - List/add/edit/delete teachers.
  - List/add/edit/delete students.
  - Mark a student with exceptional students with a “star”.
  

## How to run it

- Clone the repo from GitHub
```
git clone https://github.com/neeraj9194/school-app
```

- Navigate to the repository root:
```
cd school-app
```

- (Optional) Now if you want you can load a fixture which will prepopulated
data for you. 
```
bin/load-fixture.sh
```

- Now, you just need to do
```
docker-compose up
```

_Note: use `sudo` if permission issue._

## TODO

- [x] Dashboard
- [x] Complete readme docs.
- [x] Add fixture generator.
- [x] Complete `docker-compose up`
- [x] Relationship for Rewards(Stars).
- [ ] Include code coverage numbers/details in the README or your response.
- [x] Login
- [x] Add unit tests as well as appropriate. 
- [ ] Search in list
- [ ] Image Upload.??
- [ ] Add Staff ID in teacher model.
- [ ] Role based permissions.??
