#### Setting up your models

## Part 1: Make your base model
* After setting up your project, navigate to the models.py folder
* Create your models similar to the ones below, replacing fields and data types with ones relevant to your project
```
class Owner(models.Model):
    name = models.CharField(max_length=45)
    species = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pet(models.Model):
    name = models.CharField(max_length=45)
    species = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    description = models.TextField()
    hasFur = models.BooleanField()
    numLegs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
* ENSURE that your models are set up the way you want them and that all fields are of their proper data types

## Part 2: Adding relationships
* If your models are related to one another somehow, create those relationships in your models
* For a one to many relationship, set up the connection inside the many model (ex: there is a one to many relationship between pets and owners, with one owner owning many pets and many pets being owned by one person)
* In your many model (in this case, the pet):
`owner = models.ForeignKey(Owner, related_name="pets_owned", on_delete=models.CASCADE`
* Remember you do NOT need to specify the one to many relationship in both models, just one (it does have to be in the many model)

## Part 3: Migrate
* Run `python manage.py makemigrations` ONLY when you are sure your models are set up properly and complete
* Your models are now staged to be set in your database, and your terminal should reflect that the models were set up
* Run `python manage.py migrate` to push the staged models to your database 

## Part 4: Start adding data
* If you'd like to add data using the shell, run `python manage.py shell` to enter the shell
* You should see >>> _ to indicate you are in the shell now
* Type `from your_app_name.models import *` to import models
* Start creating!
* Note: remember that when adding a pet (the many of the one to many relationship) it is DEPENDENT on the existence of the one model it is related to
    * The many model must have a filled in foreign key when creating the instance -- this data must be an instance of the one model
    * EX: `Pet.objects.create(name="Skipper",species="Space Monkey",gender="Asexual",description="Space monkey!!",hasFur=False,numLegs=12,owner=Owner.objects.get(id=1))`

## Some common commands:
* Create a new instance of a class--be sure to replace the ClassName with your model name and the fields with the proper fields from your model: `ClassName.objects.create(field1="Data1",field2=False,field3=29,field4="Data4")`
* Get ALL instances in your model: `ClassName.objects.all()`
* Get ONE instance in your model by the id: `ClassName.objects.get(id=1)`
* Get the FIRST instance in your model: `ClassName.objects.first()`
* Get the LAST instance in your model: `ClassName.objects.last()`
* FILTER by a specific field value: `four_legged = ClassName.objects.filter(numLegs=4)`
* UPDATE an existing record:
    * GET the record first and put it in a variable `obj = ClassName.objects.get(id=1)`
    * Update the specific field: `obj.field1 = "Something else"`
    * Save the changes: `obj.save()`
* DELETE an existing record:
    * GET the record first and put it in a variable `obj = ClassName.objects.get(id=1)`
    * Delete the instance: `obj.delete()`

## Rendering Data to the Templates
### Start with calling the data and putting it in context (don't forget to import models!):
```
from .models import Owner, Pet

def index(request):
    context = {
        "all_owners": Owner.objects.all(),
        "all_pets": Pet.objects.all()
    }
    return render(request, "index.html", context)
```
### Then render on the appropriate template:
```
<h2>All Owners and their pets</h2>
    <ul>
        {% for x in all_owners %}
        <li>{{ x.name }} the {{ x.species }}</li>
        <ul>
            {% for i in x.pets_owned.all %}
                <li>{{ i.name }} the {{ i.species }}</li>
            {% endfor %}
        </ul>
        {% endfor %}
    </ul>
    <h2>All pets and their owners</h2>
    <ul>
        {% for j in all_pets %}
        <li>{{ j.name }} the {{ j.species }}</li>
        <ul>
            <li>{{ j.owner.name }} the {{ j.owner.species }}</li>
        </ul>
        {% endfor %}
    </ul>
```

## Happy Coding!