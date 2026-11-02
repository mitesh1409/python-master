# dataclasses

Why use dataclasses

* Support for default values
* Custom representations of the objects
* Easy tuple or a dictionary conversion
* Custom properties
* Frozen instances

```python
from dataclasses import dataclass

@dataclass
class Cookie:
    name: str
    quantity: int = 0 

chocolate_chip = Cookie("chocolate chip", 13)
print(chocolate_chip.name)
print(chocolate_chip.quantity) 
```

Output  

```plaintext
chocolate chip
13 
```

---

```python
from dataclasses import asdict, astuple

ginger_molasses = Cookie("ginger molasses", 8)

asdict(ginger_molasses) # {'name': 'ginger molasses', 'quantity': 8}

astuple(ginger_molasses) # ('ginger molasses', 8) 
```

---

**Custom Properties**

```python
from decimal import Decimal

@dataclass
class Cookie:
    name: str
    cost: Decimal
    quantity: int

    @property
    def value_of_goods(self):
        return int(self.quantity) * self.cost

# Using custom properties
peanut = Cookie("peanut butter", Decimal("1.2"), 8)
peanut.value_of_goods # Decimal('9.6')
```

---

**Frozen instances**

```python
@dataclass(frozen=True)
class Cookie:
    name: str
    quantity: int = 0

c = Cookie("chocolate chip", 10) 
c.quantity = 15 
```

Output  

```plaintext
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'quantity' 
```
