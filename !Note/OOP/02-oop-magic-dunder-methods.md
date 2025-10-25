# Python OOP
- [Class-Level Special Methods (Magic / Dunder Methods)](#class-level-special-methods-magic--dunder-methods)
- [Decorators in Class Methods](#decorators-in-class-methods)


<br>
<br>

#  Class-Level Special Methods (Magic / Dunder Methods)

<h6>

| Category                              | Special Methods (Dunder Methods)                                                                                                                                                                                                                                      | Purpose / Usage                                                                |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Object Construction & Destruction** [go](#object-construction--destruction) | `__new__`, `__init__`, `__del__`  | Object তৈরি, initialize এবং delete করার সময় call হয়  |
| **String Representation** [go](#string-representation)    | `__str__`, `__repr__`, `__format__`, `__bytes__`                                                                                                                                                                                                                      | Object কে human-readable বা developer-readable string/bytes আকারে দেখানোর জন্য |
| **Comparison & Hashing** [Go](#comparison--hashing)  | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__hash__`, `__bool__`                                                                                                                                                                                    | Object তুলনা, hash value, boolean conversion জন্য                              |
| **Arithmetic & Bitwise Operators** [Go](#arithmetic--bitwise-operators)  | Basic: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`<br>Reflected: `__radd__`, `__rsub__`, etc.<br>In-place: `__iadd__`, `__isub__`, etc.<br>Bitwise: `__and__`, `__or__`, `__xor__`, `__invert__`, `__lshift__`, `__rshift__` | Arithmetic, in-place operations, and bitwise operations override করার জন্য     |
| **Matrix & Complex Number Operators** [Go](#matrix--complex-number-operators)  | `__matmul__`, `__rmatmul__`, `__imatmul__`                                                                                                                                                                                                                            | Matrix / complex number operations জন্য, `@` operator ব্যবহার হয়               |
| **Type Conversion** [Go](#type-conversion)  | `__int__`, `__float__`, `__complex__`, `__index__`, `__len__`, `__round__`, `__trunc__`                                                                                                                                                                               | Type conversion, length, rounding, truncation এর জন্য                          |
| **Attribute Access** [Go](#attribute-access) | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`                                                                                                                                                                                            | Attribute access, set, delete, and introspection control করার জন্য             |
| **Container & Iteration Protocols** [Go](#container--iteration-protocols) | `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__next__`, `__reversed__`                                                                                                                                                                   | Container operations ও iteration support করার জন্য                             |
| **Context Management**  [Go](#context-management)  | `__enter__`, `__exit__`                                                                                                                                                                                                                                               | `with` statement support করার জন্য                                             |
| **Callable Objects** [Go](#callable-objects)  | `__call__`                                                                                                                                                                                                                                                            | Object কে callable বানানোর জন্য                                                |
| **Descriptors**  [Go](#descriptors)  | `__get__`, `__set__`, `__delete__` | Attribute access control (validation, lazy evaluation)  |
| **Metaprogramming**    [Go](#metaprogramming)   | `__instancecheck__`, `__subclasscheck__`, `__class_getitem__`, `__mro_entries__`, `__prepare__`   | Metaclass / type control, generic programming এবং MRO customization এর জন্য    |
| **Pickling & Copying**  [Go](#pickling--copying)  | `__reduce__`, `__reduce_ex__`, `__copy__`, `__deepcopy__`  | Object serialization (pickle) এবং copy (shallow/deep) জন্য  |
| **Async & Await**  [Go](#async--await)  | `__await__`, `__aiter__`, `__anext__`, `__aenter__`, `__aexit__`  | Async / await, async iteration, async context management এর জন্য |

  
</h6>





## Object Construction & Destruction
[Home](#class-level-special-methods-magic--dunder-methods) 
`__new__`, `__init__`, `__del__`
**creation → initialization → destruction।**

#### 1. `__new__(cls, ...)` → Object তৈরি করার সময় চলে
- Purpose: Object create (allocate) করে।
- Type: static method (class-level)
- Return করতে হয়: নতুন object (usually super().__new__(cls))

#### 2. `__init__(self, ...)` → Object initialize করার সময় চলে
- Purpose: Object তৈরি হওয়ার পর initialize করে — মান সেট করে।
- Type: instance method
- Return কিছু করে না (None হতে হবে)

#### 3. `__del__(self)` → Object delete হওয়ার সময় চলে
- Purpose: Object destroy বা cleanup করার সময় চালানো হয়।
- Type: instance method
- Auto-called: যখন object garbage collector delete করে।

```py
class User:
    def __new__(cls, *args, **kwargs):
        print("Step 1: __new__() → Object তৈরি হচ্ছে (memory allocate করা হচ্ছে)")
        instance = super().__new__(cls)   # আসল object তৈরি
        return instance                    # instance রিটার্ন করা দরকার

    def __init__(self,name:str,email:str,groups:list,age:int):
        print("Step 2: __init__() → Object initialize হচ্ছে")
        self.name = name
        self.email = email 
        self.groups = groups
        self.age = age

    def __call__(self):  # print(obj())
        return self.age  # output: 20
    
    def __del__(self):                  # del obj
        print( f"{self.name} Deleted!") # Output: AN Mamun Deleted

obj = User('AN Mamun','anmamun0@gmail.com',['Coder','Programer'],20) # RUN: __new__, __init__
print(obj())    # RUN: __call__
del obj         # RUN: __del__
```

```shell
Output:
Step 1: __new__() → Object তৈরি হচ্ছে (memory allocate করা হচ্ছে)
Step 2: __init__() → Object initialize হচ্ছে
20
AN Mamun Deleted!
```
---
<br>
<br>
<br>
<br>


## String Representation
[Home](#class-level-special-methods-magic--dunder-methods) 
`__str__`, `__repr__`, `__format__`, `__bytes__`

#### 1. `__str__(self)` → Object print করলে চলে
Purpose: Object-এর human-readable বা user-friendly string return করে। সাধারণত print(obj) বা str(obj) করলে এটা চলে।
Type: Instance method
Auto-called: যখন print() বা str() ব্যবহার করা হয়।

#### 2. `__repr__(self)` → Object debug করার সময় চলে
Purpose: Object-এর developer/debug representation return করে।
এমনভাবে লিখা হয় যাতে সেটা copy করে object recreate করা যায়।
Type: Instance method

#### 3. `__format__(self, format_spec)` → Object custom format করার সময় চলে
Purpose: format() function বা f-string এর মাধ্যমে custom output style দিতে ব্যবহৃত হয়।
তুমি নিজেই বিভিন্ন format তৈরি করতে পারো (যেমন: short, email ইত্যাদি)।
Type: Instance method
Auto-called: যখন format(obj, "spec") বা f"{obj:spec}" ব্যবহার করা হয়।
 
#### 4. `__bytes__(self)` → Object কে bytes এ convert করার সময় চলে
Purpose: Object-এর binary/bytes representation তৈরি করে।
এটা সাধারণত network transfer, encryption, বা file writing এ দরকার হয়।
Type: Instance method
Auto-called: যখন bytes(obj) ব্যবহার করা হয়।

 
```py
class User: 
    def __init__(self, name: str, email: str, groups: list, age: int): 
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age 

    def __str__(self):
        """Human-readable representation (for print)"""
        return f"👤 User: {self.name}, Email: {self.email}"

    def __repr__(self):
        """Developer-friendly representation (for debugging)"""
        return f"User(name='{self.name}', email='{self.email}', age={self.age})"

    def __format__(self, format_spec):
        """Custom string formatting"""
        if format_spec == "short":
            return f"{self.name} ({self.age}y)"
        elif format_spec == "email":
            return f"{self.name} <{self.email}>"
        else:
            return f"User({self.name}, {self.email}, {self.age})"

    def __bytes__(self):
        """Return bytes representation of the object"""
        return bytes(f"{self.name},{self.email},{self.age}", "utf-8")

# -------------------------------
# Testing all special methods
# -------------------------------
obj = User('AN Mamun', 'anmamun0@gmail.com', ['Coder', 'Programmer'], 20)
 
print(obj)                      # calls __str__
print(repr(obj))                # calls __repr__
print(format(obj, "short"))     # calls __format__
print(format(obj, "email"))     # calls __format__
print(bytes(obj))               # calls __bytes__
 
```

```shell
Output:
👤 User: AN Mamun, Email: anmamun0@gmail.com
User(name='AN Mamun', email='anmamun0@gmail.com', age=20)
AN Mamun (20y)
AN Mamun <anmamun0@gmail.com>
b'AN Mamun,anmamun0@gmail.com,20'
```

---
<br>
<br>
<br>
<br>


## Comparison & Hashing 
[Home](#class-level-special-methods-magic--dunder-methods) → 
`__eq__`  ==  `__ne__` !=  `__lt__` <  `__le__` <=  `__gt__` > `__ge__` >= `__hash__`  hashable`__bool__` truthiness


#### 1.` __eq__(self, other)` → Equal (==)
- Purpose: দুইটা object সমান কি না তা নির্ধারণ করে।
- Type: instance method
- Auto-called: যখন obj1 == obj2 লেখা হয়।
 
#### 2. `__ne__(self, other)` → Not Equal (!=)
- Purpose: দুইটা object সমান নয় কি না তা বলে।
- Auto-called: যখন obj1 != obj2 লেখা হয়।
 
#### 3. `__lt__(self, other)` → Less Than (<)
- Purpose: object1 কি object2 এর থেকে ছোট কিনা।
- Auto-called: যখন < ব্যবহার করা হয়।
 
#### 4. `__le__(self, other)` → Less Than or Equal (<=)
- Purpose: ছোট বা সমান কিনা তা বলে।
- Auto-called: যখন <= ব্যবহার করা হয়।

#### 5. `__gt__(self, other)` → Greater Than (>)
- Purpose: object1 কি object2 এর থেকে বড় কিনা।
- Auto-called: যখন > ব্যবহার করা হয়।
 
#### 6. `__ge__(self, other)` → Greater Than or Equal (>=)
- Purpose: বড় বা সমান কিনা তা বলে।
- Auto-called: যখন >= ব্যবহার করা হয়।

#### 7. `__hash__(self)` → Object hash value (for dict/set)
- Purpose: Object কে hashable বানায় যাতে dictionary বা set এ key হিসেবে ব্যবহার করা যায়।
- Auto-called: যখন object কে hash() function দিয়ে বা dict/set key হিসেবে ব্যবহার করা হয়।

#### 8. `__bool__(self)` → Truth value (True or False)
- Purpose: Object কে truthy বা falsy বানায়।
- Auto-called: যখন object কে if, while, বা bool() এ ব্যবহার করা হয়।
 
```py
class User: 
    def __init__(self, name: str, email: str, groups: list, age: int): 
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age  
    # -------------------------------
    # Comparison Methods
    # -------------------------------
    def __eq__(self, other):
        """==  → Checks equality (by email)"""
        if isinstance(other, User):
            return self.email == other.email
        return NotImplemented

    def __ne__(self, other):
        """!=  → Checks inequality"""
        if isinstance(other, User):
            return self.email != other.email
        return NotImplemented

    def __lt__(self, other):
        """<  → Compare by age"""
        if isinstance(other, User):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):
        """<=  → Compare by age"""
        if isinstance(other, User):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):
        """>  → Compare by age"""
        if isinstance(other, User):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):
        """>=  → Compare by age"""
        if isinstance(other, User):
            return self.age >= other.age
        return NotImplemented
    # -------------------------------
    # Hash & Boolean Methods
    # -------------------------------
    def __hash__(self):
        # unique hash তৈরি করার জন্য email ব্যবহার করা হলো
        return hash(self.email)
    
    # def __hash__(self):
    #     """Allow using object as dictionary key or in set"""
    #     return hash((self.email, self.age))

    def __bool__(self):
        """Truthy or Falsy → True if user has name & email"""
        return bool(self.name and self.email)
 
# -------------------------------
# Testing all special methods
# -------------------------------
obj1 = User('AN Mamun', 'anmamun0@gmail.com', ['Coder'], 20)
obj2 = User('John Doe', 'john@example.com', ['Developer'], 25)
obj3 = User('AN Mamun', 'anmamun0@gmail.com', ['Programmer'], 20)
 
print(" Comparison Methods:")
print(obj1 == obj3)  # True (same email)
print(obj1 != obj2)  # True (different email)
print(obj1 < obj2)   # True (20 < 25)
print(obj2 > obj1)   # True
print(obj1 <= obj3)  # True (20 <= 20)
print(obj1 >= obj2)  # False (20 >= 25 → False)

print("Hash:")
# Use in set (hashable object)
users = {obj1, obj2, obj3}
print(len(users))  # Output: 2 → (obj1 & obj3 same hash)

print("Boolean:")
print(bool(obj1))      # True (has name & email)
print(bool(User('', '', [], 0)))  # False

```

```ahell
Output:
 Comparison Methods:
True
True
True
True
True
False
Hash:
2
Boolean:
True
False

```


---
<br>
<br>
<br>
<br>


## Arithmetic & Bitwise Operators
[Home](#class-level-special-methods-magic--dunder-methods)

Arithmetic + Reflected + In-place + Bitwise special methods
- Basic: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
- Reflected: `__radd__`, `__rsub__`, etc.
- In-place: `__iadd__`, `__isub__`, etc.
- Bitwise: `__and__`, `__or__`, `__xor__`, `__invert__`, `__lshift__`, `__rshift__`

```py
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # -------------------------------
    # Basic Arithmetic
    # -------------------------------
    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __truediv__(self, other):
        return self.age / other.age

    def __floordiv__(self, other):
        return self.age // other.age

    def __mod__(self, other):
        return self.age % other.age

    def __pow__(self, other):
        return self.age ** other.age

    # -------------------------------
    # Reflected
    # -------------------------------
    def __radd__(self, other):
        return other + self.age  # other assumed int

    def __rsub__(self, other):
        return other - self.age

    def __rmul__(self, other):
        return other * self.age

    def __rtruediv__(self, other):
        return other / self.age
    
    # -------------------------------
    # In-place
    # -------------------------------
    def __iadd__(self, other):
        self.age += other.age
        return self

    def __isub__(self, other):
        self.age -= other.age
        return self

    def __imul__(self, other):
        self.age *= other.age
        return self
    
    # -------------------------------
    # Bitwise
    # -------------------------------
    def __and__(self, other):
        return self.age & other.age

    def __or__(self, other):
        return self.age | other.age

    def __xor__(self, other):
        return self.age ^ other.age

    def __invert__(self):
        return ~self.age

    def __lshift__(self, other):
        return self.age << other.age

    def __rshift__(self, other):
        return self.age >> other.age
 
# -------------------------------
# Testing all operators
# -------------------------------
u1 = User("Mamun", "anmamun0@gmail.com", 20)
u2 = User("John", "john@example.com", 25)

# Basic Arithmetic
print(u1 + u2)        # 45 ( __add__)
print(u1 - u2)        # -5 (__sub__)
print(u1 * u2)        # 500 (__mul__)
print(u1 / u2)        # 0.8 (__truediv__)
print(u1 // u2)       # 0 (__floordiv__)
print(u1 % u2)        # 20 (__mod__)
print(u1 ** User("X", "x@gmail.com", 2))  # 400  (20 ** 2)  (__pow__)

# Reflected
print(10 + u1)        # 30 (__radd__)
print(50 - u1)        # 30 (__rsub__)
print(2 * u1)         # 40 (__rmul__)
print(100 / u1)       # 5.0 (__rtruediv__)

# In-place
u1 += u2
print(u1.age)         # 45 (__iadd__)
u1 -= u2
print(u1.age)         # 20 (__isub__)
u1 *= u2
print(u1.age)         # 500 (__imul__)

# Bitwise
print(u1 & u2)        # 500 & 25 = 20 (__and__)
print(u1 | u2)        # 500 | 25 = 505  (__or__)
print(u1 ^ u2)        # 500 ^ 25 = 485 (__xor__)
print(~u1)            # ~500 = -501 ( __invert__)
print(u1 << User("X", "x@gmail.com", 2))  # 500 << 2 = 2000 (__lshift__)
print(u1 >> User("X", "x@gmail.com", 3))  # 500 >> 3 = 62 (__rshift__)

```

```shell
5.0
45
20
500
16
509
493
-501
2000
62

```

---

<br>
<br>
<br>
<br>
 


## Matrix & Complex Number Operators
[Home](#class-level-special-methods-magic--dunder-methods)

There are matrix & complex number operators (`__matmul__`,` __rmatmul__`, `__imatmul__`) → @ operator.

1. `__matmul__(self, other)` → Normal matrix multiplication
- Purpose: self @ other operator handle করে।
- Behavior: নতুন value return করে (in-place নয়)।
- Use case: dot product বা matrix multiplication।

2. `__rmatmul__(self, other)` → Reflected matrix multiplication
- Purpose: right-hand operand @ support করার জন্য।
- Behavior: যদি left @ right হয় এবং left object এ __matmul__ method না থাকে, Python right.__rmatmul__(left) call করে।
- Use case: অন্য type (যেমন list) কে User সাথে multiply করতে চাইলে।

3. `__imatmul__(self, other)` → In-place matrix multiplication
- Purpose: self @= other operator handle করে।
- Behavior: self object modify হয় inplace, কোন নতুন object create হয় না।
- Use case: element-wise multiplication / dot product result inplace save করতে।


```py
class User:
    def __init__(self, name, email, age_vector):
        self.name = name
        self.email = email
        self.age_vector = age_vector  # list of integers representing "age related data"

    # -------------------------------
    # Matrix multiplication operator
    # -------------------------------
    def __matmul__(self, other):
        """User1 @ User2 → dot product of age_vector"""
        return sum(a * b for a, b in zip(self.age_vector, other.age_vector))

    def __rmatmul__(self, other):
        """other @ User → support int list @ User"""
        return sum(a * b for a, b in zip(other, self.age_vector))

    def __imatmul__(self, other):
        """User1 @= User2 → element-wise multiplication in place"""
        self.age_vector = [a * b for a, b in zip(self.age_vector, other.age_vector)]
        return self


# -------------------------------
# Testing
# -------------------------------
u1 = User("Mamun", "anmamun0@gmail.com", [1, 2, 3])
u2 = User("John", "john@example.com", [4, 5, 6])

# Normal matrix multiplication (__matmul__)
print(u1 @ u2)   # 1*4 + 2*5 + 3*6 = 32  → dot product

# Reflected (__rmatmul__)
print([1, 1, 1] @ u1)  # 1*1 + 1*2 + 1*3 = 6  → right-hand list @ User

# In-place (__imatmul__)
u1 @= u2
print(u1.age_vector)  # [1*4, 2*5, 3*6] = [4, 10, 18]  → in-place matrix multiplication

```
```shell
Output: 
32
6
[4, 10, 18]
```
---

<br>
<br>
<br>
<br>
<br>



## Type Conversion
[Home](#class-level-special-methods-magic--dunder-methods)

`__int__`, `__float__`, `__complex__`, `__index__`, `__len__`, `__round__`, `__trunc__`

```py
import math

class User:  
    def __init__(self, name:str, email:str, groups:list, age:int):
        print("Step 2: __init__() → Object initialize হচ্ছে")
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age
        self.age_list = [age, age+5, age+10] 
    # -------------------------------
    # Type Conversion
    # -------------------------------
    def __int__(self):
        return self.age  # int(obj)

    def __float__(self):
        return float(self.age)  # float(obj)

    def __complex__(self):
        return complex(self.age, 5)  # complex(obj) → imaginary part 5

    def __index__(self):
        return self.age  # slicing, hex(), bin()

    def __len__(self):
        return len(self.age_list)  # len(obj)

    def __round__(self, n=0):
        return round(self.age / 3, n)  # round(obj, n)

    def __trunc__(self):
        return math.trunc(self.age / 3)  # math.trunc(obj)


# -------------------------------
# Testing
# -------------------------------
obj = User('AN Mamun', 'anmamun0@gmail.com', ['Coder','Programer'], 20)
 
# Type conversions
print(int(obj))       # 20 → __int__
print(float(obj))     # 20.0 → __float__
print(complex(obj))   # (20+5j) → __complex__

# Index (for slicing / bin / hex)
print(bin(obj))       # 0b10100 → __index__ (20 in binary)
print(hex(obj))       # 0x14 → __index__ (20 in hex)

# Length
print(len(obj))       # 3 → __len__ (age_list has 3 elements)

# Rounding / truncation
print(round(obj))     # 7 → __round__ (20/3 ≈ 6.666 → 7)
print(math.trunc(obj))# 6 → __trunc__ (20/3 truncated)
```
 
```shell
Step 2: __init__() → Object initialize হচ্ছে
20
20.0
(20+5j)
0b10100
0x14
3
7.0
6
```

---
<br>
<br>
<br>
<br>
<br>

## Attribute Access
[Home](#class-level-special-methods-magic--dunder-methods)

`__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`
- `__getattr__`	obj.attr	attribute নেই হলে call হয়
- `__getattribute__`	obj.attr	সব attribute access এর আগে call হয়
- `__setattr__`	obj.attr = value	attribute set করার সময় call হয়
- `__delattr__`	del obj.attr	attribute delete করার সময় call হয়
- `__dir__`	dir(obj)	attribute list চাইলে call হয়

```py
class User:
    def __init__(self,name:str,email:str,groups:list,age:int):
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age
    # -------------------------------
    # Attribute Access
    # -------------------------------
    def __getattr__(self, attr):
        # যখন attribute object এ নেই
        print(f"→ '{attr}' attribute নেই, default return করলাম None")
        return None

    def __getattribute__(self, attr):
        # সব attribute access এর আগে call হয়
        print(f"→ Accessing '{attr}'")
        return super().__getattribute__(attr)

    # যখন attribute object এ set করা হলে call হয়
    def __setattr__(self, attr, value):
        print(f"__setattr__ called → Setting '{attr}' = {value}")
        super().__setattr__(attr, value)

    # যখন attribute object থেকে delete করা করার পর call হবে
    def __delattr__(self, attr):
        print(f"__delattr__ called → Deleting '{attr}'")
        super().__delattr__(attr)
        
    # attribute list চাইলে call হয়
    def __dir__(self):
        print(f"__dir__ called → Listing attributes")
        return super().__dir__()
# -------------------------------
# Testing
# -------------------------------
print("--------#created obj and  setted attibute ")
obj = User('AN Mamun','anmamun0@gmail.com',['Coder','Programer'],20)

print("------# Attribute access--------")
print(obj.name)      # __getattribute__ call
print(obj.username)  # __getattribute__ + __getattr__ call (attribute নেই)

print("#---------------------# Set attribute-----------------")
obj.age = 25         # __setattr__ call

print("---------# Delete attribute ----------------")
del obj.email        # __delattr__ call

print("-------------## dir()--------------")
print(dir(obj))      # __dir__ call
 
```
 
```shell
--------#created obj and  setted attibute---------------------------
__setattr__ called → Setting 'name' = AN Mamun
__setattr__ called → Setting 'email' = anmamun0@gmail.com
__setattr__ called → Setting 'groups' = ['Coder', 'Programer']
__setattr__ called → Setting 'age' = 20
---------------------------# Attribute access-----------------------------
→ Accessing 'name'
AN Mamun
→ Accessing 'username'
→ 'username' attribute নেই, default return করলাম None
None
#---------- ---# Set attribute--------------------------------------
__setattr__ called → Setting 'age' = 25

---------# Delete attribute -------------------------------------
__delattr__ called → Deleting 'email'

-------------## dir()-----------------------------------
__dir__ called → Listing attributes
→ Accessing '__dict__'
→ Accessing '__class__'
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'groups', 'name']
 
```

---
<br>
<br>
<br>
<br>
<br>



## Container & Iteration Protocols
[Home](#class-level-special-methods-magic--dunder-methods) → 
`__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__next__`, `__reversed__`

**Container Methods**
- `__getitem__(self, key)` → obj[key] access করার জন্য।
- `__setitem__(self, key, value)` → obj[key] = value assign করার জন্য।
- `__delitem__(self, key)` → del obj[key] delete করার জন্য।
- `__contains__(self, item)` → item in obj check করার জন্য।

**Iteration Methods**
- `__iter__(self)` → iteration শুরু করার জন্য।
- `__next__(self)` → iterator থেকে next element দেওয়ার জন্য।
- `__reversed__(self)` → reversed(obj) call হলে reverse iteration।

 
```py
class User:
    def __init__(self, name:str, email:str, groups:list, age:int):
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age
        self._index = 0  # iteration জন্য

    # -------------------------------
    # Container Methods
    # -------------------------------
    def __getitem__(self, key):
        print(f"__getitem__ called → Accessing '{key}'")
        if key == 'name':
            return self.name 
        else:
             print(f"{key} attr নেই")

    def __setitem__(self, key, value):
        print(f"__setitem__ called → Setting '{key}' = {value}")
        if key == 'name':
            self.name = value
        elif key == 'email':
            self.email = value 
        else:
            print(f"{key} attr নেই")

    def __delitem__(self, key):
        print(f"__delitem__ called → Deleting '{key}'")
        if key == 'name':
            del self.name 
        else:
            print(f"{key} attr নেই")

    def __contains__(self, item):
        print(f"__contains__ called → Checking if '{item}' in User")
        return item in self.groups

    # -------------------------------
    # Iteration Methods
    # -------------------------------
    def __iter__(self):
        print("__iter__ called → Iteration start")
        self._index = 0
        return self

    def __next__(self):
        print("__next__ called")
        if self._index < len(self.groups):
            result = self.groups[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __reversed__(self):
        print("__reversed__ called")
        return reversed(self.groups)

# -------------------------------
# Testing
# -------------------------------
obj = User('AN Mamun', 'anmamun0@gmail.com', ['Coder','Programer','Designer'], 20)

# Container
print(obj['name'])      # __getitem__
print(obj['password'])      # __getitem__

obj['age'] = 25         # __setitem__
del obj['email']        # __delitem__

print('Programer' in obj)  # __contains__

# Iteration
for group in obj:        # __iter__ + __next__
    print(group)

# Reversed
for group in reversed(obj):  # __reversed__
    print(group)
 
```

```shell
Output:
$ python special_methods.py 
__getitem__ called → Accessing 'name'
AN Mamun
__getitem__ called → Accessing 'password'
password attr নেই
None
__setitem__ called → Setting 'age' = 25
age attr নেই
__delitem__ called → Deleting 'email'
email attr নেই
__contains__ called → Checking if 'Programer' in User
True
__iter__ called → Iteration start
__next__ called
Coder
__next__ called
Programer
__next__ called
Designer
__next__ called
__reversed__ called
Designer
Programer
Coder
```

---
<br>
<br>
<br>
<br>
<br>





## Context Management
[Home](#class-level-special-methods-magic--dunder-methods) → 
`__enter__`, `__exit__`

1. `__enter__(self)` → with block শুরু হওয়ার সময় call হয়।
- Return value: যেটা as statement এ assign হবে।

2. `__exit__(self, exc_type, exc_val, exc_tb)` → with block শেষ হওয়ার সময় call হয়।
- Parameters: exception handling এর জন্য।
- Return value: True দিলে exception suppress হবে, False বা None দিলে exception propagate হবে।

```py
class User:
    def __init__(self, name:str, email:str, groups:list, age:int):
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age
    # -------------------------------
    # Context Management
    # -------------------------------
    def __enter__(self):
        print(f"__enter__ called → Entering context for {self.name}")
        # সাধারণত resource open / init করা হয় এখানে
        return self  # `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"__exit__ called → Exiting context for {self.name}")
        # resource cleanup
        if exc_type:
            print(f"Exception: {exc_type}, {exc_val}")
        return False  # exception propagate হবে
    

with User('AN Mamun','anmamun0@gmail.com',['Coder','Programer'],20) as obj:
    print(f"Inside with block: {obj.name}")
    # raise ValueError("Test Exception")  # Uncomment করলে exception handle হবে
```

```shell
Output:
__enter__ called → Entering context for AN Mamun
Inside with block: AN Mamun
__exit__ called → Exiting context for AN Mamun
```

---
<br>
<br>
<br>
<br>
<br>

## Callable Objects
[Home](#class-level-special-methods-magic--dunder-methods)

`__call__`
- Purpose: Object কে callable বানায়, যেমন function।
- Usage: obj() → internally obj.__call__() call হয়।
- Return value: তুমি যেটা return করবে তা obj() call করলে পাওয়া যাবে।

```py
class User:
    def __init__(self, name:str, email:str, groups:list, age:int):
        self.name = name
        self.email = email
        self.groups = groups
        self.age = age
        
    def __call__(self):
        print(f"__call__ called → {self.name} এর age হলো {self.age}")
        return self.age
    
obj = User('AN Mamun', 'anmamun0@gmail.com', ['Coder','Programer'], 20)

age = obj()   # __call__ automatically run হবে
print(f"Returned age: {age}")
 
```

```shell
Output:
__call__ called → AN Mamun এর age হলো 20
Returned age: 20
```

---
<br>
<br>
<br>
<br>
<br>



## Descriptors
[Home](#class-level-special-methods-magic--dunder-methods) → 
`__get__`, `__set__`, `__delete__`

```py
# Descriptor class
class AgeDescriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called → Getting age for {instance.name}")
        return instance._age

    def __set__(self, instance, value):
        print(f"__set__ called → Setting age = {value} for {instance.name}")
        if value < 0:
            raise ValueError("Age cannot be negative")
        instance._age = value

    def __delete__(self, instance):
        print(f"__delete__ called → Deleting age for {instance.name}")
        del instance._age

# User class
class User:
    age = AgeDescriptor()  # descriptor attribute

    def __init__(self, name:str, email:str, groups:list, age:int):
        self.name = name
        self.email = email
        self.groups = groups
        self._age = age  # descriptor internally access this

obj = User('AN Mamun', 'anmamun0@gmail.com', ['Coder','Programer'], 20)

# Access age
print(obj.age)       # __get__   output: # initial age

# Set age
obj.age = 25         # __set__ call
print(obj.age)       # updated age

# Delete age
del obj.age          # __delete__ Output: Deleting age for AN Mamun

```

```shell
__get__ called → Getting age for AN Mamun
20
__set__ called → Setting age = 25 for AN Mamun
__get__ called → Getting age for AN Mamun     
25
__delete__ called → Deleting age for AN Mamun 
```

---

<br>
<br>
<br>
<br>
<br>

 
 

## Metaprogramming
[Home](#class-level-special-methods-magic--dunder-methods) → 
`__instancecheck__`, `__subclasscheck__`, `__class_getitem__`, `__mro_entries__`, `__prepare__`


#### 1. `__instancecheck__(self, instance)`
- Purpose: isinstance(obj, cls) call হলে trigger হয়।
- Custom logic দিয়ে override করা যায়।

#### 2. `__subclasscheck__(self, subclass)`
- Purpose: issubclass(sub, cls) call হলে trigger হয়।
- Custom logic দিয়ে override করা যায়।

#### 3. `__class_getitem__(cls, key)`
- Purpose: Generic type support → Class[key] এর জন্য।

#### 4. `__mro_entries__(cls, bases)`
- Purpose: Class inheritance change করার সময় MRO (Method Resolution Order) adjust করার জন্য।

#### 5. `__prepare__(name, bases, **kwds)`
- Purpose: Metaclass এর জন্য dict বা mapping prepare করার জন্য।
- Class creation এর সময় call হয়।

```py
# -------------------------------
# 1 & 2: isinstance / issubclass
# -------------------------------
class MyMeta(type):
    def __instancecheck__(self, instance):
        print(f"__instancecheck__ called → Checking instance of {instance}")
        return hasattr(instance, 'name')

    def __subclasscheck__(self, subclass):
        print(f"__subclasscheck__ called → Checking subclass {subclass}")
        return hasattr(subclass, 'dummy_attr')

class User(metaclass=MyMeta):
    dummy_attr = True
    def __init__(self, name):
        self.name = name

u = User('AN Mamun')

print(isinstance(u, User))   # __instancecheck__ call
print(issubclass(User, User)) # __subclasscheck__ call

# -------------------------------
# 3: __class_getitem__
# -------------------------------
class MyGeneric:
    def __class_getitem__(cls, key):
        print(f"__class_getitem__ called → {cls} with key={key}")
        return f"Generic[{key}]"

print(MyGeneric[int])  # __class_getitem__ call

# -------------------------------
# 4: __mro_entries__
# -------------------------------
class Base:
    pass

class Proxy:
    def __mro_entries__(self, bases):
        print(f"__mro_entries__ called → {bases}")
        return (Base,)  # replace with Base in MRO

class MyClass(Proxy, object):
    pass

print(MyClass.__mro__)  # check MRO

# -------------------------------
# 5: __prepare__
# -------------------------------
class MyMeta2(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f"__prepare__ called → Preparing dict for {name}")
        return {'prepared': True}

class Test(metaclass=MyMeta2):
    pass

print(Test.__dict__)
 
```

```shell
Output:
__instancecheck__ called → Checking instance of <__main__.User object at 0x...>
True                     # hasattr(instance, 'name') → True
__subclasscheck__ called → Checking subclass <class '__main__.User'>
True                     # hasattr(User, 'dummy_attr') → True
__class_getitem__ called → <class '__main__.MyGeneric'> with key=<class 'int'>
Generic[<class 'int'>]
__mro_entries__ called → (<class 'object'>,)
(<class '__main__.MyClass'>, <class '__main__.Base'>, <class 'object'>)
__prepare__ called → Preparing dict for Test
{'__module__': '__main__', '__qualname__': 'Test', 'prepared': True}

```

---

<br>
<br>
<br>
<br>
<br>








## Pickling & Copying
[Home](#class-level-special-methods-magic--dunder-methods)
`__reduce__`, `__reduce_ex__`, `__copy__`, `__deepcopy__`

1. `__reduce__(self)`
- Purpose: Object কে pickle করার সময় call হয়।
- Return: (callable, args) → pickle কে object reconstruct করতে সাহায্য করে।

2. `__reduce_ex__(self, protocol)`
- Purpose: __reduce__ এর extended version, specific pickle protocol handle করতে।
- Python internally pickle.dump() call করলে trigger হয়।

3. `__copy__(self)`
- Purpose: shallow copy (copy.copy(obj)) তৈরি করার সময় call হয়।

4. `__deepcopy__(self, memo)`
- Purpose: deep copy (copy.deepcopy(obj)) তৈরি করার সময় call হয়।
- memo dictionary circular references handle করতে ব্যবহৃত হয়।

```py
import copy
import pickle

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # -------------------------------
    # Pickling
    # -------------------------------
    def __reduce__(self):
        print("__reduce__ called")
        return (self.__class__, (self.name, self.email, self.age))

    def __reduce_ex__(self, protocol):
        print(f"__reduce_ex__ called with protocol={protocol}")
        return self.__reduce__()

    # -------------------------------
    # Copying
    # -------------------------------
    def __copy__(self):
        print("__copy__ called → shallow copy")
        return User(self.name, self.email, self.age)

    def __deepcopy__(self, memo):
        print("__deepcopy__ called → deep copy")
        return User(copy.deepcopy(self.name, memo),
                    copy.deepcopy(self.email, memo),
                    copy.deepcopy(self.age, memo))
u = User("AN Mamun", "anmamun0@gmail.com", 20)

# Shallow copy
u_copy = copy.copy(u)

# Deep copy
u_deepcopy = copy.deepcopy(u)

# Pickle & Unpickle
data = pickle.dumps(u)       # triggers __reduce_ex__ or __reduce__
u_unpickle = pickle.loads(data)
 
```

```shell
Output:
__copy__ called → shallow copy
__deepcopy__ called → deep copy
__reduce_ex__ called with protocol=5
__reduce__ called

```

Explanation:
- `copy.copy(obj)` → shallow copy, নতুন object but references same nested objects।
- `copy.deepcopy(obj)` → deep copy, nested objects পর্যন্ত copy হয়।
- `pickle.dumps(obj)` → object কে byte stream এ convert করে।

---

<br>
<br>
<br>
<br>
<br>



## Async & Await 
[Home](#class-level-special-methods-magic--dunder-methods) →  
`__await__`, `__aiter__`, `__anext__`, `__aenter__`, `__aexit__`

1. `__await__(self)`
- Purpose: Object কে awaitable বানায়।
Return: iterator (যা await চালাবে)।
- Usage: result = await obj

2. `__aiter__(self)`
- Purpose: Async iteration শুরু করার জন্য।
- Usage: async for x in obj → __aiter__ call হবে।
- Must return an async iterator object (i.e., object with __anext__)

3. `__anext__(self)`
- Purpose: Async iterator থেকে next value return করে।
- Must return an awaitable object।
- Raise StopAsyncIteration to end iteration.

4. `__aenter__(self)`
- Purpose: Async context manager start (async with) হলে call হয়।
- Must return awaitable → async with obj as x:

5. `__aexit__(self, exc_type, exc_val, exc_tb)`
- Purpose: Async context manager end হলে call হয়।
- Must return awaitable, exception handling optional

```py
import asyncio

class AsyncUser:
    def __init__(self, name):
        self.name = name
        self._groups = ["Coder", "Programer"]
        self._index = 0

    # -------------------------------
    # Async await
    # -------------------------------
    def __await__(self):
        print("__await__ called")
        yield from self._fake_await().__await__()
        return f"Welcome {self.name}"

    async def _fake_await(self):
        await asyncio.sleep(0.1)

    # -------------------------------
    # Async iteration
    # -------------------------------
    def __aiter__(self):
        print("__aiter__ called")
        self._index = 0
        return self

    async def __anext__(self):
        if self._index < len(self._groups):
            val = self._groups[self._index]
            self._index += 1
            await asyncio.sleep(0.1)
            return val
        else:
            raise StopAsyncIteration

    # -------------------------------
    # Async context management
    # -------------------------------
    async def __aenter__(self):
        print("__aenter__ called → Entering async context")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("__aexit__ called → Exiting async context")
        await asyncio.sleep(0.1)


async def main():
    # __await__
    user = AsyncUser("AN Mamun")
    msg = await user
    print(msg)

    # Async iteration
    async for g in user:
        print(f"Group: {g}")

    # Async context manager
    async with user as u:
        print(f"Inside async with: {u.name}")

asyncio.run(main())
 
```
```shell
Output:
__await__ called
Welcome AN Mamun          # await result
__aiter__ called
Group: Coder
Group: Programer
__aenter__ called → Entering async context
Inside async with: AN Mamun
__aexit__ called → Exiting async context

```

<h6>
  

| Method       | Usage                  | Call Condition        |
| ------------ | ---------------------- | --------------------- |
| `__await__`  | `await obj`            | object awaitable করতে |
| `__aiter__`  | `async for x in obj`   | async iteration start |
| `__anext__`  | async iterator         | async next element    |
| `__aenter__` | `async with obj as x:` | async context start   |
| `__aexit__`  | `async with` end       | async context cleanup |

</h6>


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



# Decorators in Class Methods
[Home](#class-level-special-methods-magic--dunder-methods) 

Decorator হলো একটি function বা class, যা অন্য function বা method কে modify বা enhance করতে পারে বিনা তার মূল code পরিবর্তন করে।
অর্থাৎ, decorator দিয়ে আমরা function/method/attribute-এর behavior পরিবর্তন করতে পারি, wrap করতে পারি বা extra functionality যোগ করতে পারি।


<h6>
  
| Decorator             | Use Case                                           | Example / Description                                                    |
| --------------------- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| `@staticmethod`       | No `self`, like a normal function inside class     | Utility functions that do not need instance or class reference           |
| `@classmethod`        | First parameter `cls`, works with class not object | Alternative constructors or methods that operate on class level          |
| `@property`           | Treats method as an attribute                      | Read-only attributes, accessed like `obj.attr` instead of `obj.method()` |
| `@<property>.setter`  | Set property values                                | Modify attributes safely, e.g., validation before setting                |
| `@<property>.deleter` | Delete property                                    | Remove attribute safely, e.g., cleanup logic                             |

 </h6>

## Python Decorators Table
 <h6>

| Decorator                    | Scope    | Use Case / Description                                                                              |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `@staticmethod`              | Class    | Instance লাগবে না, normal function inside class হিসেবে ব্যবহার করা হয়। Utility functions তৈরি করতে। |
| `@classmethod`               | Class    | First parameter `cls`, class-level method। Alternative constructors বা class-level logic এর জন্য।   |
| `@property`                  | Class    | Method কে attribute হিসেবে ব্যবহার করতে দেয়। Read-only attribute।                                   |
| `@<property>.setter`         | Class    | Property value set করার জন্য। Validation বা modification safely করা যায়।                            |
| `@<property>.deleter`        | Class    | Property delete করার জন্য। Cleanup logic বা attribute remove।                                       |
| `@functools.lru_cache`       | Function | Function result cache করার জন্য। Expensive calculation optimization।                                |
| `@functools.wraps`           | Function | Wrapper function creation, original function metadata (name, doc) preserve করার জন্য।               |
| `@contextlib.contextmanager` | Function | Function কে context manager বানায়। `with` statement support করতে।                                   |
| `@dataclass`                 | Class    | Class কে automatic init, repr, eq, hash methods সহ বানায়।                                           |
| `@abstractmethod`            | Class    | Abstract base class method define করতে। Subclass implement করতে বাধ্য।                              |
| `@singledispatch`            | Function | Generic function support, type-specific behavior override করতে।                                     |
| `@staticmethod`              | Class    | Utility functions, instance reference ছাড়া call করা যায়।                                            |
| `@classmethod`               | Class    | Alternative constructors বা class-level logic।                                                      |
| `@decorator_function`        | Function | Custom decorator, function behavior modify করতে।                                                    |

 </h6>
