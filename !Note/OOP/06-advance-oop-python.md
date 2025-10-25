## Key Advanced Concepts Summary
> Here's what we've covered in this advanced section:

1. Metaclasses & Dynamic Classes
- Control class creation
- Automatic registration
- Dynamic attribute generation

2. Descriptors

- Low-level attribute control
- Validation at descriptor level
- Lazy loading patterns

3. Context Managers

- Resource management
- `__enter__` and `__exit__`
- Custom with statements

4. Advanced Decorators

- Class decorators
- Method decorators with state
- Decorator factories

5. Multiple Inheritance & MRO

- Diamond problem
- Cooperative inheritance
- Mixin patterns

6. Design Patterns

- Singleton, Factory, Builder
- Observer, Strategy
- Command, Mediator

7. Type System

- Generics with TypeVar
- Protocols for structural typing
- Method overloading

8. Modern Python Features

- Dataclasses
- Enums with methods
- Async OOP

9. Memory Management

- `__slots__` for optimization
- Weak references
- Garbage collection awareness

10. Advanced Property Patterns

- Cached properties
- Computed properties
- Dependent properties


### Best Practices for Advanced OOP

Favor Composition Over Inheritance

- More flexible
- Easier to test
- Better encapsulation


Use ABCs for Interfaces

- Clear contracts
- Better documentation
- Enforce implementation


Apply SOLID Principles

- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion


Type Hints Everywhere

- Better IDE support
- Catch errors early
- Self-documenting code


Immutability When Possible

- Thread-safe
- Easier to reason about
- Fewer bugs


Keep Classes Focused

- One responsibility
- Small, cohesive units
- Easy to understand



You now have comprehensive knowledge of Python OOP from basic to advanced! Would you like me to explain any specific concept in more detail or provide more examples for a particular pattern?



 

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>



  

# Advanced Python OOP Concepts
Let me dive into more advanced topics that will take your OOP skills to the next level!

# 1. Advanced Decorators and Method Types

### A. Custom Decorators for Classes
```py
pythondef singleton(cls):
    """Decorator to make a class a singleton"""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "Connected"
    
    def query(self, sql):
        return f"Executing: {sql}"

# Always returns the same instance
db1 = Database()
db2 = Database()
print(db1 is db2)  # True
print(id(db1) == id(db2))  # True
```

### B. Method Chaining
```py
pythonclass QueryBuilder:
    def __init__(self):
        self._query = []
        self._params = {}
    
    def select(self, *fields):
        self._query.append(f"SELECT {', '.join(fields)}")
        return self  # Return self for chaining
    
    def from_table(self, table):
        self._query.append(f"FROM {table}")
        return self
    
    def where(self, condition):
        self._query.append(f"WHERE {condition}")
        return self
    
    def order_by(self, field, direction="ASC"):
        self._query.append(f"ORDER BY {field} {direction}")
        return self
    
    def limit(self, count):
        self._query.append(f"LIMIT {count}")
        return self
    
    def build(self):
        return " ".join(self._query)

# Method chaining in action
query = (QueryBuilder()
         .select('name', 'age', 'email')
         .from_table('users')
         .where('age > 18')
         .order_by('name')
         .limit(10)
         .build())

print(query)
# SELECT name, age, email FROM users WHERE age > 18 ORDER BY name ASC LIMIT 10
```

<br>
<br>
<br>
<br>



### 2. Context Managers (with statement)
```py
pythonclass FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        
        return False  # Propagate exception

# Using context manager
with FileManager('test.txt', 'w') as f:
    f.write("Hello, World!")

# Alternative using contextlib
from contextlib import contextmanager

@contextmanager
def timer(name):
    import time
    start = time.time()
    print(f"Starting {name}")
    yield
    end = time.time()
    print(f"{name} took {end - start:.2f} seconds")

with timer("Complex Operation"):
    sum([i**2 for i in range(1000000)])
```

### 3. Descriptors (Advanced Attribute Control)
```py
pythonclass ValidatedAttribute:
    def __init__(self, name, validator=None):
        self.name = f"_{name}"
        self.validator = validator
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)
    
    def __set__(self, obj, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value: {value}")
        setattr(obj, self.name, value)
    
    def __delete__(self, obj):
        delattr(obj, self.name)

class TypedAttribute:
    def __init__(self, name, expected_type):
        self.name = f"_{name}"
        self.expected_type = expected_type
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}, got {type(value)}")
        setattr(obj, self.name, value)

class Person:
    name = TypedAttribute('name', str)
    age = ValidatedAttribute('age', lambda x: isinstance(x, int) and 0 <= x <= 150)
    email = ValidatedAttribute('email', lambda x: '@' in str(x))
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

person = Person("Alice", 30, "alice@example.com")
print(person.name)  # Alice

# person.age = 200  # ValueError: Invalid value
# person.name = 123  # TypeError: Expected <class 'str'>, got <class 'int'>
```

<br>
<br>
<br>
<br>


# 4. Metaclasses (Class Factories)
```py
pythonclass AutoReprMeta(type):
    """Metaclass that automatically creates __repr__ method"""
    
    def __new__(cls, name, bases, dct):
        # Find all non-private attributes from __init__
        if '__init__' in dct:
            import inspect
            sig = inspect.signature(dct['__init__'])
            params = [p for p in sig.parameters.keys() if p != 'self']
            
            def __repr__(self):
                args = ', '.join(f"{p}={getattr(self, p)!r}" for p in params)
                return f"{name}({args})"
            
            dct['__repr__'] = __repr__
        
        return super().__new__(cls, name, bases, dct)

class Point(metaclass=AutoReprMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(repr(p))  # Point(x=10, y=20)

# Metaclass for enforcing abstract methods
class StrictMeta(type):
    def __new__(cls, name, bases, dct):
        # Check if all abstract methods are implemented
        abstract_methods = set()
        
        for base in bases:
            if hasattr(base, '_abstract_methods'):
                abstract_methods.update(base._abstract_methods)
        
        if '_abstract_methods' in dct:
            abstract_methods.update(dct['_abstract_methods'])
        
        for method in abstract_methods:
            if method not in dct:
                raise TypeError(f"{name} must implement {method}")
        
        return super().__new__(cls, name, bases, dct)

# Singleton metaclass
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

config1 = Config()
config2 = Config()
print(config1 is config2)  # True
```

<br>
<br>
<br>
<br>


# 5. Multiple Inheritance and MRO (Method Resolution Order)
```py
pythonclass A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B -> " + super().method()

class C(A):
    def method(self):
        return "C -> " + super().method()

class D(B, C):
    def method(self):
        return "D -> " + super().method()

d = D()
print(d.method())  # D -> B -> C -> A
print(D.mro())     # [D, B, C, A, object]

# Diamond Problem Solution
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__ called for {name}")

class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded
        print(f"Mammal.__init__ called")

class Flyer(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
        print(f"Flyer.__init__ called")

class Bat(Mammal, Flyer):
    def __init__(self, name):
        # Use cooperative inheritance
        super().__init__(name)
        print(f"Bat.__init__ called")

bat = Bat("Batsy")
print(Bat.mro())
```

<br>
<br>
<br>
<br>


# 6. Mixins (Reusable Functionality)
```py
pythonclass JSONMixin:
    """Mixin to add JSON serialization"""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(**data)

class ComparableMixin:
    """Mixin to add comparison operators"""
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return str(self) < str(other)
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        return not self.__le__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)

class LoggingMixin:
    """Mixin to add logging capabilities"""
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JSONMixin, ComparableMixin, LoggingMixin):
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
    
    def __str__(self):
        return f"{self.username} ({self.age})"

user1 = User("alice", "alice@example.com", 30)
user2 = User("bob", "bob@example.com", 25)

# Using JSONMixin
json_str = user1.to_json()
print(json_str)

# Using ComparableMixin
print(user1 > user2)  # True (alice > bob alphabetically)

# Using LoggingMixin
user1.log("User logged in")
```

<br>
<br>
<br>
<br>


# 7. Slots (Memory Optimization)
```py
pythonclass NormalClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']  # Only these attributes allowed
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys

normal = NormalClass(1, 2)
slotted = SlottedClass(1, 2)

print(f"Normal size: {sys.getsizeof(normal.__dict__)} bytes")
print(f"Slotted size: {sys.getsizeof(slotted)} bytes")

# Slots prevent adding new attributes
# slotted.z = 3  # AttributeError: 'SlottedClass' object has no attribute 'z'
normal.z = 3  # This works fine

# Inheritance with slots
class Parent:
    __slots__ = ['a']

class Child(Parent):
    __slots__ = ['b']  # Total slots: 'a' and 'b'

child = Child()
child.a = 1
child.b = 2
```
<br>
<br>
<br>
<br>

# 8. Callable Objects
```py
pythonclass Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self, increment=1):
        """Make instances callable like functions"""
        self.count += increment
        return self.count

counter = Counter()
print(counter())     # 1
print(counter(5))    # 6
print(counter(3))    # 9

# Function factory using callable classes
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```
<br>
<br>
<br>
<br>


# 9. Advanced Property Patterns
```py
pythonclass LazyProperty:
    """Descriptor for lazy-loaded properties"""
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        # Calculate value only once
        value = self.func(obj)
        # Store it in instance __dict__ to override descriptor
        setattr(obj, self.name, value)
        return value

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @LazyProperty
    def expensive_computation(self):
        print("Computing... (this happens only once)")
        return sum(x**2 for x in self.data)

processor = DataProcessor([1, 2, 3, 4, 5])
print(processor.expensive_computation)  # Computing...
print(processor.expensive_computation)  # Uses cached value

# Cached property (similar to functools.cached_property)
class CachedProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        value = self.func(obj)
        obj.__dict__[self.func.__name__] = value
        return value
    
    def __set_name__(self, owner, name):
        self.name = name
```
<br>
<br>
<br>
<br>


# 10. Abstract Base Classes (Advanced)
```py
pythonfrom abc import ABC, abstractmethod
from collections.abc import Sequence

class DataValidator(ABC):
    @abstractmethod
    def validate(self, data):
        """Validate data"""
        pass
    
    @abstractmethod
    def clean(self, data):
        """Clean/sanitize data"""
        pass
    
    # Concrete method with default implementation
    def process(self, data):
        cleaned = self.clean(data)
        if self.validate(cleaned):
            return cleaned
        raise ValueError("Invalid data")
    
    # Class method in ABC
    @classmethod
    def supports(cls, data_type):
        return data_type in cls.supported_types

class EmailValidator(DataValidator):
    supported_types = ['email', 'string']
    
    def validate(self, data):
        return '@' in data and '.' in data
    
    def clean(self, data):
        return data.strip().lower()

validator = EmailValidator()
print(validator.process("  Alice@EXAMPLE.COM  "))  # alice@example.com

# Custom abstract property
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")
```
<br>
<br>
<br>
<br>


# 11. Protocol Classes (Structural Subtyping)
```py
pythonfrom typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    """Protocol defining what makes something drawable"""
    def draw(self) -> str:
        ...

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        return f"Drawing circle with radius {self.radius}"

class Square:
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        return f"Drawing square with side {self.side}"

def render(shape: Drawable):
    """Works with any object that has draw() method"""
    print(shape.draw())

circle = Circle(5)
square = Square(10)

render(circle)  # Works
render(square)  # Works

# Runtime check
print(isinstance(circle, Drawable))  # True
```
<br>
<br>
<br>
<br>


# 12. Operator Overloading (Complete Set)

```py
import math
from typing import Union

class Vector:
    """Advanced Vector class with complete operator overloading"""
    
    def __init__(self, *components):
        self.components = list(components)
    
    # String representations
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __repr__(self):
        return f"Vector{tuple(self.components)}"
    
    # Container methods
    def __len__(self):
        return len(self.components)
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
    
    def __iter__(self):
        return iter(self.components)
    
    def __contains__(self, value):
        return value in self.components
    
    # Arithmetic operators
    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimensions")
            return Vector(*(a + b for a, b in zip(self, other)))
        return Vector(*(x + other for x in self))
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimensions")
            return Vector(*(a - b for a, b in zip(self, other)))
        return Vector(*(x - other for x in self))
    
    def __rsub__(self, other):
        return Vector(*(other - x for x in self))
    
    def __mul__(self, other):
        """Scalar multiplication or dot product"""
        if isinstance(other, Vector):
            # Dot product
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimensions")
            return sum(a * b for a, b in zip(self, other))
        # Scalar multiplication
        return Vector(*(x * other for x in self))
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, scalar):
        return Vector(*(x / scalar for x in self))
    
    def __floordiv__(self, scalar):
        return Vector(*(x // scalar for x in self))
    
    def __mod__(self, scalar):
        return Vector(*(x % scalar for x in self))
    
    def __pow__(self, exponent):
        return Vector(*(x ** exponent for x in self))
    
    # Unary operators
    def __neg__(self):
        return Vector(*(-x for x in self))
    
    def __pos__(self):
        return Vector(*self)
    
    def __abs__(self):
        """Magnitude of vector"""
        return math.sqrt(sum(x**2 for x in self))
    
    # Comparison operators
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Compare by magnitude"""
        return abs(self) < abs(other)
    
    def __le__(self, other):
        return abs(self) <= abs(other)
    
    def __gt__(self, other):
        return abs(self) > abs(other)
    
    def __ge__(self, other):
        return abs(self) >= abs(other)
    
    # In-place operators
    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimensions")
            self.components = [a + b for a, b in zip(self, other)]
        else:
            self.components = [x + other for x in self]
        return self
    
    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have same dimensions")
            self.components = [a - b for a, b in zip(self, other)]
        else:
            self.components = [x - other for x in self]
        return self
    
    def __imul__(self, scalar):
        self.components = [x * scalar for x in self]
        return self
    
    def __itruediv__(self, scalar):
        self.components = [x / scalar for x in self]
        return self
    
    # Boolean context
    def __bool__(self):
        return any(x != 0 for x in self)
    
    # Hashing (for use in sets/dicts)
    def __hash__(self):
        return hash(tuple(self.components))
    
    # Custom methods
    def magnitude(self):
        """Calculate magnitude using __abs__"""
        return abs(self)
    
    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self / mag
    
    def dot(self, other):
        """Dot product (alternative to __mul__)"""
        return self * other
    
    def cross(self, other):
        """Cross product (only for 3D vectors)"""
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        
        x = self[1] * other[2] - self[2] * other[1]
        y = self[2] * other[0] - self[0] * other[2]
        z = self[0] * other[1] - self[1] * other[0]
        
        return Vector(x, y, z)
    
    def angle_with(self, other):
        """Calculate angle between vectors (in radians)"""
        cos_angle = (self * other) / (abs(self) * abs(other))
        return math.acos(max(-1, min(1, cos_angle)))  # Clamp to avoid numerical errors
    
    # Context manager (just for demonstration)
    def __enter__(self):
        print(f"Working with {self}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Done with {self}")
        return False


# Demonstration
if __name__ == "__main__":
    print("=== Basic Operations ===")
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 3: {v1 * 3}")
    print(f"3 * v1: {3 * v1}")
    
    print("\n=== Dot and Cross Product ===")
    print(f"v1 · v2 (dot): {v1.dot(v2)}")
    print(f"v1 × v2 (cross): {v1.cross(v2)}")
    
    print("\n=== Magnitude and Normalization ===")
    print(f"|v1|: {v1.magnitude():.2f}")
    print(f"Normalized v1: {v1.normalize()}")
    print(f"|normalized v1|: {v1.normalize().magnitude():.2f}")
    
    print("\n=== Comparisons ===")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 < v2: {v1 < v2}")  # Compares magnitudes
    
    print("\n=== Indexing and Iteration ===")
    print(f"v1[0]: {v1[0]}")
    print(f"v1[1:]: {v1[1:]}")
    print(f"2 in v1: {2 in v1}")
    
    print("\nIterating over v1:")
    for component in v1:
        print(f"  {component}")
    
    print("\n=== Unary Operators ===")
    print(f"-v1: {-v1}")
    print(f"abs(v1): {abs(v1):.2f}")
    
    print("\n=== In-place Operations ===")
    v3 = Vector(1, 1, 1)
    print(f"v3: {v3}")
    v3 += Vector(2, 2, 2)
    print(f"v3 after += Vector(2,2,2): {v3}")
    v3 *= 2
    print(f"v3 after *= 2: {v3}")
    
    print("\n=== Power and Other Operations ===")
    v4 = Vector(2, 3, 4)
    print(f"v4: {v4}")
    print(f"v4 ** 2: {v4 ** 2}")
    print(f"v4 / 2: {v4 / 2}")
    
    print("\n=== Angle Between Vectors ===")
    v5 = Vector(1, 0, 0)
    v6 = Vector(0, 1, 0)
    angle = v5.angle_with(v6)
    print(f"Angle between {v5} and {v6}: {math.degrees(angle):.2f}°")
    
    print("\n=== Context Manager ===")
    with Vector(7, 8, 9) as v:
        print(f"Inside context: {v}")
    
    print("\n=== Using in Sets/Dicts (hashable) ===")
    vector_set = {Vector(1, 2), Vector(3, 4), Vector(1, 2)}
    print(f"Set of vectors: {vector_set}")
    print(f"Length (duplicates removed): {len(vector_set)}")
```

<br>
<br>
<br>
<br>


# 13. Advanced Design Patterns

### A. Factory Pattern
```py
pythonfrom abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

class AnimalFactory:
    """Factory for creating animals"""
    _creators = {}
    
    @classmethod
    def register(cls, animal_type, creator):
        """Register a new animal type"""
        cls._creators[animal_type] = creator
    
    @classmethod
    def create(cls, animal_type):
        """Create an animal of the specified type"""
        creator = cls._creators.get(animal_type)
        if not creator:
            raise ValueError(f"Unknown animal type: {animal_type}")
        return creator()

# Register animal types
AnimalFactory.register('dog', Dog)
AnimalFactory.register('cat', Cat)
AnimalFactory.register('bird', Bird)

# Create animals using factory

animals = [AnimalFactory.create('dog'), 
           AnimalFactory.create('cat'),
           AnimalFactory.create('bird')]

for animal in animals:
    print(animal.speak())
```

<br>
<br>

### B. Builder Pattern
```py
pythonclass Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []
    
    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, toppings: {', '.join(self.toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_dough(self, dough):
        self.pizza.dough = dough
        return self  # For chaining
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza
 
# Using builder 
pizza = (PizzaBuilder()
         .set_dough("thin crust")
         .set_sauce("tomato")
         .add_topping("mozzarella")
         .add_topping("pepperoni")
         .add_topping("mushrooms")
         .build())

print(pizza)
```
<br>
<br>

### C. Observer Pattern

```py
pythonclass Subject:
    """Observable object"""
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"{self.name} received update: state = {subject.state}")
 
# Using observer pattern
 
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.state = "Active"   # Both observers notified
subject.state = "Inactive" # Both observers notified
```
<br>
<br>

### D. Strategy Pattern

```py
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal account {self.email}"

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        return f"Paid ${amount} using Crypto wallet {self.wallet_address[:8]}..."

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(price for _, price in self.items)
        if not self.payment_strategy:
            return "Please select a payment method"
        return self.payment_strategy.pay(total)

# Using strategy pattern
cart = ShoppingCart()
cart.add_item("Laptop", 1200)
cart.add_item("Mouse", 25)

# Try different payment strategies
cart.set_payment_strategy(CreditCardPayment("1234567890123456", "123"))
print(cart.checkout())

cart.set_payment_strategy(PayPalPayment("user@example.com"))
print(cart.checkout())

cart.set_payment_strategy(CryptoPayment("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"))
print(cart.checkout())
```

<br>
<br>
<br>


# 14. Advanced Inheritance Techniques

### A. Template Method Pattern
```py
pythonclass DataParser(ABC):
    """Template method pattern"""
    
    def parse(self, filepath):
        """Template method - defines the algorithm structure"""
        data = self.read_file(filepath)
        parsed = self.parse_data(data)
        validated = self.validate_data(parsed)
        return self.transform_data(validated)
    
    def read_file(self, filepath):
        """Concrete method"""
        with open(filepath, 'r') as f:
            return f.read()
    
    @abstractmethod
    def parse_data(self, data):
        """Must be implemented by subclass"""
        pass
    
    @abstractmethod
    def validate_data(self, data):
        """Must be implemented by subclass"""
        pass
    
    def transform_data(self, data):
        """Hook method - can be overridden"""
        return data

class CSVParser(DataParser):
    def parse_data(self, data):
        lines = data.strip().split('\n')
        return [line.split(',') for line in lines]
    
    def validate_data(self, data):
        if not data:
            raise ValueError("No data found")
        return data
    
    def transform_data(self, data):
        # Convert to list of dicts
        headers = data[0]
        return [dict(zip(headers, row)) for row in data[1:]]

class JSONParser(DataParser):
    def parse_data(self, data):
        import json
        return json.loads(data)
    
    def validate_data(self, data):
        if not isinstance(data, (list, dict)):
            raise ValueError("Invalid JSON structure")
        return data
```
<br>
<br>

### B. Cooperative Multiple Inheritance
```py
pythonclass LoggerMixin:
    def log(self, message, level="INFO"):
        print(f"[{level}] {self.__class__.__name__}: {message}")

class ValidationMixin:
    def validate(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        return True

class SerializationMixin:
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    def from_dict(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        return self

class User(LoggerMixin, ValidationMixin, SerializationMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def save(self):
        self.validate(self.username)
        self.log(f"Saving user {self.username}")
        # Save logic here
        return self.to_dict()

user = User("alice", "alice@example.com")
user.log("User created")
data = user.save()
print(data)
```

<br>
<br>
<br>
<br>


# 15. Dynamic Class Creation
```py
# Creating classes dynamically with type()
def create_class(class_name, attributes, methods):
    """Factory to create classes dynamically"""
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    # Build class dictionary
    class_dict = {'__init__': __init__}
    class_dict.update(methods)
    
    # Create the class
    return type(class_name, (), class_dict)

# Create a Person class dynamically
methods = {
    'greet': lambda self: f"Hello, I'm {self.name}",
    'age_in_months': lambda self: self.age * 12
}

Person = create_class('Person', ['name', 'age'], methods)

person = Person(name="Alice", age=30)
print(person.greet())  # Hello, I'm Alice
print(person.age_in_months())  # 360

# Advanced: Class factory with metaclass
class AutoPropertyMeta(type):
    """Metaclass that converts all attributes to properties"""
    
    def __new__(cls, name, bases, dct):
        # Find attributes that should be properties
        properties = {}
        
        for key, value in list(dct.items()):
            if not key.startswith('_') and not callable(value):
                # Create property for this attribute
                private_name = f'_{key}'
                
                def make_property(private_name):
                    def getter(self):
                        return getattr(self, private_name, None)
                    
                    def setter(self, value):
                        setattr(self, private_name, value)
                    
                    return property(getter, setter)
                
                properties[key] = make_property(private_name)
        
        dct.update(properties)
        return super().__new__(cls, name, bases, dct)

class Config(metaclass=AutoPropertyMeta):
    debug = False
    timeout = 30
    
    def __init__(self):
        self.debug = False
        self.timeout = 30

config = Config()
config.debug = True  # Uses property setter
print(config.debug)  # Uses property getter
```
<br>
<br>
<br>
<br>


# 16. Advanced Error Handling in OOP
```py
pythonclass ValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class BusinessLogicError(Exception):
    """Custom exception for business logic errors"""
    pass

class Model:
    """Base model with validation"""
    
    def __init_subclass__(cls, **kwargs):
        """Called when a subclass is created"""
        super().__init_subclass__(**kwargs)
        
        # Automatically add validation
        if not hasattr(cls, '_validators'):
            cls._validators = {}
    
    @classmethod
    def add_validator(cls, field, validator):
        """Add a validator for a field"""
        if not hasattr(cls, '_validators'):
            cls._validators = {}
        cls._validators[field] = validator
    
    def validate(self):
        """Validate all fields"""
        errors = []
        
        for field, validator in self._validators.items():
            value = getattr(self, field, None)
            try:
                if not validator(value):
                    errors.append(ValidationError(field, "Validation failed"))
            except Exception as e:
                errors.append(ValidationError(field, str(e)))
        
        if errors:
            raise ExceptionGroup("Validation failed", errors)
        
        return True

class User(Model):
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

# Add validators
User.add_validator('username', lambda x: x and len(x) >= 3)
User.add_validator('email', lambda x: '@' in str(x))
User.add_validator('age', lambda x: isinstance(x, int) and 0 < x < 150)

try:
    user = User("ab", "invalid-email", -5)
    user.validate()
except ExceptionGroup as eg:
    print(f"Validation failed with {len(eg.exceptions)} errors:")
    for error in eg.exceptions:
        print(f"  - {error}")
```
<br>
<br>
<br>
<br>

# 17. Advanced Generators and Iterators in Classes
```py
pythonclass Range:
    """Custom range class with iterator protocol"""
    
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        """Returns an iterator"""
        current = self.start
        while current < self.end:
            yield current
            current += self.step
    
    def __reversed__(self):
        """Reverse iterator"""
        current = self.end - 1
        while current >= self.start:
            yield current
            current -= self.step
    
    def __contains__(self, value):
        """Check if value is in range"""
        if self.step > 0:
            return self.start <= value < self.end and (value - self.start) % self.step == 0
        return False

# Using custom iterator
r = Range(0, 10, 2)
print(list(r))  # [0, 2, 4, 6, 8]
print(list(reversed(r)))  # [9, 7, 5, 3, 1]
print(4 in r)  # True
print(5 in r)  # False

# Generator-based pagination
class Paginator:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
    
    def __iter__(self):
        """Yield pages"""
        for i in range(0, len(self.items), self.page_size):
            yield self.items[i:i + self.page_size]
    
    def __len__(self):
        """Number of pages"""
        return (len(self.items) + self.page_size - 1) // self.page_size

items = list(range(25))
paginator = Paginator(items, page_size=10)

for page_num, page in enumerate(paginator, 1):
    print(f"Page {page_num}: {page}")
```
<br>
<br>
<br>
<br>


# 18. Weak References and Memory Management
```py
pythonimport weakref

class Node:
    """Node with weak reference to avoid circular references"""
    
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
    
    @property
    def parent(self):
        """Return parent or None if weak reference is dead"""
        return self._parent() if self._parent else None
    
    @parent.setter
    def parent(self, node):
        """Store weak reference to parent"""
        self._parent = weakref.ref(node) if node else None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # Uses weak reference
    
    def __repr__(self):
        return f"Node({self.value})"

# Using weak references
root = Node("root")
child1 = Node("child1")
child2 = Node("child2")

root.add_child(child1)
root.add_child(child2)

print(child1.parent)  # Node(root)

# When root is deleted, weak reference doesn't prevent garbage collection
del root
print(child1.parent)  # None (weak reference is dead)

# Observer pattern with weak references
class Observable:
    def __init__(self):
        self._observers = weakref.WeakSet()
    
    def register(self, observer):
        self._observers.add(observer)
    
    def notify(self, *args, **kwargs):
        # Observers automatically removed when garbage collected
        for observer in self._observers:
            observer.update(*args, **kwargs)

class Observer:
    def update(self, *args):
        print(f"Observer {id(self)} received: {args}")

observable = Observable()
observer1 = Observer()
observer2 = Observer()

observable.register(observer1)
observable.register(observer2)

observable.notify("Event!")

del observer1  # Automatically removed from WeakSet
observable.notify("Another event!")  # Only observer2 receives it
```
<br>
<br>
<br>

# 19. Async OOP (Asynchronous Classes)
```py
pythonimport asyncio
from typing import AsyncIterator

class AsyncResource:
    """Async context manager"""
    
    def __init__(self, name):
        self.name = name
        self.is_open = False
    
    async def __aenter__(self):
        """Async enter"""
        print(f"Opening {self.name}")
        await asyncio.sleep(0.1)  # Simulate async operation
        self.is_open = True
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async exit"""
        print(f"Closing {self.name}")
        await asyncio.sleep(0.1)
        self.is_open = False
        return False

class AsyncIterableClass:
    """Async iterator"""
    
    def __init__(self, count):
        self.count = count
    
    def __aiter__(self):
        self.current = 0
        return self
    
    async def __anext__(self):
        if self.current >= self.count:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.1)  # Simulate async operation
        self.current += 1
        return self.current

class AsyncDataFetcher:
    """Async methods in class"""
    
    async def fetch_data(self, url):
        """Simulate async data fetching"""
        await asyncio.sleep(0.5)
        return f"Data from {url}"
    
    async def fetch_multiple(self, urls):
        """Fetch multiple URLs concurrently"""
        tasks = [self.fetch_data(url) for url in urls]
        return await asyncio.gather(*tasks)

# Using async classes
async def main():
    # Async context manager
    async with AsyncResource("Database") as resource:
        print(f"Resource open: {resource.is_open}")
    
    print()
    
    # Async iterator
    async for value in AsyncIterableClass(5):
        print(f"Value: {value}")
    
    print()
    
    # Async methods
    fetcher = AsyncDataFetcher()
    urls = ['url1', 'url2', 'url3']
    results = await fetcher.fetch_multiple(urls)
    for result in results:
        print(result)

# Run async code
# asyncio.run(main())
```
<br>
<br>
<br>
<br


# 20. Complete Advanced Example: Plugin System

```py
"""
Advanced Plugin System demonstrating:
- Metaclasses for automatic registration
- Abstract base classes
- Decorators
- Context managers
- Property descriptors
- Observer pattern
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Callable
import inspect
from functools import wraps
import time


# ============= Plugin Metaclass =============
class PluginMeta(type):
    """Metaclass that automatically registers plugins"""
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        
        # Don't register the base Plugin class itself
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            # Register this plugin
            plugin_name = attrs.get('name', name)
            cls.registry[plugin_name] = cls
            print(f"Registered plugin: {plugin_name}")


# ============= Decorators =============
def measure_time(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def validate_input(validator: Callable):
    """Decorator to validate input"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, data, *args, **kwargs):
            if not validator(data):
                raise ValueError(f"Invalid input for {func.__name__}")
            return func(self, data, *args, **kwargs)
        return wrapper
    return decorator


# ============= Descriptors =============
class ConfigProperty:
    """Descriptor for plugin configuration"""
    
    def __init__(self, default=None, validator=None):
        self.default = default
        self.validator = validator
        self.data = {}
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.data.get(id(obj), self.default)
    
    def __set__(self, obj, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        self.data[id(obj)] = value


# ============= Base Plugin Class =============
class Plugin(ABC, metaclass=PluginMeta):
    """Abstract base class for all plugins"""
    
    name = None  # Plugin name
    version = "1.0.0"
    
    # Configuration properties using descriptors
    enabled = ConfigProperty(default=True, validator=lambda x: isinstance(x, bool))
    priority = ConfigProperty(default=0, validator=lambda x: isinstance(x, int))
    
    def __init__(self, context: 'PluginContext'):
        self.context = context
        self._hooks = {}
        self._initialized = False
    
    @abstractmethod
    def initialize(self):
        """Initialize the plugin"""
        pass
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process data"""
        pass
    
    def register_hook(self, event: str, callback: Callable):
        """Register a hook for an event"""
        if event not in self._hooks:
            self._hooks[event] = []
        self._hooks[event].append(callback)
    
    def trigger_hook(self, event: str, *args, **kwargs):
        """Trigger all hooks for an event"""
        for callback in self._hooks.get(event, []):
            callback(*args, **kwargs)
    
    def __enter__(self):
        """Context manager support"""
        if not self._initialized:
            self.initialize()
            self._initialized = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cleanup when exiting context"""
        self.shutdown()
        return False
    
    def shutdown(self):
        """Cleanup resources"""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(enabled={self.enabled}, priority={self.priority})"


# ============= Plugin Context (Observer Pattern) =============
class PluginContext:
    """Context for plugins with observer pattern"""
    
    def __init__(self):
        self.data = {}
        self._observers = []
    
    def set(self, key: str, value: Any):
        """Set context data and notify observers"""
        self.data[key] = value
        self._notify('data_changed', key, value)
    
    def get(self, key: str, default=None):
        """Get context data"""
        return self.data.get(key, default)
    
    def attach_observer(self, observer):
        """Attach an observer"""
        self._observers.append(observer)
    
    def _notify(self, event: str, *args, **kwargs):
        """Notify all observers"""
        for observer in self._observers:
            if hasattr(observer, 'on_' + event):
                getattr(observer, 'on_' + event)(*args, **kwargs)


# ============= Concrete Plugin Implementations =============
class TextProcessorPlugin(Plugin):
    """Plugin for processing text"""
    
    name = "text_processor"
    version = "1.0.0"
    
    def initialize(self):
        print(f"Initializing {self.name}")
        self.register_hook('before_process', self._log_input)
        self.register_hook('after_process', self._log_output)
    
    def _log_input(self, data):
        print(f"[{self.name}] Input: {data[:50]}...")
    
    def _log_output(self, result):
        print(f"[{self.name}] Output: {result[:50]}...")
    
    @measure_time
    @validate_input(lambda x: isinstance(x, str))
    def process(self, data: str) -> str:
        """Convert text to uppercase"""
        self.trigger_hook('before_process', data)
        result = data.upper()
        self.trigger_hook('after_process', result)
        return result


class DataValidatorPlugin(Plugin):
    """Plugin for validating data"""
    
    name = "data_validator"
    version = "1.0.0"
    
    def initialize(self):
        print(f"Initializing {self.name}")
        self.rules = []
    
    def add_rule(self, rule: Callable[[Any], bool]):
        """Add a validation rule"""
        self.rules.append(rule)
    
    @measure_time
    def process(self, data: Any) -> Dict[str, Any]:
        """Validate data against rules"""
        results = {
            'valid': True,
            'errors': []
        }
        
        for i, rule in enumerate(self.rules):
            try:
                if not rule(data):
                    results['valid'] = False
                    results['errors'].append(f"Rule {i} failed")
            except Exception as e:
                results['valid'] = False
                results['errors'].append(f"Rule {i} error: {str(e)}")
        
        return results


class LoggerPlugin(Plugin):
    """Plugin for logging with observer pattern"""
    
    name = "logger"
    version = "1.0.0"
    
    def initialize(self):
        print(f"Initializing {self.name}")
        self.logs = []
        self.context.attach_observer(self)
    
    def process(self, data: Any) -> Any:
        """Log data"""
        self.log(f"Processing: {data}")
        return data
    
    def log(self, message: str):
        """Add log message"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def on_data_changed(self, key: str, value: Any):
        """Observer callback for context data changes"""
        self.log(f"Context changed: {key} = {value}")
    
    def get_logs(self) -> List[str]:
        """Return all logs"""
        return self.logs.copy()


# ============= Plugin Manager =============
class PluginManager:
    """Manager for loading and executing plugins"""
    
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
        self.context = PluginContext()
    
    def load_plugin(self, plugin_class: type) -> Plugin:
        """Load a plugin"""
        plugin = plugin_class(self.context)
        self.plugins[plugin.name] = plugin
        return plugin
    
    def get_plugin(self, name: str) -> Plugin:
        """Get a loaded plugin"""
        return self.plugins.get(name)
    
    def list_plugins(self) -> List[str]:
        """List all loaded plugins"""
        return list(self.plugins.keys())
    
    def list_available_plugins(self) -> List[str]:
        """List all registered plugin classes"""
        return list(Plugin.registry.keys())
    
    def execute_pipeline(self, data: Any, plugin_names: List[str]) -> Any:
        """Execute a pipeline of plugins"""
        result = data
        
        # Sort plugins by priority
        plugins = [self.plugins[name] for name in plugin_names if name in self.plugins]
        plugins.sort(key=lambda p: p.priority, reverse=True)
        
        for plugin in plugins:
            if plugin.enabled:
                with plugin:  # Use context manager
                    result = plugin.process(result)
            else:
                print(f"Skipping disabled plugin: {plugin.name}")
        
        return result
    
    def __repr__(self):
        return f"PluginManager(loaded={len(self.plugins)}, available={len(Plugin.registry)})"


# ============= Demonstration =============
def main():
    print("=" * 60)
    print("Advanced Plugin System Demo")
    print("=" * 60)
    print()
    
    # Create manager
    manager = PluginManager()
    print(f"\nAvailable plugins: {manager.list_available_plugins()}")
    print()
    
    # Load plugins
    print("Loading plugins...")
    text_processor = manager.load_plugin(TextProcessorPlugin)
    validator = manager.load_plugin(DataValidatorPlugin)
    logger = manager.load_plugin(LoggerPlugin)
    print()
    
    # Configure plugins
    text_processor.priority = 10
    validator.priority = 5
    logger.priority = 1
    
    # Add validation rules
    validator.add_rule(lambda x: len(x) > 5)
    validator.add_rule(lambda x: isinstance(x, str))
    
    # Update context (will trigger logger observer)
    manager.context.set('user', 'admin')
    manager.context.set('session_id', '12345')
    print()
    
    # Execute pipeline
    print("Executing plugin pipeline...")
    print("-" * 60)
    
    input_data = "hello world from plugin system"
    result = manager.execute_pipeline(
        input_data,
        ['logger', 'data_validator', 'text_processor']
    )
    
    print("-" * 60)
    print(f"\nFinal result: {result}")
    print()
    
    # Show validation results
    validation_result = validator.process(input_data)
    print(f"Validation: {validation_result}")
    print()
    
    # Show logs
    print("All logs:")
    for log in logger.get_logs():
        print(f"  {log}")
    print()
    
    # Demonstrate plugin registry
    print(f"\nPlugin Registry:")
    for name, plugin_class in Plugin.registry.items():
        print(f"  - {name}: {plugin_class.__name__} v{plugin_class.version}")
    print()
    
    # Show manager status
    print(manager)


if __name__ == "__main__":
    main()

```
<br>
<br>
<br>
<br>


# 21. Type Hints and Static Type Checking (Advanced)
```py
pythonfrom typing import (
    TypeVar, Generic, Protocol, Union, Optional, 
    Callable, List, Dict, Tuple, Type, overload
)
from dataclasses import dataclass
 

# Type variables for generics
 
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')
 

# Generic classes
 
class Stack(Generic[T]):
    """Generic stack implementation"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None
    
    def __len__(self) -> int:
        return len(self._items)
 

 
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
 

#  Protocol for structural typing
 
class Drawable(Protocol):
    def draw(self) -> str: ...
    def get_area(self) -> float: ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Circle(r={self.radius})"
    
    def get_area(self) -> float:
        return 3.14 * self.radius ** 2

def render_shape(shape: Drawable) -> None:
    """Works with any object implementing Drawable protocol"""
    print(shape.draw())
    print(f"Area: {shape.get_area()}")

circle = Circle(5)
render_shape(circle)  # Type-safe!
 

# Method overloading with @overload
 
class Calculator:
    @overload
    def add(self, x: int, y: int) -> int: ...
    
    @overload
    def add(self, x: float, y: float) -> float: ...
    
    @overload
    def add(self, x: str, y: str) -> str: ...
    
    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        return x + y  # type: ignore

calc = Calculator()
result1: int = calc.add(1, 2)
result2: float = calc.add(1.5, 2.5)
result3: str = calc.add("hello", "world")
```
<br>
<br>
<br>
<br>

# 22. Dataclasses and Attrs (Modern Python)

```py
pythonfrom dataclasses import dataclass, field, asdict, astuple
from typing import List, ClassVar
from datetime import datetime

@dataclass(order=True, frozen=False)
class Product:
    """Modern dataclass with auto-generated methods"""
    
    sort_index: int = field(init=False, repr=False)
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    # Class variable (not an instance field)
    _id_counter: ClassVar[int] = 0
    
    def __post_init__(self):
        """Called after __init__"""
        Product._id_counter += 1
        self.id = Product._id_counter
        # Set sort index based on price
        self.sort_index = int(self.price)
    
    @property
    def total_value(self) -> float:
        """Calculate total value"""
        return self.price * self.quantity
    
    def apply_discount(self, percentage: float) -> None:
        """Apply discount"""
        self.price *= (1 - percentage / 100)
 
# Using dataclass
 
product1 = Product("Laptop", 1200.0, 5, ["electronics", "computer"])
product2 = Product("Mouse", 25.0, 10, ["electronics", "accessory"])

print(product1)
print(f"Total value: ${product1.total_value}")
 
# Auto-generated comparison (because order=True)
 
print(product1 > product2)  # True (compares by sort_index)
 
# Convert to dict and tuple
 
print(asdict(product1))
print(astuple(product1))
 

# Advanced dataclass with validation
 
from dataclasses import dataclass, field

def validate_positive(value: float) -> float:
    if value <= 0:
        raise ValueError("Value must be positive")
    return value

@dataclass
class BankAccount:
    owner: str
    _balance: float = field(default=0.0, repr=False)
    
    def __post_init__(self):
        self._balance = validate_positive(self._balance)
    
    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount: float) -> None:
        amount = validate_positive(amount)
        self._balance += amount
    
    def withdraw(self, amount: float) -> None:
        amount = validate_positive(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount("Alice", 1000.0)
account.deposit(500)
print(f"Balance: ${account.balance}")

```
<br>
<br>
<br>
<br>

# 23. Enum Classes (Advanced)

```py
pythonfrom enum import Enum, IntEnum, Flag, auto, unique

# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
    def describe(self):
        return f"This is {self.name} with value {self.value}"

print(Color.RED.describe())
print(Color.RED == Color.RED)  # True
print(Color.RED is Color.RED)  # True

# IntEnum (can be compared with integers)
class StatusCode(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

print(StatusCode.OK == 200)  # True
print(StatusCode.OK < StatusCode.NOT_FOUND)  # True

# Flag (for bitwise operations)
class Permission(Flag):
    READ = auto()     # 1
    WRITE = auto()    # 2
    EXECUTE = auto()  # 4
    
    # Combinations
    RW = READ | WRITE
    RWX = READ | WRITE | EXECUTE

user_permissions = Permission.READ | Permission.WRITE
print(Permission.READ in user_permissions)  # True
print(Permission.EXECUTE in user_permissions)  # False
 

### Adding methods to enums
 
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
    
    @property
    def surface_gravity(self):
        G = 6.67430e-11
        return G * self.mass / (self.radius ** 2)

print(f"Earth's gravity: {Planet.EARTH.surface_gravity:.2f} m/s²")
 

#  @unique decorator prevents duplicate values
 
@unique
class UniqueColors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # CRIMSON = 1  # Would raise ValueError
```

# 24. Advanced Composition Patterns
```py
pythonfrom typing import Protocol, List

# Component interface
class Component(Protocol):
    def operation(self) -> str: ...

# Leaf components
class Button:
    def __init__(self, text: str):
        self.text = text
    
    def operation(self) -> str:
        return f"Button({self.text})"

class Input:
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
    
    def operation(self) -> str:
        return f"Input({self.placeholder})"

# Composite component
class Container:
    def __init__(self, name: str):
        self.name = name
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"{self.name}[{', '.join(results)}]"

# Building a UI tree
form = Container("Form")
form.add(Input("Enter name"))
form.add(Input("Enter email"))
form.add(Button("Submit"))

panel = Container("Panel")
panel.add(form)
panel.add(Button("Cancel"))

print(panel.operation())
# Panel[Form[Input(Enter name), Input(Enter email), Button(Submit)], Button(Cancel)]
```
<br>
<br>
<br>
<br>


# 25. Dependency Injection Pattern
```py
pythonfrom abc import ABC, abstractmethod
from typing import Protocol

# Abstract interfaces
class IDatabase(Protocol):
    def query(self, sql: str) -> List[dict]: ...

class ICache(Protocol):
    def get(self, key: str) -> Optional[str]: ...
    def set(self, key: str, value: str) -> None: ...

class ILogger(Protocol):
    def log(self, message: str) -> None: ...

# Concrete implementations
class MySQLDatabase:
    def query(self, sql: str) -> List[dict]:
        return [{"result": f"MySQL: {sql}"}]

class RedisCache:
    def __init__(self):
        self._cache = {}
    
    def get(self, key: str) -> Optional[str]:
        return self._cache.get(key)
    
    def set(self, key: str, value: str) -> None:
        self._cache[key] = value

class FileLogger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

# Service using dependency injection
class UserService:
    """Service with injected dependencies"""
    
    def __init__(
        self, 
        database: IDatabase,
        cache: ICache,
        logger: ILogger
    ):
        self.db = database
        self.cache = cache
        self.logger = logger
    
    def get_user(self, user_id: int) -> dict:
        # Try cache first
        cached = self.cache.get(f"user:{user_id}")
        if cached:
            self.logger.log(f"Cache hit for user {user_id}")
            return {"cached": cached}
        
        # Query database
        self.logger.log(f"Querying database for user {user_id}")
        result = self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
        
        # Update cache
        self.cache.set(f"user:{user_id}", str(result))
        
        return result[0] if result else {}

# Using dependency injection
database = MySQLDatabase()
cache = RedisCache()
logger = FileLogger()

# Inject dependencies
user_service = UserService(database, cache, logger)

# Use the service
user = user_service.get_user(1)
user = user_service.get_user(1)  # Second call hits cache

# Easy to test with mocks
class MockDatabase:
    def query(self, sql: str) -> List[dict]:
        return [{"id": 1, "name": "Test User"}]

test_service = UserService(MockDatabase(), cache, logger)
```
<br>
<br>
<br>
<br>

# 26. Advanced Property Patterns with Computed Properties
```py
pythonclass Temperature:
    """Class with dependent computed properties"""
    
    def __init__(self, celsius: float = 0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """Computed property"""
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self) -> float:
        """Computed property"""
        return self.celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value: float) -> None:
        self.celsius = value - 273.15

temp = Temperature(25)
print(f"C: {temp.celsius}, F: {temp.fahrenheit}, K: {temp.kelvin}")

temp.fahrenheit = 100
print(f"C: {temp.celsius:.2f}, F: {temp.fahrenheit}, K: {temp.kelvin:.2f}")

# Cached property with dependency tracking
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
        self._area_cache = None
        self._perimeter_cache = None
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        self._width = value
        # Invalidate caches
        self._area_cache = None
        self._perimeter_cache = None
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float) -> None:
        self._height = value
        self._area_cache = None
        self._perimeter_cache = None
    
    @property
    def area(self) -> float:
        """Cached computed property"""
        if self._area_cache is None:
            print("Computing area...")
            self._area_cache = self.width * self.height
        return self._area_cache
    
    @property
    def perimeter(self) -> float:
        """Cached computed property"""
        if self._perimeter_cache is None:
            print("Computing perimeter...")
            self._perimeter_cache = 2 * (self.width + self.height)
        return self._perimeter_cache

rect = Rectangle(10, 20)
print(rect.area)      # Computes
print(rect.area)      # Uses cache
rect.width = 15       # Invalidates cache
print(rect.area)      # Recomputes
```
<br>
<br>
<br>
<br>


# 27. Advanced Class Decorators

```py
pythonfrom functools import wraps
from typing import Any, Callable, Type

def add_repr(cls: Type) -> Type:
    """Class decorator to add __repr__ method"""
    def __repr__(self):
        attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    
    cls.__repr__ = __repr__
    return cls

def add_equality(cls: Type) -> Type:
    """Class decorator to add __eq__ method"""
    def __eq__(self, other):
        if not isinstance(other, cls):
            return False
        return self.__dict__ == other.__dict__
    
    cls.__eq__ = __eq__
    return cls

def immutable(cls: Type) -> Type:
    """Make class immutable"""
    original_setattr = cls.__setattr__
    original_delattr = cls.__delattr__
    
    def __setattr__(self, name, value):
        if hasattr(self, '_initialized'):
            raise AttributeError(f"Cannot modify immutable object")
        original_setattr(self, name, value)
    
    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete from immutable object")
    
    def __init_wrapper(original_init):
        @wraps(original_init)
        def wrapper(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            object.__setattr__(self, '_initialized', True)
        return wrapper
    
    cls.__setattr__ = __setattr__
    cls.__delattr__ = __delattr__
    cls.__init__ = __init_wrapper(cls.__init__)
    
    return cls
 
# Using class decorators
@add_repr
@add_equality
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(5, 15)

print(p1)  # Point(x=10, y=20)
print(p1 == p2)  # True
print(p1 == p3)  # False

@immutable
class ImmutablePoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

ip = ImmutablePoint(10, 20)
# ip.x = 30  # AttributeError: Cannot modify immutable object
```
<br>
<br>
<br>
<br>


# 28. Real-World Complete Example: Event-Driven System

```py
"""
Complete Event-Driven System demonstrating:
- Event Bus (Mediator Pattern)
- Event Handlers (Observer Pattern)
- Command Pattern
- Dependency Injection
- Async support
- Type hints
- Dataclasses
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Any, Optional, Protocol
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import uuid
from collections import defaultdict


# ============= Event Types =============
class EventType(Enum):
    """Enumeration of event types"""
    USER_CREATED = "user.created"
    USER_UPDATED = "user.updated"
    USER_DELETED = "user.deleted"
    ORDER_PLACED = "order.placed"
    ORDER_SHIPPED = "order.shipped"
    PAYMENT_PROCESSED = "payment.processed"


# ============= Base Event =============
@dataclass(frozen=True)
class Event:
    """Immutable base event class"""
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: EventType = EventType.USER_CREATED
    timestamp: datetime = field(default_factory=datetime.now)
    data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return f"Event({self.event_type.value}, {self.event_id[:8]}...)"


# ============= Specific Events =============
@dataclass(frozen=True)
class UserCreatedEvent(Event):
    """Event for user creation"""
    event_type: EventType = field(default=EventType.USER_CREATED, init=False)
    user_id: int = 0
    username: str = ""
    email: str = ""
    
    def __post_init__(self):
        # Populate data dict
        object.__setattr__(self, 'data', {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email
        })


@dataclass(frozen=True)
class OrderPlacedEvent(Event):
    """Event for order placement"""
    event_type: EventType = field(default=EventType.ORDER_PLACED, init=False)
    order_id: int = 0
    user_id: int = 0
    total_amount: float = 0.0
    items: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        object.__setattr__(self, 'data', {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'total_amount': self.total_amount,
            'items': self.items
        })


# ============= Event Handler Interface =============
class EventHandler(ABC):
    """Abstract base class for event handlers"""
    
    @abstractmethod
    def handle(self, event: Event) -> None:
        """Handle an event"""
        pass
    
    @abstractmethod
    def can_handle(self, event_type: EventType) -> bool:
        """Check if handler can handle this event type"""
        pass
    
    @property
    @abstractmethod
    def priority(self) -> int:
        """Handler priority (higher = executed first)"""
        pass


# ============= Concrete Event Handlers =============
class EmailNotificationHandler(EventHandler):
    """Handler for sending email notifications"""
    
    def __init__(self, email_service: 'EmailService'):
        self.email_service = email_service
        self._priority = 10
    
    def handle(self, event: Event) -> None:
        if isinstance(event, UserCreatedEvent):
            self.email_service.send_welcome_email(
                event.email, 
                event.username
            )
        elif isinstance(event, OrderPlacedEvent):
            self.email_service.send_order_confirmation(
                event.user_id,
                event.order_id,
                event.total_amount
            )
    
    def can_handle(self, event_type: EventType) -> bool:
        return event_type in [
            EventType.USER_CREATED, 
            EventType.ORDER_PLACED
        ]
    
    @property
    def priority(self) -> int:
        return self._priority


class LoggingHandler(EventHandler):
    """Handler for logging events"""
    
    def __init__(self, logger: 'Logger'):
        self.logger = logger
        self._priority = 100  # Highest priority
    
    def handle(self, event: Event) -> None:
        self.logger.log(
            f"Event: {event.event_type.value}",
            event_id=event.event_id,
            data=event.data
        )
    
    def can_handle(self, event_type: EventType) -> bool:
        return True  # Log all events
    
    @property
    def priority(self) -> int:
        return self._priority


class AnalyticsHandler(EventHandler):
    """Handler for tracking analytics"""
    
    def __init__(self):
        self.event_counts = defaultdict(int)
        self._priority = 5
    
    def handle(self, event: Event) -> None:
        self.event_counts[event.event_type.value] += 1
    
    def can_handle(self, event_type: EventType) -> bool:
        return True
    
    @property
    def priority(self) -> int:
        return self._priority
    
    def get_stats(self) -> Dict[str, int]:
        return dict(self.event_counts)


# ============= Event Bus =============
class EventBus:
    """Central event bus for publishing and subscribing to events"""
    
    def __init__(self):
        self._handlers: Dict[EventType, List[EventHandler]] = defaultdict(list)
        self._global_handlers: List[EventHandler] = []
        self._event_history: List[Event] = []
    
    def subscribe(
        self, 
        event_type: EventType, 
        handler: EventHandler
    ) -> None:
        """Subscribe a handler to specific event type"""
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)
            # Sort by priority (descending)
            self._handlers[event_type].sort(
                key=lambda h: h.priority, 
                reverse=True
            )
    
    def subscribe_all(self, handler: EventHandler) -> None:
        """Subscribe handler to all events"""
        if handler not in self._global_handlers:
            self._global_handlers.append(handler)
            self._global_handlers.sort(
                key=lambda h: h.priority,
                reverse=True
            )
    
    def unsubscribe(
        self, 
        event_type: EventType, 
        handler: EventHandler
    ) -> None:
        """Unsubscribe handler from event type"""
        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)
    
    def publish(self, event: Event) -> None:
        """Publish an event to all subscribed handlers"""
        self._event_history.append(event)
        
        # Get handlers for this event type
        handlers = (
            self._global_handlers + 
            self._handlers.get(event.event_type, [])
        )
        
        # Remove duplicates while preserving order
        seen = set()
        unique_handlers = []
        for handler in handlers:
            if id(handler) not in seen:
                seen.add(id(handler))
                unique_handlers.append(handler)
        
        # Execute handlers in priority order
        for handler in unique_handlers:
            if handler.can_handle(event.event_type):
                try:
                    handler.handle(event)
                except Exception as e:
                    print(f"Error in handler {handler.__class__.__name__}: {e}")
    
    def get_history(
        self, 
        event_type: Optional[EventType] = None
    ) -> List[Event]:
        """Get event history"""
        if event_type:
            return [e for e in self._event_history if e.event_type == event_type]
        return self._event_history.copy()
    
    def clear_history(self) -> None:
        """Clear event history"""
        self._event_history.clear()


# ============= Services (Dependencies) =============
class EmailService:
    """Service for sending emails"""
    
    def send_welcome_email(self, email: str, username: str) -> None:
        print(f"📧 Sending welcome email to {email} (User: {username})")
    
    def send_order_confirmation(
        self, 
        user_id: int, 
        order_id: int, 
        amount: float
    ) -> None:
        print(f"📧 Sending order confirmation to user {user_id}")
        print(f"   Order #{order_id} - ${amount:.2f}")


class Logger:
    """Logging service"""
    
    def __init__(self):
        self.logs = []
    
    def log(self, message: str, **kwargs) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        if kwargs:
            log_entry += f" | {kwargs}"
        self.logs.append(log_entry)
        print(f"📝 {log_entry}")
    
    def get_logs(self) -> List[str]:
        return self.logs.copy()


# ============= Application Layer =============
class UserService:
    """Service for user operations"""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.users = {}
        self._next_id = 1
    
    def create_user(self, username: str, email: str) -> int:
        """Create a new user and publish event"""
        user_id = self._next_id
        self._next_id += 1
        
        self.users[user_id] = {
            'id': user_id,
            'username': username,
            'email': email
        }
        
        # Publish event
        event = UserCreatedEvent(
            user_id=user_id,
            username=username,
            email=email
        )
        self.event_bus.publish(event)
        
        return user_id


class OrderService:
    """Service for order operations"""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.orders = {}
        self._next_id = 1
    
    def place_order(
        self, 
        user_id: int, 
        items: List[str], 
        total: float
    ) -> int:
        """Place an order and publish event"""
        order_id = self._next_id
        self._next_id += 1
        
        self.orders[order_id] = {
            'id': order_id,
            'user_id': user_id,
            'items': items,
            'total': total
        }
        
        # Publish event
        event = OrderPlacedEvent(
            order_id=order_id,
            user_id=user_id,
            total_amount=total,
            items=items
        )
        self.event_bus.publish(event)
        
        return order_id


# ============= Demo Application =============
def main():
    print("=" * 70)
    print("Advanced Event-Driven System Demo")
    print("=" * 70)
    print()
    
    # Create event bus
    event_bus = EventBus()
    
    # Create services (dependencies)
    email_service = EmailService()
    logger = Logger()
    
    # Create event handlers
    email_handler = EmailNotificationHandler(email_service)
    logging_handler = LoggingHandler(logger)
    analytics_handler = AnalyticsHandler()
    
    # Subscribe handlers
    event_bus.subscribe(EventType.USER_CREATED, email_handler)
    event_bus.subscribe(EventType.ORDER_PLACED, email_handler)
    event_bus.subscribe_all(logging_handler)  # Log all events
    event_bus.subscribe_all(analytics_handler)  # Track all events
    
    print("✅ Event bus configured with handlers")
    print()
    
    # Create application services
    user_service = UserService(event_bus)
    order_service = OrderService(event_bus)
    
    # Perform operations (which trigger events)
    print("=" * 70)
    print("Creating users...")
    print("-" * 70)
    user1_id = user_service.create_user("alice", "alice@example.com")
    print()
    
    user2_id = user_service.create_user("bob", "bob@example.com")
    print()
    
    print("=" * 70)
    print("Placing orders...")
    print("-" * 70)
    order1_id = order_service.place_order(
        user1_id, 
        ["Laptop", "Mouse"], 
        1250.00
    )
    print()
    
    order2_id = order_service.place_order(
        user2_id,
        ["Keyboard", "Monitor"],
        450.00
    )
    print()
    
    # Show analytics
    print("=" * 70)
    print("Analytics Summary")
    print("-" * 70)
    stats = analytics_handler.get_stats()
    for event_type, count in stats.items():
        print(f"  {event_type}: {count} events")
    print()
    
    # Show event history
    print("=" * 70)
    print("Event History")
    print("-" * 70)
    for event in event_bus.get_history():
        print(f"  {event}")
    print()
    
    # Show logs
    print("=" * 70)
    print("Complete Log History")
    print("-" * 70)
    for log in logger.get_logs():
        print(f"  {log}")


if __name__ == "__main__":
    main()
```