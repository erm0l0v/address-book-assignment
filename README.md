# Address Book

## Run tests

```
python setup.py test
```

#### Run tests with tox

install python 2.7, 3.3, 3.4, 3.5, 3.6
install tox

```
tox
```

#### Run tests in docker

Install Docker and docker-compose

```
docker-compose run --rm test
```

## API

#### Create Book

``` python
import address_book


book_repository = address_book.create_book()
```

#### Create Objects

``` python
from address_book import models


group = models.Group('Siths')
person = models.Person('Darth', 'Vader', groups={group})
```

And save

``` python
book_repository = address_book.create_book()
book_repository.save(group)
book_repository.save(person)
```

#### Get Persons by Group

``` python
from address_book import models


group = models.Group('Siths')
person = models.Person('Darth', 'Vader', groups={group})

book_repository = address_book.create_book()
book_repository.save(person) # grops saved authomaticaly

group.persons # -> {person}
```

#### Get Groups by Person

``` python
from address_book import models


person = models.Person('Darth', 'Vader')
group = models.Group('Siths', persons={group})

book_repository = address_book.create_book()
book_repository.save(group) # persons saved authomaticaly

person.groups # -> {group}
```

#### Find person by name

``` python
book_repository.find_persons_by_name('Vader Darth')
```

#### Find person by email

``` python
person = models.Person('Darth', 'Sidious', emails={'dsidious@death-star.com'})
person = models.Person('Darth', 'Vader', emails={'dvader@death-star.com'})
book_repository.save(person)

book_repository.find_persons_by_email('death-star.com')
# will return persons: Darth Vader and Darth Sidious
```
